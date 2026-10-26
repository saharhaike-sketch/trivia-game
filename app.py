# מבצע הגות צבאית – משחק למידה (Streamlit)
# הקובץ game.html חייב לשבת באותה תיקייה כמו app.py
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="מבצע הגות צבאית – משחק למידה",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# מסתיר את המסגרת של Streamlit כדי שהמשחק ימלא את כל המסך
st.markdown(
    """
    <style>
      header, footer, #MainMenu {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      .stApp {background: #070d18;}
      iframe {border: none;}
    </style>
    """,
    unsafe_allow_html=True,
)

GAME_FILE = Path(__file__).parent / "game.html"


@st.cache_data
def load_game() -> str:
    return GAME_FILE.read_text(encoding="utf-8")


if hasattr(st, "iframe"):  # גרסאות חדשות של Streamlit
    st.iframe(load_game(), height=1600)
else:  # גרסאות ישנות
    import streamlit.components.v1 as components
    components.html(load_game(), height=1600, scrolling=True)
