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
        "explanation": "RPO (Recovery Point Objective) היא כמות המידע המקסימלית שמותר לאבד. לעומת זאת, RTO (Recovery Time Objective) הוא הזמן המוקצב לשחזור המערכת עצמה והחזרתה לאוויר."
    },
    {
        "question": "כיצד מחושב מדד ה-MTD (זמן השבתה מקסימלי נסבל)?",
        "options": [
            "MTD = RTO + WRT",
            "MTD = RPO + RTO",
            "MTD = RTO - WRT",
            "MTD = BIA + BCP"
        ],
        "answer": 0,
        "hint": "חיבור של זמן שחזור המערכת יחד עם זמן שחזור העבודה.",
        "explanation": "MTD (Maximum Tolerable Downtime) מחושב כחיבור של RTO (זמן חזרת המערכת) ו-WRT (זמן השלמת העבודה שהצטברה). הוא מייצג את זמן ההשבתה המקסימלי לפני שייגרם נזק בלתי הפיך."
    },
    {
        "question": "מהו ההבדל העיקרי בין סיכון מסוג 'קרנף אפור' ל'ברבור שחור'?",
        "options": [
            "קרנף אפור הוא סכנה ברורה שמתעלמים ממנה, בעוד ברבור שחור הוא אירוע בלתי סביר שמגיע משום מקום.",
            "קרנף אפור הוא סכנה פיננסית בלבד, וברבור שחור הוא סכנה לוגיסטית.",
            "ברבור שחור קורה לעיתים קרובות, בעוד קרנף אפור קורה פעם במאה שנה.",
            "אין הבדל, שניהם מונחים נרדפים לאותו סוג של משבר פתאומי."
        ],
        "answer": 0,
        "hint": "תחשוב על משבר שראינו מגיע מזמן (כמו הקורונה) לעומת הפתעה מוחלטת.",
        "explanation": "סיכון קרנף אפור מוגדר כסכנה ברורה, גלויה ובעלת השפעה גבוהה שמסתערת לעברנו ובכל זאת מתעלמים ממנה. ברבור שחור הוא אירוע בלתי סביר לחלוטין שמגיע בהפתעה גמורה."
    },
    {
        "question": "לפי מטריצת הערכת הסיכונים המותאמת ל'קרנף אפור', כיצד משתנה שקלול הסיכונים?",
        "options": [
            "ההשפעה (Impact) מקבלת משקל גבוה שעולה בקפיצות של 5, ואילו הסבירות עולה רק ברבעים קטנים.",
            "הסבירות הופכת להיות המדד היחיד שקובע את רמת הסיכון של הארגון.",
            "מבטלים לחלוטין את מדד ההשפעה (Impact) ומתמקדים רק בזמן ההתאוששות.",
            "ההשפעה והסבירות מקבלות בדיוק את אותו המשקל, בסולם של 1 עד 5."
        ],
        "answer": 0,
        "hint": "המטרה היא למנוע מסיכון הרסני לרדת לתחתית רק בגלל סבירות נמוכה.",
        "explanation": "בשיטה החדשה, מדד ההשפעה מקבל משקל גבוה (20, 15, 10, 5, 1) בעוד מכפיל הסבירות עולה רק ברבעים (1, 1.25, 1.5). כך מבטיחים שסיכון קטסטרופלי לא יידחק לשוליים."
    },
    {
        "question": "מה מוכיח 'ניסוי הגורילה' בהקשר של ניהול סיכונים (עיוורון קשבי)?",
        "options": [
            "כשאנחנו מרוכזים במה שאנחנו מצפים לראות, אנחנו מפספסים דברים בולטים שמופיעים ממש מול העיניים.",
            "אנשים מפחדים מגורילות יותר מאשר מסכנות עסקיות יומיומיות.",
            "רק מומחים להערכת סיכונים יכולים לזהות סכנות חבויות.",
            "עובדים בארגון תמיד יבחינו בסכנה אם יגידו להם מראש לחפש אותה."
        ],
        "answer": 0,
        "hint": "תחשוב על מה שקורה כשאתה מרוכז רק בספירת מסירות כדורסל.",
        "explanation": "עיוורון קשבי (Inattentional Blindness) אומר שמומחים שמכוונים לחפש דפוסים המוכרים להם, עלולים לא להבחין ב'קרנף אפור' שעומד ממש מולם, פשוט כי לא ציפו לו."
    },
    {
        "question": "מהו ההבדל המרכזי בין BIA (ניתוח השפעות עסקיות) להערכת סיכונים?",
        "options": [
            "BIA מתחיל מהתהליך העסקי ושואל 'בלי מה אי אפשר לשרוד?', בעוד הערכת סיכונים שואלת 'מה עלול להשתבש?'.",
            "BIA מבוצע רק לאחר שהמשבר נגמר, והערכת סיכונים מבוצעת לפניו.",
            "BIA בוחן אך ורק תהליכי ייצור כבדים, והערכת סיכונים בוחנת כוח אדם.",
            "אין הבדל, מדובר בשני שמות שונים לאותו שלב ניהולי בדיוק."
        ],
        "answer": 0,
        "hint": "האחד מתמקד ב'שורות התחתונות' של העסק, והשני מתמקד באיומים ומניעה.",
        "explanation": "הערכת סיכונים מתמקדת באיומים ובחולשות. ה-BIA מתחיל מהתהליך העסקי ומתמקד בהשלכות הפגיעה בו ובסדר העדיפויות לשחזור, ללא קשר לסיבה שגרמה לאסון."
    },
    {
        "question": "אילו ארבעה סוגי השפעה נהוג לבחון ולכמת במסגרת ניתוח ה-BIA?",
        "options": [
            "פיננסית, תפעולית/שירותית, תדמיתית ורגולטורית/חוקית.",
            "לוגיסטית, חשבונאית, גיאוגרפית וטכנולוגית.",
            "סייבר, אסונות טבע, מגיפות ומלחמות.",
            "פנימית, חיצונית, אקולוגית ואסתטית."
        ],
        "answer": 0,
        "hint": "ההשפעות בוחנות פגיעה בכסף, בשירות, במוניטין ובעמידה בחוק.",
        "explanation": "בשלב איסוף הנתונים ל-BIA בוחנים 4 קטגוריות של השפעה: פיננסית (אובדן הכנסות), תפעולית (פגיעה באספקה), תדמיתית (נזק למוניטין) ומשפטית/רגולטורית."
    },
    {
        "question": "מה המשמעות של 'נקודת כשל בודדת' (SPOF) בבניית תוכנית התאוששות?",
        "options": [
            "תהליכים, מערכות או אנשים ייחודיים שבלעדיהם כל הפעילות העסקית נעצרת לחלוטין.",
            "נקודה גיאוגרפית אחת שבה מרוכזים כל משרדי הממשלה.",
            "תקלה נקודתית במחשב בודד שניתן לתקן על ידי טכנאי זוטר.",
            "רגע מדויק בציר הזמן שבו המערכת חוזרת לעבוד בשגרה מלאה."
        ],
        "answer": 0,
        "hint": "מצב שבו יש 'צוואר בקבוק' קריטי אחד בארגון, שאם הוא נופל - הכל קורס.",
        "explanation": "SPOF מתאר רכיב מרכזי במערכת, אדם בעל מיומנות קריטית או תהליך ליבה, שאם יפגעו ואין להם אלטרנטיבה או גיבוי מיידי, תופסק כלל הפעילות של הארגון."
    },
    {
        "question": "במודל 4 עמודי התווך של התאוששות (מבנים, כ\"א, טכנולוגיה, אספקה), איזו טענה נכונה?",
        "options": [
            "הם תלויים זה בזה — חולשה באחד (כמו צוות ללא טכנולוגיה) מבטלת את החוזק של האחרים.",
            "כל עמוד פועל בנפרד, ואפשר לשקם מבנה גם אם אין שום טכנולוגיה או כוח אדם.",
            "טכנולוגיה היא העמוד החשוב מכולם ואין צורך בשאר העמודים אם יש גיבוי בענן.",
            "שרשרת האספקה רלוונטית רק למפעלים תעשייתיים ולא לחברות שירות."
        ],
        "answer": 0,
        "hint": "תחשבו על שרשרת שחוזקה נמדד אך ורק לפי החוליה החלשה ביותר שבה.",
        "explanation": "ארבעת עמודי התווך אינם עצמאיים. קיימת שרשרת תלות ביניהם, ולכן אסטרטגיה טובה ככל שתהיה לא תעזור אם חסר אחד המרכיבים הקריטיים לתפעולה."
    },
    {
        "question": "תהליך הייצור חזר לעבודה תוך 72 שעות (במקום 48 ב-RTO). הנתונים שוחזרו תוך שעתיים (במקום 4 ב-RPO). מה המסקנה?",
        "options": [
            "הארגון עמד ביעד ה-RPO שהגדיר לעצמו, אך נכשל ועבר את יעד ה-RTO.",
            "הארגון עמד ביעד ה-RTO, אך נכשל ביעד ה-RPO.",
            "יעד ה-RTO היה ריאלי ומדויק, אך העובדים פשוט לא רצו לחזור לעבודה.",
            "הארגון הצליח במלוא תוכנית ההמשכיות העסקית שלו ללא שום חריגות."
        ],
        "answer": 0,
        "hint": "תבדקו איזה מדד לקח פחות זמן מהמתוכנן (הצלחה) ואיזה חרג מהזמן המותר (כישלון).",
        "explanation": "מכיוון שהנתונים שוחזרו מהר מהמותר, יעד ה-RPO הושג בהצלחה. לעומת זאת, החזרה לעבודה לקחה יותר זמן מהמקסימום המותר, ולכן הארגון לא עמד ביעד ה-RTO."
    },
    {
        "question": "מהי אסטרטגיית 'אתר חם' (Hot Site) כמענה ליעד התאוששות (RTO) קצר?",
        "options": [
            "אתר משני פעיל לחלוטין המקבל נתונים מסונכרנים, ומאפשר מעבר מיידי (Failover).",
            "שטח פיזי ריק שמכיל רק חיבורי חשמל, ויש להביא אליו ציוד במקרה חירום.",
            "הסכם מול חברה קבלנית לבניית משרדים חדשים במהירות לאחר שריפה.",
            "גיבוי שנשמר על קלטות פיזיות בכספת לאחזור ארוך טווח."
        ],
        "answer": 0,
        "hint": "אתר שבו הכל מוכן, פעיל וחם, ורק מחכה שיעבירו אליו את הפעילות.",
        "explanation": "אתר חם (Hot Site / Active-Active) היא אסטרטגיה המשקפת נתונים באופן סינכרוני ומאפשרת מעבר אוטומטי. זהו פתרון יקר המתאים למערכות קריטיות (Mission-Critical)."
    },
    {
        "question": "לפי מחקר השדה של יוסף לניר על הקיבוץ, מה מאפיין את המשבר התעסוקתי במערכת המשקית?",
        "options": [
            "אבטלה סמויה, תלות גוברת בעבודה שכירה, ופיגור בפיתוח ההון האנושי המקומי.",
            "גידול עצום במגזר החקלאות שגורם למחסור בידיים עובדות בחממות.",
            "הפרטה מלאה של כל ענפי התעשייה וחוסר רצון של חברים להיות שכירים.",
            "עודף גדול בכוח אדם צעיר שמוכן לעבוד אך ורק במגזר הפיננסי."
        ],
        "answer": 0,
        "hint": "מערכת שהצליחה בעבר, אך מתקשה להסתגל כיום ולהכשיר כוח אדם פנימי למציאות החדשה.",
        "explanation": "הגורמים הפנימיים למשבר בקיבוץ, לפי לניר, כוללים התערערות המבנה התעסוקתי, פיגור בהכשרת הון אנושי, אבטלה סמויה מופנמת ותלות בעבודה שכירה הבולמת טכנולוגיות חדשות."
    },
    {
        "question": "איזה תהליך עולמי מרכזי משפיע בצורה ישירה על 'משבר התעסוקה בקיבוץ' (לפי לניר)?",
        "options": [
            "המעבר מאוטומציה של מיכון לאוטומציה של מחשוב ושירותים, הדורשים מיומנויות חדשות.",
            "הגידול המשמעותי בסובסידיות שממשלות מעניקות לחקלאות הקונבנציונלית.",
            "הירידה בתוחלת החיים בארצות המפותחות.",
            "מעבר רוב התעשייה לאנרגיה סולארית בלבד."
        ],
        "answer": 0,
        "hint": "המעבר מתעשייה מסורתית וכבדה לתעשייה עתירת ידע (הייטק ושירותים).",
        "explanation": "המהפכה התעסוקתית העולמית מתאפיינת בעלייה של שירותי תקשורת, מחשוב ובקרה. הקיבוץ שהצליח בעידן המיכון הישן נאלץ כעת לעשות אדפטציה מהירה לכלכלת המחשוב והשירותים."
    },
    {
        "question": "מהי תיאוריית 'האיש העשירי' (The Tenth Man) בניהול משברים?",
        "options": [
            "אסטרטגיה לפיה אם 9 אנשים מסכימים על כיוון, חובתו של העשירי לחלוק ולהציג חלופה נגדית.",
            "חוק שלפיו כל צוות ניהול משברים חייב לכלול בדיוק עשרה חברים.",
            "בחירת עובד אקראי (העשירי שנכנס לחדר) כדי שינהל את צוות ההמשכיות.",
            "הנחה שרק עשירית מהסיכונים שהוערכו ב-BIA מתממשים בפועל."
        ],
        "answer": 0,
        "hint": "תפקידו להיות 'איפכא מסתברא' כדי לאתגר את קונצנזוס הרוב ולהימנע מעיוורון.",
        "explanation": "האיש העשירי היא אסטרטגיה שלפיה אדם אחד חייב לצאת נגד הקונצנזוס ולהציג תרחישים לא סבירים, במטרה לזהות סיכוני 'ברבור שחור' או תרחישים הרסניים שהרוב התעלם מהם."
    },
    {
        "question": "מהו 'סיכון סיסטמטי' (Systematic Risk), בדומה לזה שגרם למשבר הכלכלי של 2008?",
        "options": [
            "מצב שבו תקלה או כשל בודד משפיעים על כלל המערכת בשל הקשרים והתלות ההדדית בתוכה.",
            "סיכון אופרטיבי שמתרחש באופן עקבי ושיטתי כל יום באותה שעה בארגון.",
            "סיכון המשפיע אך ורק על מערכות ההפעלה של מחשבי הנהלת החשבונות.",
            "מצב של אובדן נתונים נקודתי שלא משפיע על אף מערכת אחרת וניתן לתיקון."
        ],
        "answer": 0,
        "hint": "כמו מגדל קוביות: משיכה של קובייה מרכזית מפילה את המגדל כולו כבתגובת שרשרת.",
        "explanation": "סיכון סיסטמטי מתאר מצב שבו המערכת כולה בסכנת התמוטטות בגלל המורכבות והתלות ההדדית של חלקיה (לדוגמה, קריסה של שוק המשכנתאות שהובילה לקריסה כמעגל דומינו של כל המערכת הפיננסית)."
    }
]

