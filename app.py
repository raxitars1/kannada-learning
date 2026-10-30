import streamlit as st
from datetime import date

st.set_page_config(page_title="Pocket Tasks", page_icon="✅", layout="centered")

st.markdown("""
<style>
.stApp { background: #f3f6fb; }
.block-container { max-width: 720px; padding-top: 1.2rem; }
.hero { padding: 22px; border-radius: 18px; color: white;
        background: linear-gradient(120deg,#3157d5,#7b61d1); margin-bottom: 16px; }
.task-card { background: white; border: 1px solid #e4e9f2;
             padding: 14px 16px; border-radius: 14px; margin: 8px 0; }
.small-muted { color: #687386; font-size: 13px; }
div.stButton > button { border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

if "tasks" not in st.session_state:
    st.session_state.tasks = [
        {"id": 1, "title": "Read mobile UI notes", "category": "Study", "due": str(date.today()), "done": False},
        {"id": 2, "title": "Practice Python", "category": "Personal", "due": str(date.today()), "done": True},
    ]
if "page" not in st.session_state:
    st.session_state.page = "Tasks"
if "next_id" not in st.session_state:
    st.session_state.next_id = 3

def navigate(page):
    st.session_state.page = page

st.markdown('<div class="hero"><h1>✅ Pocket Tasks</h1><p style="margin:0">A simple mobile-friendly To-Do application</p></div>', unsafe_allow_html=True)

nav = st.columns(3)
for col, label, page in zip(nav, ["📋 Tasks", "➕ Add Task", "📊 Summary"], ["Tasks", "Add Task", "Summary"]):
    with col:
        if st.button(label, use_container_width=True):
            navigate(page)

st.divider()

tasks = st.session_state.tasks

if st.session_state.page == "Add Task":
    st.subheader("Add a new task")
    with st.form("add_task_form", clear_on_submit=True):
        title = st.text_input("Task name *", placeholder="e.g. Complete assignment")
        category = st.selectbox("Category", ["Study", "Work", "Personal", "Shopping", "Other"])
        due = st.date_input("Due date", value=date.today())
        submitted = st.form_submit_button("Add task", type="primary", use_container_width=True)
    if submitted:
        clean_title = title.strip()
        if not clean_title:
            st.error("Please enter a task name.")
        elif len(clean_title) > 80:
            st.error("Task name must be 80 characters or fewer.")
        else:
            st.session_state.tasks.append({
                "id": st.session_state.next_id,
                "title": clean_title,
                "category": category,
                "due": str(due),
                "done": False
            })
            st.session_state.next_id += 1
            st.success("Task added successfully!")
            st.session_state.page = "Tasks"
            st.rerun()
    st.caption("* Required field. Task names cannot be empty and are limited to 80 characters.")

elif st.session_state.page == "Summary":
    st.subheader("Your progress")
    total = len(tasks)
    completed = sum(1 for task in tasks if task["done"])
    pending = total - completed
    a, b, c = st.columns(3)
    a.metric("Total", total)
    b.metric("Completed", completed)
    c.metric("Pending", pending)
    st.progress(completed / total if total else 0)
    counts = {}
    for task in tasks:
        counts[task["category"]] = counts.get(task["category"], 0) + 1
    st.markdown("**Tasks by category**")
    if counts:
        for category, count in sorted(counts.items()):
            st.write(f"- {category}: {count}")
    else:
        st.info("No tasks yet. Add your first task.")

else:
    st.subheader("My tasks")
    if not tasks:
        st.info("Your task list is empty. Select **Add Task** to create one.")
    else:
        filter_category = st.selectbox("Filter by category", ["All"] + sorted({t["category"] for t in tasks}))
        show = [t for t in tasks if filter_category == "All" or t["category"] == filter_category]
        for task in show:
            with st.container():
                st.markdown('<div class="task-card">', unsafe_allow_html=True)
                left, right = st.columns([5, 1])
                with left:
                    new_done = st.checkbox(
                        f"{'~~' if task['done'] else ''}{task['title']}",
                        value=task["done"],
                        key=f"done_{task['id']}"
                    )
                    if new_done != task["done"]:
                        task["done"] = new_done
                        st.rerun()
                    st.markdown(
                        f'<span class="small-muted">Category: {task["category"]} · Due: {task["due"]}</span>',
                        unsafe_allow_html=True
                    )
                with right:
                    if st.button("🗑️", key=f"delete_{task['id']}", help="Delete task"):
                        st.session_state.tasks = [t for t in st.session_state.tasks if t["id"] != task["id"]]
                        st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

st.divider()
st.caption("Python + Streamlit · Educational project · Tasks are stored in session memory and reset when the session ends.")
