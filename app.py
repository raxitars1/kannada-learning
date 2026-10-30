import streamlit as st

st.set_page_config(
    page_title="My Mobile App Demo",
    page_icon="📱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Simple responsive styling
st.markdown("""
<style>
    .stApp { background: #f4f7fb; }
    .block-container { max-width: 520px; padding-top: 1.2rem; }
    .app-header {
        background: linear-gradient(135deg, #3157d5, #6d8cff);
        color: white; padding: 22px; border-radius: 18px;
        text-align: center; margin-bottom: 18px;
    }
    .app-card {
        background: white; padding: 18px; border-radius: 16px;
        border: 1px solid #e7ebf3; margin: 10px 0;
        box-shadow: 0 3px 12px rgba(30,50,90,.05);
    }
    .muted { color: #667085; font-size: 14px; }
    div.stButton > button { width: 100%; border-radius: 12px; min-height: 44px; }
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "Home"

def go(page):
    st.session_state.page = page

st.markdown(
    '<div class="app-header"><h1>📱 My Mobile App</h1>'
    '<p style="margin:0">A simple Python mobile-layout demo</p></div>',
    unsafe_allow_html=True
)

# Navigation
nav1, nav2, nav3 = st.columns(3)
with nav1:
    if st.button("🏠 Home"):
        go("Home")
with nav2:
    if st.button("🔐 Login"):
        go("Login")
with nav3:
    if st.button("👤 Profile"):
        go("Profile")

st.divider()

if st.session_state.page == "Home":
    st.subheader("Welcome!")
    st.write("Explore the sample screens of this basic mobile application.")
    st.markdown('<div class="app-card"><h3>📚 Learn</h3><p class="muted">Understand mobile app screens and navigation.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="app-card"><h3>🎨 Design</h3><p class="muted">A clean layout that adjusts to different screen widths.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="app-card"><h3>🧭 Navigate</h3><p class="muted">Use the Home, Login and Profile buttons above.</p></div>', unsafe_allow_html=True)
    st.info("This is a demonstration app. It does not store user accounts or passwords.")

elif st.session_state.page == "Login":
    st.subheader("Login Screen")
    st.write("Enter sample details to preview a login form.")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Sign in", type="primary"):
        if username.strip() and password:
            st.success(f"Welcome, {username}! (Demo only)")
        else:
            st.warning("Please enter both username and password.")
    st.caption("Demo only: do not enter a real password.")

elif st.session_state.page == "Profile":
    st.subheader("Profile Screen")
    st.markdown('<div class="app-card"><h2 style="text-align:center">👤</h2><h3 style="text-align:center">Student Profile</h3><p style="text-align:center" class="muted">Mobile App Development Learner</p></div>', unsafe_allow_html=True)
    st.write("**Name:** Student")
    st.write("**Course:** BCA")
    st.write("**Technology:** Python and Streamlit")
    st.write("**Project:** Basic Mobile Application UI")

st.divider()
st.caption("Python + Streamlit | Educational practical project")