if "game_state" not in st.session_state:
    st.session_state.game_state = "start"
    st.session_state.selected_questions = []
    st.session_state.current_question = 0
    st.session_state.current_q_idx = -1
    st.session_state.lifelines = {"5050": True, "audience": True, "phone": True}
    st.session_state.hidden_options = []
    st.session_state.hint_message = ""
    st.session_state.show_explanation = False
    st.session_state.is_correct = False
    st.session_state.history = []
    st.session_state.start_time = None
    st.session_state.end_time = None

def reset_game():
    st.session_state.game_state = "playing"
    st.session_state.selected_questions = random.sample(ALL_QUESTIONS, 15)
    st.session_state.current_question = 0
    st.session_state.current_q_idx = -1
    st.session_state.lifelines = {"5050": True, "audience": True, "phone": True}
    st.session_state.hidden_options = []
    st.session_state.hint_message = ""
    st.session_state.show_explanation = False
    st.session_state.is_correct = False
    st.session_state.history = []
    st.session_state.start_time = time.time()
    st.session_state.end_time = None

col_title, col_icon = st.columns([8, 1])
with col_title:
    st.title("💰 מי רוצה להיות מיליונר? 💰")
st.markdown("---")

if st.session_state.game_state == "start":
    st.subheader("ברוכים הבאים לאתגר הזמנים (ניהול המשכיות עסקית)!")
    st.write("ענו נכון על 15 שאלות מהר ככל האפשר. הטיימר מתחיל לרוץ מיד עם הלחיצה!")
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("התחל במשחק והפעל שעון", type="primary", use_container_width=True):
        reset_game()
        st.rerun()

