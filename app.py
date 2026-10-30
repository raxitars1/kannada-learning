import requests
import streamlit as st
from datetime import datetime, timezone

st.set_page_config(page_title="CloudConnect", page_icon="☁️", layout="centered")

st.markdown("""
<style>
.stApp { background:#f3f7fb; }
.block-container { max-width:820px; padding-top:1.2rem; }
.hero { background:linear-gradient(120deg,#2457c5,#5b8def); color:white;
        padding:22px; border-radius:18px; margin-bottom:16px; }
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="hero"><h1>☁️ CloudConnect</h1>'
    '<p style="margin:0">REST API + Firebase Authentication + Cloud Firestore demo</p></div>',
    unsafe_allow_html=True
)

# Firebase settings are read from Streamlit secrets. Never put real keys in source control.
def firebase_config():
    try:
        cfg = st.secrets["firebase"]
        return {
            "api_key": cfg["api_key"],
            "project_id": cfg["project_id"]
        }
    except Exception:
        return None

def firebase_auth(endpoint, email, password, api_key):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:{endpoint}?key={api_key}"
    response = requests.post(
        url,
        json={"email": email, "password": password, "returnSecureToken": True},
        timeout=20
    )
    data = response.json()
    if not response.ok:
        message = data.get("error", {}).get("message", "Firebase authentication failed")
        raise ValueError(message)
    return data

def firestore_url(project_id, collection="tasks"):
    return f"https://firestore.googleapis.com/v1/projects/{project_id}/databases/(default)/documents/{collection}"

def fs_value(value):
    if isinstance(value, bool):
        return {"booleanValue": value}
    if isinstance(value, int):
        return {"integerValue": str(value)}
    return {"stringValue": str(value)}

def firestore_add(project_id, token, uid, title, category):
    url = firestore_url(project_id)
    payload = {
        "fields": {
            "ownerUid": fs_value(uid),
            "title": fs_value(title),
            "category": fs_value(category),
            "createdAt": fs_value(datetime.now(timezone.utc).isoformat())
        }
    }
    r = requests.post(
        url,
        params={"documentId": f"{uid}_{int(datetime.now().timestamp() * 1000)}"},
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        json=payload,
        timeout=20
    )
    data = r.json()
    if not r.ok:
        raise ValueError(data.get("error", {}).get("message", "Could not save document"))
    return data

def firestore_list(project_id, token):
    r = requests.get(
        firestore_url(project_id),
        headers={"Authorization": f"Bearer {token}"},
        timeout=20
    )
    data = r.json()
    if not r.ok:
        raise ValueError(data.get("error", {}).get("message", "Could not load documents"))
    return data.get("documents", [])

def decode_fields(doc):
    fields = doc.get("fields", {})
    def val(key):
        item = fields.get(key, {})
        return item.get("stringValue", item.get("integerValue", item.get("booleanValue", "")))
    return {
        "Document": doc.get("name", "").split("/")[-1],
        "Title": val("title"),
        "Category": val("category"),
        "Owner UID": val("ownerUid"),
        "Created": val("createdAt")
    }

tab_api, tab_auth, tab_cloud, tab_info = st.tabs(
    ["🌐 REST API", "🔐 Firebase Login", "☁️ Cloud Tasks", "📘 Setup & Docs"]
)

with tab_api:
    st.subheader("Consume a REST API")
    st.write("This example sends an HTTP GET request and parses the JSON response from JSONPlaceholder.")
    post_id = st.number_input("Post ID", min_value=1, max_value=100, value=1, step=1)
    if st.button("Send GET request", type="primary"):
        try:
            response = requests.get(
                f"https://jsonplaceholder.typicode.com/posts/{post_id}", timeout=15
            )
            st.caption(f"HTTP status: {response.status_code}")
            response.raise_for_status()
            payload = response.json()
            st.success("JSON response received and parsed.")
            st.write(f"**Title:** {payload.get('title', '')}")
            st.write(f"**Body:** {payload.get('body', '')}")
            with st.expander("View raw JSON"):
                st.json(payload)
        except requests.RequestException as exc:
            st.error(f"API request failed: {exc}")

with tab_auth:
    st.subheader("Firebase user registration and login")
    cfg = firebase_config()
    if not cfg:
        st.warning("Firebase is not configured yet. Follow Setup & Docs and add your Firebase API key and project ID to `.streamlit/secrets.toml`.")
    mode = st.radio("Choose action", ["Register", "Login"], horizontal=True)
    email = st.text_input("Email address", key="auth_email")
    password = st.text_input("Password", type="password", key="auth_password")
    if st.button(mode, type="primary", use_container_width=True):
        if not email.strip() or not password:
            st.error("Enter both email and password.")
        elif len(password) < 6:
            st.error("Firebase email/password accounts require at least 6 characters.")
        elif not cfg:
            st.error("Add Firebase configuration first.")
        else:
            try:
                endpoint = "signUp" if mode == "Register" else "signInWithPassword"
                auth_data = firebase_auth(endpoint, email.strip(), password, cfg["api_key"])
                st.session_state["firebase_token"] = auth_data["idToken"]
                st.session_state["firebase_uid"] = auth_data["localId"]
                st.session_state["firebase_email"] = auth_data.get("email", email.strip())
                st.session_state["firebase_project"] = cfg["project_id"]
                st.success(f"{mode} successful. Signed in as {st.session_state['firebase_email']}.")
            except (ValueError, KeyError) as exc:
                st.error(str(exc))

    if st.session_state.get("firebase_uid"):
        st.info(f"Signed in: {st.session_state.get('firebase_email')} · UID: {st.session_state['firebase_uid']}")
        if st.button("Sign out"):
            for key in ["firebase_token", "firebase_uid", "firebase_email", "firebase_project"]:
                st.session_state.pop(key, None)
            st.rerun()

with tab_cloud:
    st.subheader("Save and read cloud tasks")
    if not st.session_state.get("firebase_token"):
        st.info("Register or log in using the Firebase Login tab to access your cloud tasks.")
    else:
        task_title = st.text_input("Task title", key="cloud_title")
        task_category = st.selectbox("Category", ["Study", "Work", "Personal", "Other"])
        if st.button("Save task to Firestore", type="primary"):
            if not task_title.strip():
                st.error("Task title cannot be empty.")
            else:
                try:
                    firestore_add(
                        st.session_state["firebase_project"],
                        st.session_state["firebase_token"],
                        st.session_state["firebase_uid"],
                        task_title.strip(),
                        task_category
                    )
                    st.success("Task saved to Cloud Firestore.")
                except (ValueError, requests.RequestException) as exc:
                    st.error(str(exc))
        if st.button("Load cloud tasks"):
            try:
                documents = firestore_list(
                    st.session_state["firebase_project"],
                    st.session_state["firebase_token"]
                )
                own_docs = [
                    decode_fields(doc) for doc in documents
                    if doc.get("fields", {}).get("ownerUid", {}).get("stringValue")
                    == st.session_state["firebase_uid"]
                ]
                if own_docs:
                    st.dataframe(own_docs, use_container_width=True, hide_index=True)
                else:
                    st.info("No tasks found for this account.")
            except (ValueError, requests.RequestException) as exc:
                st.error(str(exc))

with tab_info:
    st.subheader("Project learning outcomes")
    st.markdown("""
    - **REST API:** HTTP GET request, status codes, timeout and error handling.
    - **JSON:** Parse API responses and display selected fields.
    - **Firebase Authentication:** Register and sign in with email/password.
    - **Cloud Firestore:** Save and retrieve task documents.
    - **Data model:** Each task has `ownerUid`, `title`, `category`, and `createdAt`.
    """)
    st.markdown("**Configuration required**")
    st.code("""[firebase]
api_key = "YOUR_FIREBASE_WEB_API_KEY"
project_id = "YOUR_FIREBASE_PROJECT_ID"
""", language="toml")
    st.markdown("Create this file at `.streamlit/secrets.toml` beside `app.py`. Do not upload it to GitHub.")
    st.markdown("**Firestore collection:** `tasks`")
    st.code("""tasks/{documentId}
  ownerUid: string
  title: string
  category: string
  createdAt: string (ISO 8601)
""", language="text")
    st.markdown("**Recommended Firestore security rules**")
    st.code("""rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /tasks/{taskId} {
      allow create: if request.auth != null
                    && request.resource.data.ownerUid == request.auth.uid
                    && request.resource.data.title is string
                    && request.resource.data.title.size() > 0
                    && request.resource.data.title.size() <= 100;
      allow read, delete: if request.auth != null
                          && resource.data.ownerUid == request.auth.uid;
      allow update: if request.auth != null
                    && resource.data.ownerUid == request.auth.uid
                    && request.resource.data.ownerUid == request.auth.uid;
    }
  }
}""", language="javascript")
    st.warning("Publish and test Firestore rules in Firebase Console. Never use open rules such as allow read, write: if true.")
    st.markdown("**Firebase Console:** https://console.firebase.google.com/")
    st.markdown("**REST API guide:** https://firebase.google.com/docs/firestore/use-rest-api")
    st.markdown("**Authentication REST API:** https://firebase.google.com/docs/reference/rest/auth")

st.divider()
st.caption("Educational demo · Keep Firebase secrets private · Configure Firestore rules before real use.")
