import random
import streamlit as st
import time

st.set_page_config(page_title="מי רוצה להיות מיליונר - יסודות הניהול", page_icon="💼", layout="wide")

# --- עיצוב האולפן והתאמה לנייד ---
def set_studio_design():
    st.markdown(
        """
        <style>
        p, h1, h2, h3, h4, span, button, .stMarkdown {
            direction: rtl !important;
            text-align: right !important;
            unicode-bidi: isolate;
        }
        [data-testid="stSidebar"] div {
            direction: rtl !important;
            text-align: right !important;
            white-space: nowrap !important; 
        }
        .block-container {
            max-width: 100% !important;
            padding: 1.5rem 1rem !important;
            margin-top: 1rem;
            background-color: rgba(0, 0, 0, 0.75);
            border-radius: 15px;
            border: 2px solid #ce9b2c;
            box-shadow: 0 0 15px rgba(206, 155, 44, 0.3);
        }
        .stApp { background: radial-gradient(circle at 50% 50%, #1e3c72 0%, #030a1c 60%, #000000 100%); }
        [data-testid="stSidebar"] { background: linear-gradient(180deg, #030a1c 0%, #000000 100%) !important; border-left: 2px solid #ce9b2c; }
        [data-testid="stSidebar"] * { color: #ffffff !important; }
        h1, h2, h3, h4, p, span, .stMarkdown, li { color: white !important; }
        
        .stButton>button {
            background-color: #00004d;
            color: white !important;
            border: 2px solid #ce9b2c;
            border-radius: 12px;
            font-size: 16px;
            font-weight: bold;
            padding: 10px;
            width: 100%;
            height: auto;
            min-height: 50px;
            white-space: normal !important; 
            transition: all 0.3s ease;
        }
        .stButton>button:hover { background-color: #ce9b2c; color: black !important; border-color: white; }
        header {visibility: hidden;}
        
        .correct-answer { color: #4CAF50; font-weight: bold; }
        .wrong-answer { color: #f44336; font-weight: bold; }
        </style>
        """,
        unsafe_allow_html=True
    )

set_studio_design()

PRIZE_LADDER = [
    100, 200, 300, 500, 1000, 2000, 4000, 8000,
    16000, 32000, 64000, 125000, 250000, 500000, 1000000,
]

ALL_QUESTIONS = [
    {
        "question": "על פי ד\"ר טאוב אליאב, מה קורה לבעל סמכות שאינו אוכף ציות?",
        "options": [
            "הוא גוזר על עצמו לבצע משימות בעצמו או לעמוד מול כישלונות שייוצרו על ידי עובדיו.",
            "האחריות עוברת באופן אוטומטי לעובדים הזוטרים.",
            "הסמכות שלו מתבטלת על פי נהלי הארגון.",
            "הוא הופך למנהל 'משתף' ומתפקד בצורה דמוקרטית יותר."
        ],
        "answer": 0,
        "hint": "סמכות מלווה באחריות. למי באים בטענות בסוף?",
        "explanation": "סמכות מלווה באחריות. בעל סמכות שאינו אוכף ציות ייאלץ לבצע את המשימות לבד או לשאת בתוצאות של כישלונות העובדים, כי בסוף האחריות עליו."
    },
    {
        "question": "מהו ההבדל המרכזי בין 'האצלת סמכות' ל'ביזור סמכות'?",
        "options": [
            "בהאצלה האחריות נשארת אצל בעל הסמכות, בביזור גם הסמכות וגם האחריות עוברות לבעל תפקיד אחר.",
            "בהאצלה המשימה מועברת לעובד לא מיומן, בביזור היא מועברת לעובד מיומן.",
            "בהאצלה העברת הסמכות היא קבועה, בביזור היא רק לטווח קצר.",
            "אין הבדל ממשי, שתי השיטות נועדו לשתף עובדים בקבלת החלטות."
        ],
        "answer": 0,
        "hint
