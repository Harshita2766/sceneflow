import gradio as gr
import time

# ---------------- AI LOGIC ----------------
def analyze_script(script):
    time.sleep(1)

    lines = [l.strip() for l in script.split("\n") if l.strip()]
    n = len(lines)

    intro = lines[: max(1, n//4)]
    build = lines[max(1, n//4): max(2, n//3)]
    climax = lines[max(2, n//3):]

    return f"""
✨ SCENEFLOW AI STORY ANALYSIS ✨

🎬 INTRO — Atmosphere & Setup
{chr(10).join("• "+l for l in intro)}

🚀 BUILD — Rising Momentum
{chr(10).join("• "+l for l in build)}

🔥 CLIMAX — Peak Emotion
{chr(10).join("• "+l for l in climax)}

🎧 EDITING SUGGESTIONS
• Slow ambient music → cinematic rise
• Increase cuts per second gradually
• Use beat drops for emotional punches
• End with a 2s silence hold
"""

# ---------------- STYLING ----------------
custom_css = """
body {
    background: radial-gradient(circle at top, #0b1220, #000);
    overflow-x: hidden;
}

/* Floating glow orbs */
.orb {
    position: fixed;
    width: 180px;
    height: 180px;
    border-radius: 50%;
    filter: blur(90px);
    opacity: 0.6;
    animation: float 12s infinite ease-in-out;
    z-index: 0;
}
.orb.blue { background: #4f9cff; top: 10%; left: 5%; }
.orb.cyan { background: #00ffd5; bottom: 15%; right: 8%; animation-delay: 2s; }
.orb.pink { background: #ff6b9f; top: 50%; right: 20%; animation-delay: 4s; }

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-40px); }
    100% { transform: translateY(0px); }
}

.hero {
    text-align: center;
    padding: 140px 20px 100px;
    position: relative;
    z-index: 1;
}

.logo {
    font-size: 5rem;
    font-weight: 900;
    background: linear-gradient(90deg, #00ffd5, #4f9cff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glow 3s ease-in-out infinite;
}

@keyframes glow {
    0% { text-shadow: 0 0 10px #00ffd5; }
    50% { text-shadow: 0 0 40px #4f9cff; }
    100% { text-shadow: 0 0 10px #00ffd5; }
}

.subtitle {
    color: #cbd5e1;
    font-size: 1.2rem;
    margin-top: 14px;
}

.section {
    max-width: 950px;
    margin: auto;
    padding: 80px 20px;
    position: relative;
    z-index: 1;
}

.card {
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(18px);
    border-radius: 22px;
    padding: 28px;
    box-shadow: 0 0 40px rgba(0,255,213,0.15);
    margin-bottom: 40px;
    animation: fadeUp 1s ease forwards;
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

.timeline {
    display: flex;
    gap: 14px;
    margin-top: 18px;
}

.block {
    flex: 1;
    padding: 18px;
    border-radius: 16px;
    font-weight: 700;
    text-align: center;
    color: black;
}

.intro { background: #00ffd5; }
.build { background: #4f9cff; }
.climax { background: #ff6b6b; }

button {
    background: linear-gradient(90deg, #00ffd5, #4f9cff) !important;
    color: black !important;
    font-weight: 700 !important;
    border-radius: 14px !important;
}
"""

# ---------------- APP ----------------
with gr.Blocks(
    css=custom_css,
    title="SceneFlow — AI Film Editing Assistant"
) as demo:

    # Floating background elements
    gr.HTML("""
    <div class="orb blue"></div>
    <div class="orb cyan"></div>
    <div class="orb pink"></div>
    """)

    # Hero section
    gr.HTML("""
    <div class="hero">
        <div class="logo">SceneFlow</div>
        <div class="subtitle">
            AI that analyzes your story before you edit a single frame
        </div>
    </div>
    """)

    with gr.Column(elem_classes="section"):
        gr.HTML("""
        <div class="card">
            <h2>🧠 How SceneFlow Understands Your Story</h2>
            <p>SceneFlow breaks scripts into emotional phases and suggests edits visually.</p>
            <div class="timeline">
                <div class="block intro">Intro</div>
                <div class="block build">Build</div>
                <div class="block climax">Climax</div>
            </div>
        </div>
        """)

        script_input = gr.Textbox(
            lines=14,
            label="🎬 Paste Script or Scene Notes",
            placeholder="INT. ROOM - NIGHT\nA single light flickers..."
        )

        analyze_btn = gr.Button("✨ Analyze with AI")

        output = gr.Textbox(
            lines=18,
            label="AI Editing & Story Breakdown"
        )

        analyze_btn.click(analyze_script, script_input, output)

demo.launch()
