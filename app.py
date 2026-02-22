import streamlit as st
import random
import pyperclip

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Content Idea Generator",
    layout="centered"
)

# ---------------- THEME TOGGLE ----------------
if "theme" not in st.session_state:
    st.session_state.theme = "light"

def toggle_theme():
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

# ---------------- CSS THEMES ----------------
light_css = """
<style>
body {
    background-color: #f4f6f8;
}
.app {
    background: #ffffff;
    border-radius: 16px;
    padding: 32px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.12);
}
h1 {
    font-weight: 700;
}
.subtitle {
    color: #555;
    margin-bottom: 24px;
}
.card {
    background: #f8f9fb;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
}
.idea {
    background: #eef2ff;
    border-left: 5px solid #4f46e5;
    padding: 14px;
    border-radius: 8px;
    margin-bottom: 10px;
    font-weight: 500;
}
.footer {
    margin-top: 30px;
    font-size: 14px;
    color: #555;
}
.links a {
    text-decoration: none;
    color: #4f46e5;
    margin-right: 12px;
}
</style>
"""

dark_css = """
<style>
body {
    background-color: #0f172a;
}
.app {
    background: #020617;
    color: #e5e7eb;
    border-radius: 16px;
    padding: 32px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.6);
}
.subtitle {
    color: #9ca3af;
}
.card {
    background: #020617;
    border: 1px solid #1e293b;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
}
.idea {
    background: #020617;
    border-left: 5px solid #38bdf8;
    padding: 14px;
    border-radius: 8px;
    margin-bottom: 10px;
    font-weight: 500;
}
.footer {
    margin-top: 30px;
    font-size: 14px;
    color: #9ca3af;
}
.links a {
    text-decoration: none;
    color: #38bdf8;
    margin-right: 12px;
}
</style>
"""

st.markdown(light_css if st.session_state.theme == "light" else dark_css, unsafe_allow_html=True)

# ---------------- DATA ----------------
ideas = {
    "Instagram": {
        "Travel": [
            "Low-budget travel challenge",
            "Hidden locations most people miss",
            "Solo travel storytelling reel",
            "Common travel mistakes beginners make",
            "Best photography spots guide"
        ],
        "Tech": [
            "Beginner project ideas",
            "Mistakes new developers make",
            "Free tools that improve productivity",
            "How to build your first real project",
            "Why resumes get rejected"
        ]
    },
    "YouTube": {
        "Travel": [
            "Complete destination guide with budget",
            "Is this place worth visiting",
            "Travel planning step-by-step",
            "Cost breakdown travel vlog",
            "Beginner travel mistakes explained"
        ]
    },
    "LinkedIn": {
        "Tech": [
            "Project I built using Python",
            "Lessons learned while learning to code",
            "How I structured my learning roadmap",
            "Resources that helped me grow",
            "Mistakes I fixed in my journey"
        ]
    }
}

fake_ai_templates = [
    "A high-retention content idea for {platform} focused on {topic}",
    "Problem-solution based content idea around {topic}",
    "Storytelling content format explaining {topic}",
    "Beginner-focused educational content on {topic}",
    "Practical mistake-based content idea related to {topic}"
]

# ---------------- SESSION STATE ----------------
if "ideas_list" not in st.session_state:
    st.session_state.ideas_list = []

# ---------------- UI ----------------
st.markdown("<div class='app'>", unsafe_allow_html=True)

st.button(
    "Switch Theme",
    on_click=toggle_theme
)

st.title("Content Idea Generator")
st.markdown("<div class='subtitle'>Generate structured, platform-specific content ideas</div>", unsafe_allow_html=True)

# -------- GENERATOR --------
st.markdown("<div class='card'>", unsafe_allow_html=True)

platform = st.selectbox("Platform", list(ideas.keys()))
niche = st.selectbox("Niche", list(ideas[platform].keys()))
count = st.slider("Number of ideas", 1, 10, 5)

if st.button("Generate Ideas"):
    st.session_state.ideas_list = random.sample(
        ideas[platform][niche],
        min(count, len(ideas[platform][niche]))
    )

st.markdown("</div>", unsafe_allow_html=True)

# -------- DISPLAY --------
if st.session_state.ideas_list:
    text_to_copy = ""
    for idea in st.session_state.ideas_list:
        st.markdown(f"<div class='idea'>{idea}</div>", unsafe_allow_html=True)
        text_to_copy += idea + "\n"

    if st.button("Copy Ideas"):
        pyperclip.copy(text_to_copy)
        st.success("Copied to clipboard")

# -------- SMART AI (FREE) --------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("Smart Idea Generator")

topic = st.text_input("Describe your topic")

if st.button("Generate Smart Idea"):
    if topic:
        template = random.choice(fake_ai_templates)
        smart_idea = template.format(platform=platform, topic=topic)
        st.markdown(f"<div class='idea'>{smart_idea}</div>", unsafe_allow_html=True)
    else:
        st.warning("Please enter a topic")

st.markdown("</div>", unsafe_allow_html=True)

# -------- PROFILE & CONTACT --------
st.markdown("<div class='footer'>", unsafe_allow_html=True)
st.markdown("### Developer")
st.markdown("**Hiranmoy Pati**  Python | Web | Automation | Content Tools")

st.markdown(
    """
<div class="links">
<a href="https://hiranmoypati.com" target="_blank">Website</a>
<a href="https://github.com/hiranmoy-pati" target="_blank">GitHub</a>
<a href="https://www.linkedin.com/in/hiranmoy-pati/" target="_blank">LinkedIn</a>
<a href="mailto:contact@hiranmoypati.com">Email</a>
</div>
""",
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)