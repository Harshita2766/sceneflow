# 🎬 SceneFlow — AI-Assisted Story Analysis for Video Editing

SceneFlow is an AI-assisted system that analyzes raw scripts or scene descriptions and structures them into narrative phases such as **Intro**, **Build**, and **Climax** — helping creators understand story flow *before* timeline-based editing.

> 📌 **Note:** The primary evaluation artifact for this project is the Jupyter Notebook  
> 👉 `sceneflow.ipynb`

---

## 🚀 Project Motivation

Video editors and filmmakers often start with unstructured scripts or rough ideas. Translating these into a coherent editing timeline requires experience, intuition, and repeated trial-and-error.

SceneFlow reduces this friction by providing:
- Automated story flow analysis
- Pre-editing narrative understanding
- Faster creative decision-making

---

## 🧠 AI Approach

SceneFlow uses a **lightweight, explainable NLP-inspired rule-based system** that:
- Analyzes script progression
- Detects narrative intensity
- Maps content into cinematic phases

### Narrative Phases
- **Intro** — setup and context
- **Build** — tension and progression
- **Climax** — peak action or emotional moments

This approach was intentionally chosen for:
- Transparency
- Speed
- Reproducibility
- Educational clarity

---

## 🏗 System Architecture

Script Input
↓
Text Cleaning
↓
Sequential Analysis
↓
Narrative Phase Mapping
↓
Structured Output


The same analysis logic is used in both:
- `sceneflow.ipynb` (main evaluation)
- `app.py` (interactive demo)

---

## 📓 Primary Evaluation Notebook

📌 **File:** `sceneflow.ipynb`

The notebook includes:
- Problem definition and objectives
- Real-world relevance
- System and architecture design
- Core AI implementation
- Sample inference outputs
- Evaluation and analysis
- Ethical considerations
- Conclusion and future scope

This notebook runs **top-to-bottom without errors** and serves as the **main source of truth** for evaluation.

---

## 🌐 Demo Application (Supporting)

📌 **File:** `app.py`

A simple interactive web interface built using **Gradio** allows users to:
- Paste scripts
- Receive structured story analysis
- Visualize narrative phases

> The demo is a supporting artifact and not required for primary evaluation.

---

## ⚙️ Installation & Usage (Optional)

```bash
pip install -r requirements.txt
python app.py

⚠️ Ethical & Responsible AI Use

No personal data is used

No automated decision-making

Fully explainable logic

Designed as an assistive creative tool

Minimal bias risk due to rule-based approach

🔮 Future Enhancements

Integration with Large Language Models (LLMs)

Scene pacing and shot suggestions

Timeline export for video editors

Multilingual script analysis

Deeper semantic understanding

👩‍💻 Author

Harshita

📎 Important Links

📓 Main Notebook: sceneflow.ipynb

🌐 Demo App: app.py


---

# 🟢 STEP 3: `requirements.txt` (MINIMAL & SAFE)

```txt
gradio
