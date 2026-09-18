import random
import streamlit as st

st.set_page_config(page_title="מי רוצה להיות מיליונר", page_icon="💰", layout="wide")

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

PRIZE_LADDER = [
    100, 200, 300, 500, 1000, 2000, 4000, 8000,
    16000, 32000, 64000, 125000, 250000, 500000, 1000000,
]

# מאגר השאלות המלא
ALL_QUESTIONS = [
    {"question": "כיצד מוגדרת 'סמכות' בחומר הנלמד?", "options": ["היכולת לאכוף ציות", "היכולת לתקצב", "אחריות מוחלטת", "העברת אחריות"], "answer": 0, "hint": "תחשוב על פעולה שקשורה לאכיפה ומשמעת של עובדים."},
    {"question": "מה קורה לבעל סמכות שאינו אוכף ציות?", "options": ["הוא גוזר על עצמו לבצע את המשימות בעצמו או לעמוד מול כישלונות", "הוא מקבל בונוס", "האחריות עוברת לעובד", "הוא מפוטר מידית"], "answer": 0, "hint": "מי שלא גורם לאחרים לעשות את העבודה, בסוף יישאר לעשות אותה או יספוג את האשמה."},
    {"question": "מה ההבדל בין האצלת סמכות לביזור סמכות?", "options": ["בהאצלה האחריות נשארת אצל המנהל ולטווח קצר, בביזור היא עוברת באופן קבוע", "ביזור הוא זמני והאצלה היא קבועה", "אין הבדל", "בהאצלה העובד אינו מיומן"], "answer": 0, "hint": "בהאצלה, למרות שנתת סמכות למישהו, אם משהו משתבש - אתה עדיין אשם."},
    {"question": "מתי הכי נכון להשתמש בסגנון ניהול 'מכוון'?", "options": ["כשלעובד אין מיומנות ואין זמן ללמד אותו", "כשיש זמן רב והעובד מיומן", "כשהמיומנות גבוהה", "בבניית תקציב"], "answer": 0, "hint": "תחשוב על מצב חירום: אין זמן להסברים ארוכים והעובד לא יודע מה לעשות, צריך להגיד לו כמו 'תוכי'."},
    {"question": "באיזה סגנון ניהול המעורבות והשליטה נמוכות (למשל: לזרוק את הפח)?", "options": ["מאציל", "מייעץ", "מכוון", "משתף"], "answer": 0, "hint": "מדובר בפעולה שאתה נותן למישהו אחר כי אין לך זמן, והוא מיומן מספיק לעשות אותה לבד."},
    {"question": "בסגנון 'מייעץ' (מיומנות נמוכה אך יש מספיק זמן), כיצד פועל המנהל?", "options": ["שואל שאלות מנחות ומכוונות", "נותן הוראות כמו לתוכי", "מבצע בעצמו", "מקיים הצבעה"], "answer": 0, "hint": "המנהל פועל כמו מדריך – הוא לא נותן את התשובה אלא עוזר לעובד להגיע אליה לבד."},
    {"question": "על פי מודל 'מעגל הזהב' (טבעת הזהב), במה מתמקדים ארגונים מסוג 'Why'?", "options": ["במה הארגון מאמין ולמה הוא מתאים ללקוח", "מהו המוצר בלבד", "איך מייצרים את המוצר", "בתקציב השנתי"], "answer": 0, "hint": "הם פונים לייחודיות של האדם ולא רק מסבירים על התכונות היבשות של המוצר."},
    {"question": "לפי חוק פריצת תודעת הלקוח, איזה אחוז מהלקוחות קונים ראשונים לפי ה-Why?", "options": ["13.5%", "50%", "80%", "5%"], "answer": 0, "hint": "מדובר בשכבה קטנה אך משמעותית שנגררת ראשונה, המספר נע בין 10 ל-15 אחוזים."},
    {"question": "לפי מקס וובר, מהן הבעיות המרכזיות שמבנה ארגוני אמור לפתור?", "options": ["כפילויות בין מחלקות וקונפליקטים", "שחיקת עובדים", "תמחור מוצרים", "גיוס לקוחות חדשים"], "answer": 0, "hint": "כשמשרטטים עץ היררכי מסודר, פתאום מגלים מי עושה עבודה כפולה ולמי כל אחד כפוף."},
    {"question": "מה מאפיין ארגון שבנוי על בסיס לקוחות לעומת ארגון על בסיס התמחות?", "options": ["הוא נועד לקצר את התהליך בשביל הלקוח", "התהליך בו הרבה יותר ארוך", "אינו קשור לתפוקות", "מבוסס על אזורים"], "answer": 0, "hint": "המטרה היא לייצר זרימה מהירה ונוחה לאדם שמקבל את השירות."},
    {"question": "בגישת המערכות הפתוחות, מהם ארבעת השלבים המרכזיים?", "options": ["תשומה, המרה, תפוקה, משוב", "תכנון, ביצוע, בקרה, תגמול", "ייצור, שיווק, מכירה, רווח", "רעיון, פיתוח, השקה, ביקורת"], "answer": 0, "hint": "מתחילים בהכנסת משאבים, משנים אותם, מוציאים תוצר, ומקבלים תגובה מהסביבה."},
    {"question": "מי נכלל בסביבת ה'מיקרו' (הסביבה האוהדת) של הארגון?", "options": ["ספקים, לקוחות, עובדים ומוסדות פיננסיים", "ממשלות ומיסוי", "חוקי המדינה", "טכנולוגיות גלובליות"], "answer": 0, "hint": "אלו הגורמים הקרובים ביותר לארגון שמקיימים איתו אינטראקציה ישירה ויומיומית."},
    {"question": "לפי עציוני, מה תרבות ארגונית חזקה מאפשרת להנהלה לעשות?", "options": ["לשלוט בפעולות העובדים ולהפחית התנגדויות", "להוריד מיסים", "לבטל היררכיה", "להגדיל חופשות"], "answer": 0, "hint": "היא יוצרת 'נורמות' שגורמות לעובדים ליישר קו מרצונם בלי לייצר קונפליקטים."},
    {"question": "מה מיוחד בתרבות ארגונית 'שבטית'?", "options": ["הלקוחות נחשבים שותפים, והדגש הוא על נאמנות וצוות", "היא נוקשה ומלאה בחוקים", "התפיסה היא שהסביבה עוינת", "מתמקדת רק ברווח מהיר"], "answer": 0, "hint": "הארגון מתנהג כמו משפחה אחת גדולה שמשקיעה בפיתוח העובד והמורל."},
    {"question": "על פי אלטון מאיו (ניסויי האוטורן), מה גורם לרמת ביצוע משופרת?", "options": ["מוטיבציה חברתית ותשומת לב מיוחדת לעובד", "תגמול כספי בלבד", "שליטה ניהולית נוקשה", "תאורה פלורסנטית"], "answer": 0, "hint": "הניסוי הוכיח שאנשים עובדים טוב יותר פשוט כי הם יודעים שמישהו מתעניין בהם."},
    {"question": "מתי נכון להפעיל 'מוטת שליטה צרה' (השגחה צמודה ורבה)?", "options": ["בתחומים מורכבים הנוגעים לכסף, חיי אדם או שלום הציבור", "בעבודות שגרתיות ופשוטות", "כשיש צוות אחיד לגמרי", "כאשר יש מערכות טכנולוגיות אוטומטיות"], "answer": 0, "hint": "זה מתאים למקומות שבהם טעות קטנה עלולה להיות קטלנית או לעלות הון."},
    {"question": "מה מאפיין אדם שמפעיל 'סמכותניות' (ולא סמכות רגילה)?", "options": ["פועל מתוך קונפליקטים אישיים ואמוציות שגוררות חבלה בעבודה", "פועל בצורה לגיטימית מתוקף תפקידו", "מאציל סמכויות בצורה מסודרת", "מגלה אמפתיה גבוהה"], "answer": 0, "hint": "זה מצב שבו המנהל מוציא את התסכולים הרגשיים שלו על העובדים (למשל, צועק רוב הזמן)."},
    {"question": "כיצד מבחינים בין בעיה טכנית ל'אתגר הסתגלותי'?", "options": ["אתגר הסתגלותי דורש שינוי אמונות ותפיסות, ומלווה באובדן או כאב", "בעיה טכנית נמשכת יותר זמן", "באתגר הסתגלותי משתמשים רק בידע קיים", "אין דרך להבחין ביניהם"], "answer": 0, "hint": "אם זה לא דורש ממך לעשות וויתור רגשי או לשנות גישה עמוקה – זה כנראה לא אתגר מהסוג הזה."},
    {"question": "איזו פעולה מסייעת ל'הורדת הטמפרטורה' כשהארגון בלחץ?", "options": ["פירוק הבעיה לגורמים ומיקוד זמני בבעיות טכניות", "הסבת תשומת לב לבעיות הקשות כדי להגביר דריכות", "הסרת המנהל", "התעלמות מהעובדים"], "answer": 0, "hint": "כשחם מדי, כדאי לפרק את הבעיה הגדולה לחלקים קטנים וטכניים יותר כדי להרגיע את כולם."},
    {"question": "שיטת תקצוב המכונה 'גזור-הדבק' שמבוססת על השנה הקודמת היא:", "options": ["תקציב תוספתי", "תקציב בסיס אפס", "תקציב פעולות", "תקצוב לפי יעדים"], "answer": 0, "hint": "לוקחים את מה שהיה, מוסיפים התאמה למדד (דלתא) וממשיכים הלאה."},
    {"question": "מהי אחת הסכנות המרכזיות ב'תקציב בסיס אפס'?", "options": ["לא מתאים לארגונים גדולים ועלול לגרור פיטורים מיותרים", "לא בודק תפוקות בכלל", "מייצר הוצאות כפולות", "מקשה על בקרה"], "answer": 0, "hint": "אם נשאל את עצמנו כל שנה מחדש 'למה אנחנו קיימים', אנחנו עלולים לערער את ליבת הארגון ולפטר כוח אדם."},
    {"question": "על מי מוטלת האחריות לעריכת התקציב הכולל בארגון?", "options": ["על המנהל (בשיתוף רכזים), כשהוא מוציא לפועל את מדיניות ההנהלה", "על רואה החשבון בלבד", "על הלקוחות האסטרטגיים", "על העובדים הזוטרים"], "answer": 0, "hint": "ההנהלה רק קובעת את הכיוון (מדיניות), אבל איש השטח המרכזי הוא זה שבונה את המספרים."},
    {"question": "מה חייבים לכלול בטבלאות השכר כדי לא להיות מופתעים?", "options": ["את 'עלות המעביד' הכוללת ולא רק את שכר הברוטו", "רק עובדים בכירים", "שעות נוספות בלבד", "קנסות אפשריים"], "answer": 0, "hint": "המשכורת שרשומה בחוזה היא אף פעם לא ההוצאה האמיתית של בעל העסק."},
    {"question": "מה תפקידו של 'דו\"ח תזרים' בשונה ממאזן בוחן?", "options": ["מראה את הכסף הזמין שיש לעסק לשלם איתו כרגע (ולא רק רווח על הנייר)", "מראה את ההיסטוריה הגיאוגרפית של המכירות", "משקף רק חובות", "אין הבדל"], "answer": 0, "hint": "עסק יכול להיות סופר רווחי על הנייר, אבל לפשוט רגל כי פשוט אין לו מזומן בקופה היום."},
    {"question": "תקשורת הזורמת מהמנהל לעובד ('מלמעלה למטה') נקראת:", "options": ["תקשורת נותנת הוראות, שדורשת בקרה וגם ביצוע", "תקשורת מדווחת", "תקשורת אופקית", "מערכת רב-ערוצית"], "answer": 0, "hint": "זה סוג התקשורת שלא מספיק רק להבין אותה, העובד גם חייב לקום ולעשות משהו בנידון."}
]

