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

    import os
    import shutil
    project_dir = "generated_project"
    
    if os.path.exists(project_dir):
        st.subheader("🎉 Your project is ready!")
        
        # Create ZIP file for download
        shutil.make_archive("generated_project", 'zip', project_dir)
        with open("generated_project.zip", "rb") as f:
            st.download_button(
                label="📥 Download Project (ZIP)",
                data=f,
                file_name="generated_project.zip",
                mime="application/zip",
                use_container_width=True
            )
            
        st.info("💻 **To run locally:**\n1. Extract the ZIP\n2. Open terminal in the extracted folder\n3. Run `python -m http.server 8000` (for HTML/JS projects)\n4. Open `http://localhost:8000` in your browser.")

    output_placeholder.json(result)
