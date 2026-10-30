import random
import streamlit as st

# ------------------------------------------------------------
# With You Kannada - Streamlit learning application
# Run: streamlit run app.py
# ------------------------------------------------------------

st.set_page_config(
    page_title="With You Kannada",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Styling ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Kannada:wght@400;500;600;700&display=swap');

html, body, [class*="css"], [data-testid="stAppViewContainer"] {
    font-family: 'Noto Sans Kannada', sans-serif;
}
.stApp {
    background: linear-gradient(180deg, #eef8ff 0%, #ffffff 48%, #f5fbff 100%);
}
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}
.hero {
    background: linear-gradient(120deg, #d8efff, #f5fbff);
    border: 1px solid #c4e5fb;
    border-radius: 24px;
    padding: 26px;
    margin-bottom: 20px;
}
.hero h1 { color: #125c91; margin-bottom: 6px; }
.hero p { color: #376783; font-size: 1.05rem; }
.small-tag {
    display: inline-block; background: white; color: #17699f;
    padding: 6px 12px; border-radius: 999px; margin: 3px;
    border: 1px solid #cde8fa; font-size: 0.9rem;
}
.lesson-card {
    background: white; border: 1px solid #d9ecf8; border-radius: 18px;
    padding: 18px; min-height: 125px; box-shadow: 0 3px 12px #d9edf833;
}
.lesson-card h3 { color: #155d91; margin-top: 0; }
.kannada-big { font-size: 1.6rem; line-height: 2; color: #155d91; }
div.stButton > button {
    border-radius: 12px; border: 1px solid #b9def5;
    background: #e5f4ff; color: #155d91; font-weight: 600;
}
div.stButton > button:hover {
    background: #cdeaff; border-color: #8dcaf0; color: #0c4f80;
}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------- Learning content ----------
VOWELS = ["ಅ", "ಆ", "ಇ", "ಈ", "ಉ", "ಊ", "ಋ", "ಎ", "ಏ", "ಐ", "ಒ", "ಓ", "ಔ", "ಅಂ", "ಅಃ"]
CONSONANTS = [
    "ಕ", "ಖ", "ಗ", "ಘ", "ಙ", "ಚ", "ಛ", "ಜ", "ಝ", "ಞ",
    "ಟ", "ಠ", "ಡ", "ಢ", "ಣ", "ತ", "ಥ", "ದ", "ಧ", "ನ",
    "ಪ", "ಫ", "ಬ", "ಭ", "ಮ", "ಯ", "ರ", "ಲ", "ವ", "ಶ",
    "ಷ", "ಸ", "ಹ", "ಳ"
]
GUNITAKSHARA = {
    "ಕ": ["ಕ", "ಕಾ", "ಕಿ", "ಕೀ", "ಕು", "ಕೂ", "ಕೃ", "ಕೆ", "ಕೇ", "ಕೈ", "ಕೊ", "ಕೋ", "ಕೌ", "ಕಂ", "ಕಃ"],
    "ಗ": ["ಗ", "ಗಾ", "ಗಿ", "ಗೀ", "ಗು", "ಗೂ", "ಗೃ", "ಗೆ", "ಗೇ", "ಗೈ", "ಗೊ", "ಗೋ", "ಗೌ", "ಗಂ", "ಗಃ"],
    "ಮ": ["ಮ", "ಮಾ", "ಮಿ", "ಮೀ", "ಮು", "ಮೂ", "ಮೃ", "ಮೆ", "ಮೇ", "ಮೈ", "ಮೊ", "ಮೋ", "ಮೌ", "ಮಂ", "ಮಃ"],
    "ನ": ["ನ", "ನಾ", "ನಿ", "ನೀ", "ನು", "ನೂ", "ನೃ", "ನೆ", "ನೇ", "ನೈ", "ನೊ", "ನೋ", "ನೌ", "ನಂ", "ನಃ"],
    "ಪ": ["ಪ", "ಪಾ", "ಪಿ", "ಪೀ", "ಪು", "ಪೂ", "ಪೃ", "ಪೆ", "ಪೇ", "ಪೈ", "ಪೊ", "ಪೋ", "ಪೌ", "ಪಂ", "ಪಃ"],
}

WORD_BANK = {
    "ಎರಡು ಅಕ್ಷರದ ಪದಗಳು": ["ಮನೆ", "ಮರ", "ಹಸು", "ಕವಿ", "ನದಿ", "ಹಣ್ಣು", "ಅಮ್ಮ", "ಅಪ್ಪ", "ಕೈ", "ಕಾಲು"],
    "ಮೂರು ಅಕ್ಷರದ ಪದಗಳು": ["ಕಮಲ", "ಕಡಲೆ", "ಬಾಳೆಹಣ್ಣು", "ಮಗು", "ಗಿಡವು", "ಆನೆ", "ಕಾಗೆ", "ಕಿಟಕಿ", "ಪುಸ್ತಕ", "ಮಳೆಗಾಲ"],
    "ಸಜಾತಿ ಒತ್ತಕ್ಷರಗಳು": ["ಅಕ್ಕ", "ಅಪ್ಪ", "ಅಮ್ಮ", "ಹಗ್ಗ", "ಕಲ್ಲು", "ಚಿಕ್ಕ", "ಮುತ್ತು", "ಸಕ್ಕರೆ"],
    "ವಿಜಾತಿ ಒತ್ತಕ್ಷರಗಳು": ["ಅಕ್ಷರ", "ವಿದ್ಯೆ", "ಸತ್ಯ", "ಭಕ್ತಿ", "ಶಕ್ತಿ", "ಮಿತ್ರ", "ಚಕ್ರ", "ಪತ್ರ"],
    "ಬಹು ಒತ್ತಕ್ಷರಗಳ ಪದಗಳು": ["ವಿದ್ಯಾರ್ಥಿ", "ಸ್ವಾತಂತ್ರ್ಯ", "ಪ್ರಶ್ನೆ", "ಸಂಸ್ಕೃತಿ", "ಅಭ್ಯಾಸ", "ವ್ಯಕ್ತಿತ್ವ"],
    "ಸರಳ ಪದಗಳು": ["ಮನೆ", "ಮರ", "ಹೂವು", "ನೀರು", "ಹಾಲು", "ಬೆಕ್ಕು", "ನಾಯಿ", "ಸೂರ್ಯ", "ಚಂದ್ರ", "ಪುಸ್ತಕ"],
}

PROVERBS = [
    ("ಅತಿ ಆಸೆ ______", ["ಗತಿ ಕೇಡು", "ಜ್ಞಾನ ಹೆಚ್ಚಳ", "ಹೂವು ಅರಳುವುದು"], "ಗತಿ ಕೇಡು"),
    ("ಒಗ್ಗಟ್ಟಿನಲ್ಲಿ ______", ["ಬಲವಿದೆ", "ನಷ್ಟವಿದೆ", "ಭಯವಿದೆ"], "ಬಲವಿದೆ"),
    ("ಹನಿ ಹನಿಗೂಡಿ ______", ["ಹಳ್ಳ", "ಬೆಟ್ಟ", "ಕಾಡು"], "ಹಳ್ಳ"),
    ("ಮಾತು ಬೆಳ್ಳಿ, ಮೌನ ______", ["ಬಂಗಾರ", "ಕಲ್ಲು", "ಮಣ್ಣು"], "ಬಂಗಾರ"),
    ("ಕೈ ಕೆಸರಾದರೆ ______", ["ಬಾಯಿ ಮೊಸರು", "ಮನೆ ಖಾಲಿ", "ದಾರಿ ದೂರ"], "ಬಾಯಿ ಮೊಸರು"),
    ("ಆಡು ಮುಟ್ಟದ ಸೊಪ್ಪಿಲ್ಲ, ______", ["ಹನುಮಂತ ಮುಟ್ಟದ ಬೆಟ್ಟವಿಲ್ಲ", "ಮಳೆ ಬೀಳದ ಊರಿಲ್ಲ", "ಮರ ಇಲ್ಲದ ಕಾಡಿಲ್ಲ"], "ಹನುಮಂತ ಮುಟ್ಟದ ಬೆಟ್ಟವಿಲ್ಲ"),
    ("ಬಿತ್ತಿದಂತೆ ______", ["ಬೆಳೆಯುವೆ", "ಕೊಯ್ಯುವೆ", "ಓಡುವೆ"], "ಕೊಯ್ಯುವೆ"),
    ("ಕಾಗೆಗೂ ತನ್ನ ______", ["ಮರಿ ಚಿನ್ನ", "ಗೂಡು ದೊಡ್ಡದು", "ರೆಕ್ಕೆ ಬಿಳಿ"], "ಮರಿ ಚಿನ್ನ"),
    ("ದೂರದ ಬೆಟ್ಟ ______", ["ನಣ್ಣಗೆ", "ದೊಡ್ಡದು", "ಕಪ್ಪು"], "ನಣ್ಣಗೆ"),
    ("ಅರಿವೇ ______", ["ಗುರು", "ಶತ್ರು", "ಭಯ"], "ಗುರು"),
]

GK = [
    ("ಭಾರತದ ರಾಷ್ಟ್ರೀಯ ಪ್ರಾಣಿ ಯಾವುದು?", ["ಹುಲಿ", "ಸಿಂಹ", "ಆನೆ", "ಚಿರತೆ"], "ಹುಲಿ"),
    ("ಭಾರತದ ರಾಷ್ಟ್ರೀಯ ಪಕ್ಷಿ ಯಾವುದು?", ["ನವಿಲು", "ಗಿಳಿ", "ಕಾಗೆ", "ಹದ್ದು"], "ನವಿಲು"),
    ("ಭಾರತದ ರಾಷ್ಟ್ರೀಯ ಮರ ಯಾವುದು?", ["ಆಲದ ಮರ", "ಬೇವಿನ ಮರ", "ತೆಂಗಿನ ಮರ", "ಮಾವಿನ ಮರ"], "ಆಲದ ಮರ"),
    ("ಭಾರತದ ರಾಷ್ಟ್ರೀಯ ಹೂವು ಯಾವುದು?", ["ಕಮಲ", "ಗುಲಾಬಿ", "ಮಲ್ಲಿಗೆ", "ಸೂರ್ಯಕಾಂತಿ"], "ಕಮಲ"),
    ("ಭಾರತದ ರಾಜಧಾನಿ ಯಾವುದು?", ["ನವದೆಹಲಿ", "ಮುಂಬೈ", "ಚೆನ್ನೈ", "ಬೆಂಗಳೂರು"], "ನವದೆಹಲಿ"),
    ("ಕರ್ನಾಟಕದ ರಾಜಧಾನಿ ಯಾವುದು?", ["ಬೆಂಗಳೂರು", "ಮೈಸೂರು", "ಹುಬ್ಬಳ್ಳಿ", "ಮಂಗಳೂರು"], "ಬೆಂಗಳೂರು"),
    ("ಕರ್ನಾಟಕದ ರಾಜ್ಯ ಪ್ರಾಣಿ ಯಾವುದು?", ["ಆನೆ", "ಹುಲಿ", "ಸಿಂಹ", "ಜಿಂಕೆ"], "ಆನೆ"),
    ("ಕರ್ನಾಟಕದ ರಾಜ್ಯ ಪಕ್ಷಿ ಯಾವುದು?", ["ನೀಲಕಂಠ", "ನವಿಲು", "ಗಿಳಿ", "ಕೋಗಿಲೆ"], "ನೀಲಕಂಠ"),
    ("ಕರ್ನಾಟಕದ ರಾಜ್ಯ ಮರ ಯಾವುದು?", ["ಶ್ರೀಗಂಧ", "ಆಲದ ಮರ", "ಬೇವಿನ ಮರ", "ಮಾವಿನ ಮರ"], "ಶ್ರೀಗಂಧ"),
    ("ಭಾರತದ ರಾಷ್ಟ್ರಗಾನ ಯಾವುದು?", ["ಜನ ಗಣ ಮನ", "ವಂದೇ ಮಾತರಂ", "ಸಾರೆ ಜಹಾಂ ಸೆ ಅಚ್ಚಾ", "ಜಯ ಭಾರತ ಜನನಿಯ ತನುಜಾತೆ"], "ಜನ ಗಣ ಮನ"),
    ("ಭಾರತದ ಸ್ವಾತಂತ್ರ್ಯ ದಿನ ಯಾವಾಗ?", ["ಆಗಸ್ಟ್ 15", "ಜನವರಿ 26", "ಅಕ್ಟೋಬರ್ 2", "ನವೆಂಬರ್ 14"], "ಆಗಸ್ಟ್ 15"),
    ("ಭಾರತದ ಗಣರಾಜ್ಯೋತ್ಸವ ಯಾವಾಗ?", ["ಜನವರಿ 26", "ಆಗಸ್ಟ್ 15", "ಮೇ 1", "ಜೂನ್ 5"], "ಜನವರಿ 26"),
    ("ಭೂಮಿಯ ಉಪಗ್ರಹ ಯಾವುದು?", ["ಚಂದ್ರ", "ಸೂರ್ಯ", "ಮಂಗಳ", "ಶುಕ್ರ"], "ಚಂದ್ರ"),
    ("ಒಂದು ವಾರದಲ್ಲಿ ಎಷ್ಟು ದಿನಗಳಿವೆ?", ["7", "5", "6", "8"], "7"),
    ("ಸಸ್ಯಗಳು ಆಹಾರ ತಯಾರಿಸಲು ಮುಖ್ಯವಾಗಿ ಯಾವುದನ್ನು ಬಳಸುತ್ತವೆ?", ["ಸೂರ್ಯನ ಬೆಳಕು", "ಚಂದ್ರನ ಬೆಳಕು", "ಮಣ್ಣು ಮಾತ್ರ", "ಗಾಳಿ ಮಾತ್ರ"], "ಸೂರ್ಯನ ಬೆಳಕು"),
]

MATCHES = {
    "ಪ್ರಾಣಿ ಮತ್ತು ಹೆಸರು": {"🐘": "ಆನೆ", "🐯": "ಹುಲಿ", "🐄": "ಹಸು", "🐈": "ಬೆಕ್ಕು"},
    "ಹಣ್ಣು ಮತ್ತು ಹೆಸರು": {"🍎": "ಸೇಬು", "🥭": "ಮಾವು", "🍌": "ಬಾಳೆಹಣ್ಣು", "🍇": "ದ್ರಾಕ್ಷಿ"},
    "ಬಣ್ಣ ಮತ್ತು ಹೆಸರು": {"🔴": "ಕೆಂಪು", "🔵": "ನೀಲಿ", "🟢": "ಹಸಿರು", "🟡": "ಹಳದಿ"},
    "ಭಾರತದ ಚಿಹ್ನೆಗಳು": {"🐅": "ರಾಷ್ಟ್ರೀಯ ಪ್ರಾಣಿ", "🦚": "ರಾಷ್ಟ್ರೀಯ ಪಕ್ಷಿ", "🪷": "ರಾಷ್ಟ್ರೀಯ ಹೂವು", "🌳": "ರಾಷ್ಟ್ರೀಯ ಮರ"},
}

# ---------- Session state ----------
defaults = {
    "points": 0,
    "completed": 0,
    "quiz_question": None,
    "quiz_checked": False,
    "match_pairs": None,
    "match_score": 0,
    "match_round": 0,
    "jumbled_word": None,
    "jumbled_letters": [],
    "jumbled_checked": False,
    "proverb_question": None,
    "proverb_checked": False,
    "gk_question": None,
    "gk_checked": False,
}
for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ---------- Header ----------
st.markdown("""
<div class="hero">
  <h1>📘 With You Kannada</h1>
  <p><b>ಬನ್ನಿ, ಕನ್ನಡ ಕಲಿಯೋಣ!</b> — ಕಲಿಯೋಣ, ಆಡೋಣ, ಕನ್ನಡದಲ್ಲಿ ಮುಂದೆ ಸಾಗೋಣ!</p>
  <span class="small-tag">🌱 Basic to Advanced</span>
  <span class="small-tag">🧩 Word Games</span>
  <span class="small-tag">🏆 Quiz & Rewards</span>
  <span class="small-tag">GFGCW</span>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🧭 ಕಲಿಕೆಯ ವಿಭಾಗಗಳು")
    page = st.radio(
        "ವಿಭಾಗ ಆಯ್ಕೆಮಾಡಿ",
        [
            "🏠 ಮುಖಪುಟ",
            "🔤 ಸ್ವರಗಳು",
            "🅰️ ವ್ಯಂಜನಗಳು",
            "🪄 ಗುಣಿತಾಕ್ಷರಗಳು / ಬಳ್ಳಿಗಳು",
            "📚 ಪದಗಳ ಕಲಿಕೆ",
            "🔗 ಒತ್ತಕ್ಷರಗಳು",
            "📝 ಗಾದೆಮಾತು ಪೂರ್ಣಗೊಳಿಸಿ",
            "🧩 Match the Following",
            "🔀 Jumbled Words",
            "🖼️ ಚಿತ್ರ ಮತ್ತು ಪದ",
            "🌍 ಸಾಮಾನ್ಯ ಜ್ಞಾನ (GK)",
            "📈 ನನ್ನ ಪ್ರಗತಿ",
        ],
    )
    st.divider()
    st.metric("⭐ ನಿಮ್ಮ ಅಂಕಗಳು", st.session_state.points)
    st.caption("Header: GFGCW · Footer: BCA")

# ---------- Pages ----------
if page == "🏠 ಮುಖಪುಟ":
    st.subheader("ನಿಮ್ಮ ಕನ್ನಡ ಕಲಿಕೆಯ ಪಯಣ")
    st.write("ನಿಮಗೆ ಇಷ್ಟವಾದ ವಿಭಾಗ ಆಯ್ಕೆ ಮಾಡಿ. ಪ್ರತಿಯೊಂದು ಪಾಠದ ನಂತರ ಆಟ ಆಡಿ ಮತ್ತು ಅಂಕಗಳನ್ನು ಗಳಿಸಿ.")
    cols = st.columns(3)
    cards = [
        ("🔤", "ಸ್ವರಗಳು", "ಕನ್ನಡದ ಸ್ವರಗಳನ್ನು ಗುರುತಿಸಿ."),
        ("🅰️", "ವ್ಯಂಜನಗಳು", "ವ್ಯಂಜನಗಳನ್ನು ಓದಿ ಅಭ್ಯಾಸ ಮಾಡಿ."),
        ("🪄", "ಗುಣಿತಾಕ್ಷರಗಳು", "ಅಕ್ಷರಗಳಿಗೆ ಸ್ವರ ಚಿಹ್ನೆ ಸೇರಿಸಿ."),
        ("📚", "ಪದಗಳ ಕಲಿಕೆ", "ಸರಳ ಪದಗಳಿಂದ ಮುಂದುವರಿದ ಪದಗಳವರೆಗೆ."),
        ("🔗", "ಒತ್ತಕ್ಷರಗಳು", "ಸಜಾತಿ, ವಿಜಾತಿ ಮತ್ತು ಬಹು ಒತ್ತಕ್ಷರಗಳು."),
        ("📝", "ಗಾದೆಮಾತು", "ಗಾದೆಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸಿ."),
        ("🧩", "Matching Game", "ಸರಿಯಾದ ಜೋಡಿಗಳನ್ನು ಹೊಂದಿಸಿ."),
        ("🔀", "Jumbled Words", "ಅಕ್ಷರಗಳನ್ನು ಸರಿಯಾದ ಕ್ರಮದಲ್ಲಿ ಜೋಡಿಸಿ."),
        ("🌍", "ಸಾಮಾನ್ಯ ಜ್ಞಾನ", "ಭಾರತ ಮತ್ತು ಕರ್ನಾಟಕದ ಬಗ್ಗೆ ತಿಳಿಯಿರಿ."),
    ]
    for i, (emoji, title, desc) in enumerate(cards):
        with cols[i % 3]:
            st.markdown(
                f'<div class="lesson-card"><h3>{emoji} {title}</h3><p>{desc}</p></div>',
                unsafe_allow_html=True,
            )
            st.write("")
    st.info("💡 ಸಲಹೆ: ಮೊದಲು ಸ್ವರಗಳು ಮತ್ತು ವ್ಯಂಜನಗಳನ್ನು ಕಲಿಯಿರಿ. ನಂತರ ಪದಗಳು ಮತ್ತು ಆಟಗಳಿಗೆ ಹೋಗಿ.")

elif page == "🔤 ಸ್ವರಗಳು":
    st.subheader("🔤 ಕನ್ನಡ ಸ್ವರಗಳು")
    st.write("ಸ್ವರಗಳನ್ನು ಜೋರಾಗಿ ಓದಿ. ಪ್ರತಿಯೊಂದು ಅಕ್ಷರವನ್ನು ಗುರುತಿಸುವ ಅಭ್ಯಾಸ ಮಾಡಿ.")
    st.markdown(f'<div class="kannada-big">{"　".join(VOWELS)}</div>', unsafe_allow_html=True)
    st.caption("ಸ್ವರಗಳನ್ನು ನೆನಪಿಟ್ಟುಕೊಳ್ಳಲು ಪ್ರತಿದಿನ ಅಭ್ಯಾಸ ಮಾಡಿ.")
    selected = st.selectbox("ಅಕ್ಷರ ಆಯ್ಕೆ ಮಾಡಿ", VOWELS)
    st.success(f"ನೀವು ಆಯ್ಕೆ ಮಾಡಿದ ಸ್ವರ: **{selected}**")
    if st.button("✅ ಸ್ವರಗಳ ಪಾಠ ಪೂರ್ಣಗೊಳಿಸಿ"):
        st.session_state.points += 5
        st.session_state.completed += 1
        st.success("ಚೆನ್ನಾಗಿದೆ! ನಿಮಗೆ 5 ಅಂಕಗಳು ದೊರೆತಿವೆ.")

elif page == "🅰️ ವ್ಯಂಜನಗಳು":
    st.subheader("🅰️ ಕನ್ನಡ ವ್ಯಂಜನಗಳು")
    for label, letters in [
        ("ಕ ವರ್ಗ", ["ಕ", "ಖ", "ಗ", "ಘ", "ಙ"]),
        ("ಚ ವರ್ಗ", ["ಚ", "ಛ", "ಜ", "ಝ", "ಞ"]),
        ("ಟ ವರ್ಗ", ["ಟ", "ಠ", "ಡ", "ಢ", "ಣ"]),
        ("ತ ವರ್ಗ", ["ತ", "ಥ", "ದ", "ಧ", "ನ"]),
        ("ಪ ವರ್ಗ", ["ಪ", "ಫ", "ಬ", "ಭ", "ಮ"]),
        ("ಇತರೆ ವ್ಯಂಜನಗಳು", ["ಯ", "ರ", "ಲ", "ವ", "ಶ", "ಷ", "ಸ", "ಹ", "ಳ"]),
    ]:
        st.markdown(f"**{label}**")
        st.markdown(f'<div class="kannada-big">{"　".join(letters)}</div>', unsafe_allow_html=True)
    if st.button("✅ ವ್ಯಂಜನಗಳ ಪಾಠ ಪೂರ್ಣಗೊಳಿಸಿ"):
        st.session_state.points += 5
        st.session_state.completed += 1
        st.success("ಅಭಿನಂದನೆಗಳು! 5 ಅಂಕಗಳು ಗಳಿಸಿದ್ದೀರಿ.")

elif page == "🪄 ಗುಣಿತಾಕ್ಷರಗಳು / ಬಳ್ಳಿಗಳು":
    st.subheader("🪄 ಗುಣಿತಾಕ್ಷರಗಳು / ಬಳ್ಳಿಗಳು")
    consonant = st.selectbox("ವ್ಯಂಜನ ಆಯ್ಕೆ ಮಾಡಿ", list(GUNITAKSHARA.keys()))
    st.markdown(f'<div class="kannada-big">{"　".join(GUNITAKSHARA[consonant])}</div>', unsafe_allow_html=True)
    st.write("ಉದಾಹರಣೆ: ಕ + ಾ = ಕಾ, ಕ + ಿ = ಕಿ. ಅಕ್ಷರಗಳನ್ನು ಓದಿ ಮತ್ತು ಬರೆಯಲು ಅಭ್ಯಾಸ ಮಾಡಿ.")
    st.caption("ಇಲ್ಲಿ ಕೆಲವು ಮಾದರಿ ವ್ಯಂಜನಗಳಿವೆ; ಬೇಕಾದರೆ GUNITAKSHARA ಪಟ್ಟಿಗೆ ಹೆಚ್ಚಿನ ವ್ಯಂಜನಗಳನ್ನು ಸೇರಿಸಿ.")
    if st.button("✅ ಗುಣಿತಾಕ್ಷರಗಳ ಪಾಠ ಪೂರ್ಣಗೊಳಿಸಿ"):
        st.session_state.points += 5
        st.session_state.completed += 1
        st.success("ಚೆನ್ನಾಗಿದೆ! 5 ಅಂಕಗಳು ಗಳಿಸಿದ್ದೀರಿ.")

elif page == "📚 ಪದಗಳ ಕಲಿಕೆ":
    st.subheader("📚 ಕನ್ನಡ ಪದಗಳ ಕಲಿಕೆ")
    category = st.selectbox("ಪದಗಳ ಗುಂಪು ಆಯ್ಕೆಮಾಡಿ", list(WORD_BANK.keys()))
    words = WORD_BANK[category]
    st.markdown(f'<div class="kannada-big">{"　 ·　 ".join(words)}</div>', unsafe_allow_html=True)
    st.write("ಕೆಳಗಿನ ಪದಗಳಲ್ಲಿ ಒಂದನ್ನು ಆಯ್ಕೆ ಮಾಡಿ ಓದಿ.")
    chosen_word = st.selectbox("ಪದ ಆಯ್ಕೆ ಮಾಡಿ", words, key="word_practice")
    st.info(f"ಅಭ್ಯಾಸದ ಪದ: **{chosen_word}**")
    if st.button("⭐ ಪದಗಳ ಅಭ್ಯಾಸ ಪೂರ್ಣಗೊಳಿಸಿ"):
        st.session_state.points += 3
        st.session_state.completed += 1
        st.success("ಅದ್ಭುತ! 3 ಅಂಕಗಳು ಗಳಿಸಿದ್ದೀರಿ.")

elif page == "🔗 ಒತ್ತಕ್ಷರಗಳು":
    st.subheader("🔗 ಒತ್ತಕ್ಷರಗಳ ಕಲಿಕೆ")
    kind = st.selectbox("ವಿಭಾಗ ಆಯ್ಕೆಮಾಡಿ", [
        "ಸಜಾತಿ ಒತ್ತಕ್ಷರಗಳು", "ವಿಜಾತಿ ಒತ್ತಕ್ಷರಗಳು", "ಬಹು ಒತ್ತಕ್ಷರಗಳ ಪದಗಳು"
    ])
    words = WORD_BANK[kind]
    st.markdown(f'<div class="kannada-big">{"　 ·　 ".join(words)}</div>', unsafe_allow_html=True)
    st.write("ಪದಗಳನ್ನು ಓದಿ. ಒತ್ತಕ್ಷರ ಇರುವ ಭಾಗವನ್ನು ಗುರುತಿಸಿ.")
    if st.button("⭐ ಒತ್ತಕ್ಷರಗಳ ಪಾಠ ಪೂರ್ಣಗೊಳಿಸಿ"):
        st.session_state.points += 5
        st.session_state.completed += 1
        st.success("ಚೆನ್ನಾಗಿದೆ! 5 ಅಂಕಗಳು ಗಳಿಸಿದ್ದೀರಿ.")

elif page == "📝 ಗಾದೆಮಾತು ಪೂರ್ಣಗೊಳಿಸಿ":
    st.subheader("📝 ಗಾದೆಮಾತು ಪೂರ್ಣಗೊಳಿಸಿ")
    if st.session_state.proverb_question is None:
        st.session_state.proverb_question = random.choice(PROVERBS)
        st.session_state.proverb_checked = False
    question = st.session_state.proverb_question
    st.markdown(f"### {question[0]}")
    answer = st.radio("ಸರಿಯಾದ ಉತ್ತರ ಆಯ್ಕೆಮಾಡಿ", question[1], key=f"proverb_{PROVERBS.index(question)}")
    if st.button("ಉತ್ತರ ಪರಿಶೀಲಿಸಿ", key="check_proverb"):
        st.session_state.proverb_checked = True
        if answer == question[2]:
            st.session_state.points += 10
            st.success("🎉 ಸರಿಯಾದ ಉತ್ತರ! 10 ಅಂಕಗಳು.")
        else:
            st.error(f"ಸರಿಯಾದ ಉತ್ತರ: {question[2]}")
    if st.session_state.proverb_checked and st.button("ಮುಂದಿನ ಗಾದೆ ➡️", key="next_proverb"):
        st.session_state.proverb_question = random.choice(PROVERBS)
        st.session_state.proverb_checked = False
        st.rerun()

elif page == "🧩 Match the Following":
    st.subheader("🧩 Match the Following — ಜೋಡಿಗಳನ್ನು ಹೊಂದಿಸಿ")
    match_category = st.selectbox("ಆಟದ ವಿಭಾಗ", list(MATCHES.keys()))
    pairs = MATCHES[match_category]
    emojis = list(pairs.keys())
    if st.session_state.match_pairs is None or st.session_state.get("active_match_category") != match_category:
        shuffled = emojis.copy()
        random.shuffle(shuffled)
        st.session_state.match_pairs = shuffled
        st.session_state.active_match_category = match_category
        st.session_state.match_round = 0
    st.write("ಎಡಭಾಗದ ಚಿತ್ರ/ಚಿಹ್ನೆಗೆ ಬಲಭಾಗದ ಸರಿಯಾದ ಹೆಸರನ್ನು ಆಯ್ಕೆಮಾಡಿ.")
    correct = 0
    for i, emoji in enumerate(emojis):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown(f'<div class="lesson-card"><h2 style="text-align:center">{emoji}</h2></div>', unsafe_allow_html=True)
        with col2:
            selected_name = st.selectbox(
                f"ಜೋಡಿ {i+1}",
                ["ಆಯ್ಕೆಮಾಡಿ..."] + [pairs[e] for e in st.session_state.match_pairs],
                key=f"match_{match_category}_{i}",
            )
            if selected_name == pairs[emoji]:
                correct += 1
    if st.button("ಜೋಡಿಗಳನ್ನು ಪರಿಶೀಲಿಸಿ", key="check_match"):
        if correct == len(emojis):
            st.session_state.points += 10
            st.session_state.match_round += 1
            st.balloons()
            st.success(f"ಎಲ್ಲಾ ಜೋಡಿಗಳು ಸರಿಯಾಗಿವೆ! +10 ಅಂಕಗಳು. ({correct}/{len(emojis)})")
        else:
            st.warning(f"{correct}/{len(emojis)} ಜೋಡಿಗಳು ಸರಿಯಾಗಿವೆ. ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ.")
    if st.button("ಹೊಸ ಆಟ / ಮರುಹೊಂದಿಸಿ", key="reset_match"):
        st.session_state.match_pairs = None
        st.rerun()

elif page == "🔀 Jumbled Words":
    st.subheader("🔀 Jumbled Words — ಅಕ್ಷರಗಳನ್ನು ಜೋಡಿಸಿ")
    all_words = sum(WORD_BANK.values(), [])
    if st.session_state.jumbled_word is None:
        st.session_state.jumbled_word = random.choice(all_words)
    word = st.session_state.jumbled_word
    letters = list(word)
    random.shuffle(letters)
    st.write("ಕೆಳಗಿನ ಅಕ್ಷರಗಳನ್ನು ಸರಿಯಾದ ಕ್ರಮದಲ್ಲಿ ಜೋಡಿಸಿ ಪದ ರಚಿಸಿ.")
    st.markdown(f'<div class="kannada-big">{"　".join(letters)}</div>', unsafe_allow_html=True)
    guess = st.text_input("ಸರಿಯಾದ ಪದವನ್ನು ಇಲ್ಲಿ ಬರೆಯಿರಿ", key=f"jumbled_guess_{word}")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("ಉತ್ತರ ಪರಿಶೀಲಿಸಿ", key="check_jumbled"):
            if guess.strip() == word:
                st.session_state.points += 10
                st.balloons()
                st.success("🎉 ಸರಿಯಾದ ಪದ! 10 ಅಂಕಗಳು.")
            else:
                st.error("ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ. ಸುಳಿವು: ಪದವನ್ನು ನಿಧಾನವಾಗಿ ಓದಿ.")
    with c2:
        if st.button("ಹೊಸ ಪದ", key="new_jumbled"):
            st.session_state.jumbled_word = random.choice(all_words)
            st.rerun()

elif page == "🖼️ ಚಿತ್ರ ಮತ್ತು ಪದ":
    st.subheader("🖼️ ಚಿತ್ರ ಮತ್ತು ಕನ್ನಡ ಪದ")
    picture_words = [
        ("🍎", "ಸೇಬು"), ("🥭", "ಮಾವು"), ("🍌", "ಬಾಳೆಹಣ್ಣು"),
        ("🐘", "ಆನೆ"), ("🐄", "ಹಸು"), ("🐈", "ಬೆಕ್ಕು"),
        ("🌞", "ಸೂರ್ಯ"), ("🌙", "ಚಂದ್ರ"), ("🌳", "ಮರ"),
        ("🌹", "ಗುಲಾಬಿ"), ("📚", "ಪುಸ್ತಕ"), ("🏠", "ಮನೆ"),
    ]
    cols = st.columns(3)
    for i, (emoji, word) in enumerate(picture_words):
        with cols[i % 3]:
            st.markdown(
                f'<div class="lesson-card" style="text-align:center"><div style="font-size:3rem">{emoji}</div><h3>{word}</h3></div>',
                unsafe_allow_html=True,
            )
            st.write("")
    st.caption("ಇವು ಕಲಿಕೆಯ ಮಾದರಿ ಚಿತ್ರ-ಚಿಹ್ನೆಗಳು. ಮುಂದಿನ ಹಂತದಲ್ಲಿ ನೈಜ ಚಿತ್ರಗಳು ಮತ್ತು ಧ್ವನಿ ಸೇರಿಸಬಹುದು.")

elif page == "🌍 ಸಾಮಾನ್ಯ ಜ್ಞಾನ (GK)":
    st.subheader("🌍 ಸಾಮಾನ್ಯ ಜ್ಞಾನ — ಕನ್ನಡ Quiz")
    if st.session_state.gk_question is None:
        st.session_state.gk_question = random.choice(GK)
        st.session_state.gk_checked = False
    q = st.session_state.gk_question
    st.markdown(f"### {q[0]}")
    selected = st.radio("ನಿಮ್ಮ ಉತ್ತರ", q[1], key=f"gk_{GK.index(q)}")
    if st.button("ಉತ್ತರ ಪರಿಶೀಲಿಸಿ", key="check_gk"):
        st.session_state.gk_checked = True
        if selected == q[2]:
            st.session_state.points += 10
            st.success("🎉 ಸರಿಯಾದ ಉತ್ತರ! 10 ಅಂಕಗಳು.")
        else:
            st.error(f"ಸರಿಯಾದ ಉತ್ತರ: {q[2]}")
    if st.session_state.gk_checked and st.button("ಮುಂದಿನ ಪ್ರಶ್ನೆ ➡️", key="next_gk"):
        st.session_state.gk_question = random.choice(GK)
        st.session_state.gk_checked = False
        st.rerun()
    st.caption("ಈ ಮಾದರಿ GK ಬ್ಯಾಂಕ್‌ನಲ್ಲಿ ಆರಂಭಿಕ ಪ್ರಶ್ನೆಗಳಿವೆ. ನಂತರ ಹೆಚ್ಚಿನ ಪರಿಶೀಲಿತ ಪ್ರಶ್ನೆಗಳನ್ನು ಸೇರಿಸಬಹುದು.")

elif page == "📈 ನನ್ನ ಪ್ರಗತಿ":
    st.subheader("📈 ನನ್ನ ಕಲಿಕೆಯ ಪ್ರಗತಿ")
    c1, c2, c3 = st.columns(3)
    c1.metric("⭐ ಒಟ್ಟು ಅಂಕಗಳು", st.session_state.points)
    c2.metric("✅ ಪೂರ್ಣಗೊಳಿಸಿದ ಪಾಠಗಳು", st.session_state.completed)
    c3.metric("🏅 ಮಟ್ಟ", "ಆರಂಭಿಕ" if st.session_state.points < 50 else ("ಮಧ್ಯಮ" if st.session_state.points < 150 else "ಮುಂದುವರಿದ"))
    st.progress(min(st.session_state.points / 200, 1.0), text="ಮುಂದಿನ ಗುರಿ: 200 ಅಂಕಗಳು")
    st.write("ನಿಯಮಿತವಾಗಿ ಅಭ್ಯಾಸ ಮಾಡಿ, ಆಟಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸಿ, ಹೊಸ ಅಂಕಗಳನ್ನು ಗಳಿಸಿ.")
    if st.button("ಪ್ರಗತಿಯನ್ನು ಮರುಹೊಂದಿಸಿ"):
        for key, value in defaults.items():
            st.session_state[key] = value
        st.rerun()

# ---------- Footer ----------
st.divider()
st.markdown(
    '<div style="text-align:center;color:#47748e;padding:8px">'
    '<b>With You Kannada</b> · GFGCW · Footer: BCA<br>'
    'ಕನ್ನಡ ಕಲಿಕೆ ಎಲ್ಲರಿಗೂ ಸುಲಭವಾಗಲಿ! 💙'
    '</div>',
    unsafe_allow_html=True,
)