# אתחול משתני המשחק והגרלת 15 שאלות
if "game_state" not in st.session_state:
    st.session_state.game_state = "start"
    st.session_state.selected_questions = []
    st.session_state.current_question = 0
    st.session_state.lifelines = {"5050": True, "audience": True, "phone": True}
    st.session_state.hidden_options = []
    st.session_state.hint_message = ""

def reset_game():
    st.session_state.game_state = "playing"
    st.session_state.selected_questions = random.sample(ALL_QUESTIONS, 15)
    st.session_state.current_question = 0
    st.session_state.lifelines = {"5050": True, "audience": True, "phone": True}
    st.session_state.hidden_options = []
    st.session_state.hint_message = ""

col_title, col_icon = st.columns([8, 1])
with col_title:
    st.title("💰 מי רוצה להיות מיליונר? 💰")
st.markdown("---")

if st.session_state.game_state == "start":
    st.subheader("ברוכים הבאים למשחק הטריוויה האישי שלך!")
    st.write("בכל משחק יוגרלו 15 שאלות חדשות מתוך המאגר המלא.")
    st.write("לרשותך 3 גלגלי הצלה: 50:50, עזרת הקהל, וחבר טלפוני (לקבלת רמז).")
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("התחל במשחק", type="primary", use_container_width=True):
        reset_game()
        st.rerun()

