# Codder-Agent

Codder-Agent is an AI-powered software engineering assistant that converts a simple project idea into a structured development plan and generates the project files automatically.

The project is built using **LangGraph** to orchestrate multiple AI agents. Instead of asking a single LLM to generate an entire application, Codder-Agent breaks the work into different stages such as planning, architecture design, and code generation.

This project is mainly an experiment to understand how multi-agent AI systems can automate parts of the software development lifecycle.

---

## How it works

The workflow consists of three AI agents:

**Planner**

* Understands the user's project idea.
* Creates a high-level development plan.

**Architect**

* Converts the plan into implementation tasks.
* Decides which files need to be created or modified.

**Coder**

* Uses tools to read, create and update project files.
* Generates code step by step.

```
User Idea
    │
    ▼
 Planner
    │
    ▼
 Architect
    │
    ▼
  Coder
    │
    ▼
Generated Project
```

---

## Tech Stack

* Python
* LangGraph
* LangChain
* Groq API
* Streamlit
* Pydantic
* python-dotenv

---

## Project Structure

```
Codder-agent
│
├── agent/
│   ├── graph.py
│   ├── prompts.py
│   ├── states.py
│   ├── tools.py
│   └── __init__.py
│
├── generated_project/
├── app.py
├── main.py
├── pyproject.toml
├── README.md
└── .env
```

---

## Getting Started

Clone the repository:

```bash
git clone https://github.com/<your-username>/Codder-agent.git
cd Codder-agent
```

Create a virtual environment and install dependencies:

```bash
uv venv
uv sync
```

Activate the virtual environment:

**Windows**

```bash
.venv\Scripts\activate
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Start the application:

```bash
streamlit run app.py
```

or

```bash
python main.py
```

---

## Current Features

* Multi-agent workflow using LangGraph
* AI project planning
* Architecture generation
* AI code generation
* File creation and editing tools
* Streamlit interface
* Modular project structure

---

## Current Limitations

* Groq token limits can affect larger projects.
* Generated code may require manual review.
* Retry handling and execution monitoring are still being improved.

---

If you have suggestions or find issues, feel free to open an issue or submit a pull request.
