# --- עיצוב האולפן, סרגל הצד והתאמה לטלפון הנייד ---
def set_studio_design():
    st.markdown(
        """
        <style>
        /* יישור לימין רק לטקסטים כדי לא לשבור את המסך בטלפון */
        p, h1, h2, h3, h4, span, button, .stMarkdown {
            direction: rtl !important;
            text-align: right !important;
            unicode-bidi: isolate;
        }
        
        /* תיקון הכתב האנכי בסרגל הצד בטלפון */
        [data-testid="stSidebar"] div {
            direction: rtl !important;
            text-align: right !important;
            white-space: nowrap !important; /* מונע את שבירת האותיות כלפי מטה */
        }
        
        /* התאמת התיבה המרכזית למסכים קטנים (מובייל) */
        .block-container {
            max-width: 100% !important;
            padding: 1.5rem 1rem !important;
            margin-top: 1rem;
            background-color: rgba(0, 0, 0, 0.7);
            border-radius: 15px;
            border: 2px solid #ce9b2c;
            box-shadow: 0 0 15px rgba(206, 155, 44, 0.3);
        }
        
        /* צבעי רקע וטקסט */
        .stApp { background: radial-gradient(circle at 50% 50%, #1e3c72 0%, #030a1c 60%, #000000 100%); }
        [data-testid="stSidebar"] { background: linear-gradient(180deg, #030a1c 0%, #000000 100%) !important; border-left: 2px solid #ce9b2c; }
        [data-testid="stSidebar"] * { color: #ffffff !important; }
        h1, h2, h3, h4, p, span, .stMarkdown { color: white !important; }

        /* כפתורים מותאמים לטלפון - מאפשרים לשאלה ארוכה לרדת שורה בתוך הכפתור */
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