elif st.session_state.game_state == "playing":
    q_idx = st.session_state.current_question
    current_q = st.session_state.selected_questions[q_idx]

    if "shuffled_options" not in st.session_state or st.session_state.current_q_idx != q_idx:
        opts_with_idx = list(enumerate(current_q["options"]))
        random.shuffle(opts_with_idx)
        st.session_state.shuffled_options = [opt for i, opt in opts_with_idx]
        st.session_state.correct_idx = next(i for i, (orig_i, opt) in enumerate(opts_with_idx) if orig_i == current_q["answer"])
        st.session_state.current_q_idx = q_idx

    correct_answer_idx = st.session_state.correct_idx
    options_list = st.session_state.shuffled_options

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
            if st.button("👥 עזרת הקהל", use_container_width=True):
                letters = ["א'", "ב'", "ג'", "ד'"]
                st.session_state.hint_message = f"**הקהל הצביע!** רוב מוחץ בקהל (74%) חושב שהתשובה הנכונה היא {letters[correct_answer_idx]}."
                st.session_state.lifelines["audience"] = False
                st.rerun()
        else:
            st.button("👥 עזרת הקהל (נוצל)", disabled=True, use_container_width=True)

    with col_l3:
        if st.session_state.lifelines["phone"]:
            if st.button("📞 חבר טלפוני", use_container_width=True):
                st.session_state.hint_message = f"**רמז מהחבר הטלפוני:** '{current_q['hint']}'"
                st.session_state.lifelines["phone"] = False
                st.rerun()
        else:
            st.button("📞 חבר טלפוני (נוצל)", disabled=True, use_container_width=True)

    with col_info:
        current_prize = PRIZE_LADDER[q_idx - 1] if q_idx > 0 else 0
        st.markdown(f"<h4 style='margin:0;'>שאלה {q_idx + 1} מתוך 15</h4><span>סכום מובטח כרגע: <b>{current_prize:,} ₪</b></span>", unsafe_allow_html=True)

    if st.session_state.hint_message:
        st.info(st.session_state.hint_message)

    st.markdown("---")
    st.subheader(f"{current_q['question']}")
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    letters = ["א'", "ב'", "ג'", "ד'"]

    for i, option in enumerate(options_list):
        target_col = col1 if i % 2 == 0 else col2
        with target_col:
            if i in st.session_state.hidden_options:
                st.button(f"{letters[i]}. (הוסתר)", disabled=True, key=f"opt_{i}", use_container_width=True)
            else:
                if st.button(f"{letters[i]}. {option}", key=f"opt_{i}", use_container_width=True):
                    if i == correct_answer_idx:
                        st.session_state.hidden_options = []
                        st.session_state.hint_message = ""
                        if q_idx + 1 >= 15:
                            st.session_state.game_state = "won"
                        else:
                            st.session_state.current_question += 1
                        st.rerun()
                    else:
                        st.session_state.game_state = "lost"
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

elif st.session_state.game_state == "won":
    st.balloons()
    st.success("🏆 כל הכבוד! ענית על כל השאלות נכון וזכית במיליון שקלים!")
    if st.button("שחק שוב - שאלות חדשות", type="primary"):
        reset_game()
        st.rerun()

elif st.session_state.game_state == "lost":
    st.error("❌ טעות! תשובה שגויה.")
    q_idx = st.session_state.current_question
    final_prize = 32000 if q_idx >= 10 else 1000 if q_idx >= 5 else 0
    st.warning(f"הפסדת את המשחק, אך סיימת עם סכום זכייה של: **{final_prize:,} ₪**")
    if st.button("נסה שוב - שאלות חדשות", type="primary"):
        reset_game()
        st.rerun()
