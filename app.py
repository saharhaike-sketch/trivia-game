import random
import streamlit as st
import time

st.set_page_config(page_title="מי רוצה להיות מיליונר", page_icon="💰", layout="wide")

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
        "question": "מה ההבדל המרכזי בין מדד RPO למדד RTO בניהול המשכיות עסקית?",
        "options": [
            "RPO מתייחס לכמות המידע שמותר לאבד (מסתכל אחורה), ו-RTO לזמן המוקצב לשחזור המערכת (מסתכל קדימה).",
            "RPO מודד את זמן חזרת העובדים, ו-RTO מודד את כמות המחשבים שניזוקו.",
            "RPO הוא מדד כלכלי בלבד, בעוד RTO הוא מדד תפעולי של שירות לקוחות.",
            "אין הבדל, שניהם מודדים את זמן ההשבתה המקסימלי (MTD)."
        ],
        "answer": 0,
        "hint": "אחד מסתכל אחורה על אובדן מידע, והשני קדימה על התאוששות למערכת פעילה.",
        "explanation": "RPO (Recovery Point Objective) היא כמות המידע המקסימלית שמותר לאבד. לעומת זאת, RTO (Recovery Time Objective) הוא הזמן המוקצב
