import streamlit as st
from agent.graph import agent

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(page_title="AI Engineering Planner", page_icon="🧠", layout="wide")

# -----------------------------
# Header
# -----------------------------
st.title("🧠 AI Engineering Planner")
st.caption("Turn your ideas into complete software projects using AI agents.")

# -----------------------------
# Project Input
# -----------------------------
st.subheader("📝 Project Idea")

project_prompt = st.text_area(
    "Describe the application you want to build",
    height=200,
    placeholder="Example:\nBuild a modern To-Do application using HTML CSS and JavaScript.",
    key="project_prompt",
)

# -----------------------------
# Generate Button
# -----------------------------
generate = st.button(
    "🚀 Generate Project", use_container_width=True, key="generate_btn"
)

# -----------------------------
# Status Section
# -----------------------------
st.divider()
st.subheader("⚙️ Status")

status_placeholder = st.empty()

# -----------------------------
# Output Section
# -----------------------------
st.divider()
st.subheader("📄 Output")

output_placeholder = st.empty()

# -----------------------------
# Default Status
# -----------------------------
status_placeholder.info("🟢 Ready to generate your project.")

# -----------------------------
# Button Action
# -----------------------------
if generate:
    if not project_prompt.strip():
        status_placeholder.error("Please enter a project idea.")
        st.stop()

    status_placeholder.info("🤖 AI Engineering Planner is working...")

    result = agent.invoke(
        {"user_prompt": project_prompt},
        {"recursion_limit": 100},
    )

    status_placeholder.success("✅ Project Generated Successfully!")

    output_placeholder.json(result)