elif st.session_state.game_state == "playing":
    q_idx = st.session_state.current_question
    current_q = st.session_state.selected_questions[q_idx]

    # ערבוב תשובות כשהשאלה מתחלפת בלבד
    if "shuffled_options" not in st.session_state or st.session_state.get("current_q_idx") != q_idx:
        opts_with_idx = list(enumerate(current_q["options"]))
        random.shuffle(opts_with_idx)
        st.session_state.shuffled_options = [opt for i, opt in opts_with_idx]
        st.session_state.correct_idx = next(i for i, (orig_i, opt) in enumerate(opts_with_idx) if orig_i == current_q["answer"])
        st.session_state.current_q_idx = q_idx

    correct_answer_idx = st.session_state.correct_idx
    options_list = st.session_state.shuffled_options
    current_prize = PRIZE_LADDER[q_idx - 1] if q_idx > 0 else 0

    if st.session_state.show_explanation:
        st.markdown(f"### שאלה {q_idx + 1}: {current_q['question']}")
        
        if st.session_state.is_correct:
            st.balloons()  
            st.success("🎉 תשובה נכונה!")
        else:
            st.error("❌ טעות בתשובה!")
            st.warning(f"התשובה הנכונה היא: **{options_list[correct_answer_idx]}**")
        
        st.info(f"💡 **הסבר לחומר:** {current_q['explanation']}")
        
        btn_text = "המשך לשאלה הבאה" if st.session_state.is_correct and q_idx < 14 else "לצפייה בתוצאת הזמן והסיכום"
        if st.button(btn_text, type="primary", use_container_width=True):
            st.session_state.show_explanation = False
            if not st.session_state.is_correct:
                st.session_state.game_state = "lost"
            elif q_idx + 1 >= 15:
                st.session_state.game_state = "won"
            else:
                st.session_state.current_question += 1
                st.session_state.hidden_options = []
                st.session_state.hint_message = ""
            st.rerun()

    else:
        col_l1, col_l2, col_l3, col_info = st.columns([1.2, 1.2, 1.2, 2.5])
        
        with col_l1:
            if st.session_state.lifelines["5050"]:
                if st.button("✂️ 50:50", use_container_width=True):
                    wrong_indices = [i for i in range(4) if i != correct_answer_idx]
                    st.session_state.hidden_options = random.sample(wrong_indices, 2)
                    st.session_state.lifelines["5050"] = False
                    st.rerun()
            else:
                st.button("✂️ 50:50 (נוצל)", disabled=True, use_container_width=True)

        with col_l2:
            if st.session_state.lifelines["audience"]:
                if st.button("👥 עזרת קהל", use_container_width=True):
                    letters = ["א", "ב", "ג", "ד"]
                    st.session_state.hint_message = f"רוב מוחץ בקהל (74%) מהמר על אפשרות {letters[correct_answer_idx]}."
                    st.session_state.lifelines["audience"] = False
                    st.rerun()
            else:
                st.button("👥 קהל (נוצל)", disabled=True, use_container_width=True)

        with col_l3:
            if st.session_state.lifelines["phone"]:
                if st.button("📞 חבר טלפוני", use_container_width=True):
                    st.session_state.hint_message = f"**רמז מהחבר הטלפוני:** '{current_q['hint']}'"
                    st.session_state.lifelines["phone"] = False
                    st.rerun()
            else:
                st.button("📞 טלפוני (נוצל)", disabled=True, use_container_width=True)

        with col_info:
            st.markdown(f"<h4 style='margin:0;'>שאלה {q_idx + 1} מתוך 15</h4><span>סכום מובטח: <b>{current_prize:,} ₪</b></span>", unsafe_allow_html=True)

        if st.session_state.hint_message:
            st.info(st.session_state.hint_message)

        st.markdown("---")
        st.subheader(f"{current_q['question']}")
        st.markdown("<br>", unsafe_allow_html=True)

        letters = ["א. ", "ב. ", "ג. ", "ד. "]
        
        row1_col_left, row1_col_right = st.columns(2)
        
        with row1_col_right: 
            if 0 in st.session_state.hidden_options:
                st.button(f"{letters[0]} (הוסתר)", disabled=True, key="opt_0", use_container_width=True)
            else:
                if st.button(f"{letters[0]} {options_list[0]}", key="opt_0", use_container_width=True):
                    st.session_state.is_correct = (0 == correct_answer_idx)
                    if not st.session_state.is_correct or q_idx == 14:
                        st.session_state.end_time = time.time()
                    st.session_state.history.append({
                        "question": current_q['question'],
                        "user_ans": options_list[0],
                        "correct_ans": options_list[correct_answer_idx],
                        "explanation": current_q['explanation'],
                        "is_correct": st.session_state.is_correct
                    })
                    st.session_state.show_explanation = True
                    st.rerun()
                    
        with row1_col_left: 
            if 1 in st.session_state.hidden_options:
                st.button(f"{letters[1]} (הוסתר)", disabled=True, key="opt_1", use_container_width=True)
            else:
                if st.button(f"{letters[1]} {options_list[1]}", key="opt_1", use_container_width=True):
                    st.session_state.is_correct = (1 == correct_answer_idx)
                    if not st.session_state.is_correct or q_idx == 14:
                        st.session_state.end_time = time.time()
                    st.session_state.history.append({
                        "question": current_q['question'],
                        "user_ans": options_list[1],
                        "correct_ans": options_list[correct_answer_idx],
                        "explanation": current_q['explanation'],
                        "is_correct": st.session_state.is_correct
                    })
                    st.session_state.show_explanation = True
                    st.rerun()

        row2_col_left, row2_col_right = st.columns(2)
        
        with row2_col_right: 
            if 2 in st.session_state.hidden_options:
                st.button(f"{letters[2]} (הוסתר)", disabled=True, key="opt_2", use_container_width=True)
            else:
                if st.button(f"{letters[2]} {options_list[2]}", key="opt_2", use_container_width=True):
                    st.session_state.is_correct = (2 == correct_answer_idx)
                    if not st.session_state.is_correct or q_idx == 14:
                        st.session_state.end_time = time.time()
                    st.session_state.history.append({
                        "question": current_q['question'],
                        "user_ans": options_list[2],
                        "correct_ans": options_list[correct_answer_idx],
                        "explanation": current_q['explanation'],
                        "is_correct": st.session_state.is_correct
                    })
                    st.session_state.show_explanation = True
                    st.rerun()
                    
        with row2_col_left: 
            if 3 in st.session_state.hidden_options:
                st.button(f"{letters[3]} (הוסתר)", disabled=True, key="opt_3", use_container_width=True)
            else:
                if st.button(f"{letters[3]} {options_list[3]}", key="opt_3", use_container_width=True):
                    st.session_state.is_correct = (3 == correct_answer_idx)
                    if not st.session_state.is_correct or q_idx == 14:
                        st.session_state.end_time = time.time()
                    st.session_state.history.append({
                        "question": current_q['question'],
                        "user_ans": options_list[3],
                        "correct_ans": options_list[correct_answer_idx],
                        "explanation": current_q['explanation'],
                        "is_correct": st.session_state.is_correct
                    })
                    st.session_state.show_explanation = True
                    st.rerun()

    with st.sidebar:
        st.subheader("🏆 סולם הזכיות")
        for idx in range(len(PRIZE_LADDER) - 1, -1, -1):
            prize_text = f"{PRIZE_LADDER[idx]:,} ₪"
            if idx == q_idx:
                st.markdown(f"🔴 **{idx + 1}. {prize_text}** (נוכחית)")
            elif idx < q_idx:
                st.markdown(f"✅ {idx + 1}. {prize_text}")
            else:
                st.markdown(f"⚪ {idx + 1}. {prize_text}")

elif st.session_state.game_state in ["won", "lost"]:
    if st.session_state.game_state == "won":
        st.success("🏆 מדהים! ענית על כל השאלות נכון וזכית במיליון שקלים!")
    else:
        q_idx = st.session_state.current_question
        final_prize = 32000 if q_idx >= 10 else 1000 if q_idx >= 5 else 0
        st.error(f"הפסדת את המשחק, אך סיימת עם סכום זכייה של: **{final_prize:,} ₪**")
    
    if st.session_state.start_time and st.session_state.end_time:
        total_sec = int(st.session_state.end_time - st.session_state.start_time)
        mins = total_sec // 60
        secs = total_sec % 60
        st.warning(f"⏱️ **זמן המשחק שלך: {mins} דקות ו-{secs} שניות!** צלם מסך ושלח לקבוצה כדי להשוויץ בתוצאה.")
    
    if st.button("שחק שוב - משחק חדש", type="primary"):
        reset_game()
        st.rerun()
        
    st.markdown("---")
    st.subheader("📚 סיכום ולמידה - השאלות ששיחקת:")
    
    for idx, item in enumerate(st.session_state.history):
        icon = "✅" if item['is_correct'] else "❌"
        with st.expander(f"שאלה {idx + 1} {icon}"):
            st.markdown(f"**מה הייתה השאלה?** {item['question']}")
            if not item['is_correct']:
                st.markdown(f"**התשובה שסימנת בטעות:** {item['user_ans']}")
            st.markdown(f"**מה התשובה הנכונה?** {item['correct_ans']}")
            st.info(f"**ולמה זו התשובה בעצם?** {item['explanation']}")
