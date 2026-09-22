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
        "question": "כיצד מוגדרת 'סמכות' בחומר הנלמד?", 
        "options": ["היכולת לאכוף ציות", "היכולת לתקצב", "אחריות מוחלטת", "העברת אחריות"], 
        "answer": 0, 
        "hint": "זה קשור לאכיפה ומשמעת של עובדים.",
        "explanation": "סמכות היא היכולת לאכוף ציות. התפקיד מאפשר למנהל לגרום לאנשים לעשות מה שהוא רוצה, וזו זכות לגיטימית בארגון."
    },
    {
        "question": "מה קורה לבעל סמכות שאינו אוכף ציות?", 
        "options": ["הוא גוזר על עצמו לבצע את המשימות בעצמו או לעמוד מול כישלונות", "הוא מקבל בונוס", "האחריות עוברת לעובד", "הוא מפוטר מידית"], 
        "answer": 0, 
        "hint": "אם הוא לא דורש מאחרים לעשות, הוא ישלם את המחיר בעצמו.",
        "explanation": "סמכות מלווה באחריות. לכן, אם המנהל מוותר על אכיפת ציות, בסופו של דבר הוא יצטרך לשאת בתוצאות ולעשות את העבודה לבד."
    },
    {
        "question": "מה ההבדל בין האצלת סמכות לביזור סמכות?", 
        "options": ["בהאצלה האחריות נשארת אצל המאציל ולטווח קצר, בביזור היא עוברת באופן קבוע", "ביזור הוא זמני והאצלה היא קבועה", "אין הבדל", "בהאצלה העובד אינו מיומן"], 
        "answer": 0, 
        "hint": "בהאצלה אתה עדיין אשם אם משהו משתבש.",
        "explanation": "בהאצלת סמכות מעבירים את הסמכות לטווח קצר והאחריות נשארת אצל המנהל. בביזור, מעבירים באופן קבוע את הסמכות ויחד איתה גם את האחריות."
    },
    {
        "question": "מתי הכי נכון להשתמש בסגנון ניהול 'מכוון'?", 
        "options": ["כשלעובד אין מיומנות ואין זמן ללמד אותו", "כשיש זמן רב והעובד מיומן", "כשהמיומנות גבוהה", "בבניית תקציב"], 
        "answer": 0, 
        "hint": "במצב חירום כשחייבים להסביר לעובד בדיוק מה לעשות צעד אחר צעד.",
        "explanation": "סגנון מכוון מתאים כשמעורבות המנהל והשליטה שלו צריכות להיות גבוהות מאוד, כי לעובד אין מיומנות ואין למנהל זמן ללמד."
    },
    {
        "question": "באיזה סגנון ניהול המעורבות והשליטה נמוכות (למשל: לבקש מהילד לזרוק את הפח)?", 
        "options": ["מאציל", "מייעץ", "מכוון", "משתף"], 
        "answer": 0, 
        "hint": "פעולה שאתה משחרר למישהו אחר כי אין לך זמן והוא מיומן לעשותה לבד.",
        "explanation": "בסגנון מאציל, המיומנות של העובד (או הילד) גבוהה, ולמנהל אין זמן. לכן המעורבות והשליטה שלו נמוכות."
    },
    {
        "question": "בסגנון 'מייעץ' (מיומנות נמוכה אך יש מספיק זמן), כיצד פועל המנהל?", 
        "options": ["שואל שאלות מנחות ומכוונות", "נותן הוראות כמו לתוכי", "מבצע בעצמו", "מקיים הצבעה"], 
        "answer": 0, 
        "hint": "המנהל פועל כמו מנטור או מדריך - הוא לא פותר את הבעיה עבור העובד.",
        "explanation": "מנהל מייעץ לא מכתיב פתרונות אלא משתמש בשאלות מנחות כדי לעזור לעובד הלא-מיומן להגיע להחלטה הנכונה בעצמו, מה שלוקח יותר זמן."
    },
    {
        "question": "על פי מודל 'טבעת הזהב' (מעגל הזהב), במה מתמקדים ארגונים מסוג 'Why'?", 
        "options": ["במה הארגון מאמין ולמה הוא מתאים ללקוח", "מהו המוצר בלבד", "איך מייצרים את המוצר", "בתקציב השנתי"], 
        "answer": 0, 
        "hint": "הם פונים ללב ולייחודיות של האדם ולא רק לתכונות הטכניות.",
        "explanation": "ארגוני Why לא מסבירים מיד מהו המוצר, אלא קודם כל פונים לייחודיות של האדם, מציגים במה הארגון מאמין ולמה זה מתאים ללקוח."
    },
    {
        "question": "לפי חוק פריצת תודעת הלקוח, איזה אחוז מהלקוחות קונים ראשונים לפי ה-Why?", 
        "options": ["13.5%", "50%", "80%", "5%"], 
        "answer": 0, 
        "hint": "מדובר בשכבה קטנה של 'מאמצים מוקדמים' שנעים סביב המספר 13.",
        "explanation": "השכבה הראשונה שקונה לפי האמונה (ה-Why) מהווה 13.5% מהלקוחות, וכל שאר הלקוחות כבר נגררים בעקבותיהם."
    },
    {
        "question": "לפי מקס ובר, מהן הבעיות המרכזיות שמבנה ארגוני משרטט אמור לפתור?", 
        "options": ["איתור כפילויות ומניעת קונפליקטים", "שחיקת עובדים", "תמחור מוצרים", "גיוס לקוחות חדשים"], 
        "answer": 0, 
        "hint": "כשיש עץ היררכי מסודר, פתאום רואים מי עולה על מי.",
        "explanation": "שרטוט עץ ארגוני עוזר לראות כפילויות בין מחלקות, ומונע קונפליקטים משום שברור למי כל סמכות כפופה."
    },
    {
        "question": "מה מאפיין ארגון שבנוי על בסיס לקוחות לעומת ארגון על בסיס התמחות?", 
        "options": ["הוא נועד לקצר את התהליך בשביל הלקוח", "התהליך בו הרבה יותר ארוך", "אינו קשור לתפוקות", "מבוסס על אזורים"], 
        "answer": 0, 
        "hint": "המטרה היא לייצר זרימה קלה ומהירה למקבל השירות.",
        "explanation": "ארגון על בסיס התמחות מאריך את התהליך כי הוא מתמקד במקצועיות הטהורה. ארגון על בסיס לקוחות מתמקד בלקוח ולכן מקצר עבורו את התהליך."
    },
    {
        "question": "בגישת המערכות הפתוחות, מהם ארבעת השלבים המרכזיים?", 
        "options": ["תשומה, המרה, תפוקה, משוב", "תכנון, ביצוע, בקרה, תגמול", "ייצור, שיווק, מכירה, רווח", "רעיון, פיתוח, השקה, ביקורת"], 
        "answer": 0, 
        "hint": "מתחילים בהכנסת משאבים (ציוד, כוח אדם), משנים אותם, ומוציאים תוצר.",
        "explanation": "הארגון מקבל 'תשומה' מהסביבה, 'ממיר' אותה בתהליך העבודה, מוציא 'תפוקה' בצורת מוצר או שירות, וממתין ל'משוב' הלקוחות."
    },
    {
        "question": "מי נכלל בסביבת ה'מיקרו' (הסביבה האוהדת) של הארגון?", 
        "options": ["ספקים, לקוחות, עובדים ומוסדות פיננסיים", "ממשלות ומיסוי", "חוקי המדינה", "טכנולוגיות גלובליות"], 
        "answer": 0, 
        "hint": "הגורמים הקרובים ביותר לארגון שמקיימים איתו קשר ישיר.",
        "explanation": "סביבת המיקרו האוהדת כוללת את השותפים היומיומיים שרוצים בהצלחת הארגון: הלקוחות, הספקים, העובדים והבנקים."
    },
    {
        "question": "לפי החוקר עציוני, מה מאפשרת תרבות ארגונית חזקה?", 
        "options": ["לשלוט בפעולות העובדים ובחוויותיהם ולהפחית התנגדויות", "להוריד מיסים", "לבטל היררכיה", "להגדיל חופשות"], 
        "answer": 0, 
        "hint": "יוצרת זהות ארגונית שמונעת חיכוכים.",
        "explanation": "התרבות הארגונית היא מערכת של ערכים ונורמות שמשמשת תשתית השומרת על יציבות ומאפשרת לשלוט בקונפליקטים ללא התנגדות מורגשת מצד העובדים."
    },
    {
        "question": "על פי אלטון מאיו (ניסויי האוטורן), מה גורם לרמת ביצוע משופרת של עובדים?", 
        "options": ["מוטיבציה חברתית ותשומת לב מיוחדת לעובד", "תגמול כספי בלבד", "שליטה ניהולית נוקשה", "תאורה חזקה יותר"], 
        "answer": 0, 
        "hint": "אנשים עובדים טוב יותר כשהם מרגישים שמתעניינים בהם.",
        "explanation": "המחקר גילה שתשומת הלב המיוחדת שהעובדים קיבלו מהחוקרים (הפן החברתי-אנושי) העלתה את הביצועים שלהם הרבה יותר מכל תנאי פיזי כמו תאורה או חימום."
    },
    {
        "question": "מתי נכון להפעיל 'מוטת שליטה צרה' (השגחה צמודה ורבה)?", 
        "options": ["בתחומים מורכבים הנוגעים לכסף, חיי אדם או שלום הציבור", "בעבודות שגרתיות ופשוטות", "כשיש צוות אחיד לגמרי", "כאשר יש מערכות טכנולוגיות אוטומטיות"], 
        "answer": 0, 
        "hint": "מתאים למקומות שבהם טעות קטנה עלולה לעלות בחיי אדם או בהמון כסף.",
        "explanation": "מוטת שליטה צרה מתאימה לארגונים מורכבים במיוחד (כמו רפואה, צבא או הנדסה) שבהם פיקוח הדוק נדרש כדי למנוע אסונות הקשורים בחיי אדם ורכוש."
    },
    {
        "question": "מה מאפיין אדם שמפעיל 'סמכותניות' (ולא סמכות לגיטימית רגילה)?", 
        "options": ["הוא פועל מתוך קונפליקטים אישיים ואמוציות הגוררים חבלה בעבודה", "הוא פועל בצורה רגועה מתוקף תפקידו", "הוא מאציל סמכויות בצורה מובנית", "הוא מנהל דמוקרטי לחלוטין"], 
        "answer": 0, 
        "hint": "מנהל שמוציא תסכולים רגשיים על העובדים (צועק, מתעצבן).",
        "explanation": "סמכותניות נובעת מקונפליקטים אישיים של מפעיל הסמכות המדבר מתוך רגש, ומשליך מעצמו את האחריות על אחרים (למשל, מנהל שרק צועק על עובדיו)."
    },
    {
        "question": "כיצד ניתן להבחין בין 'בעיה טכנית' לבין 'אתגר הסתגלותי'?", 
        "options": ["אתגר הסתגלותי דורש שינוי עמדות ואמונות ומלווה באובדן או כאב רגשי", "בעיה טכנית נמשכת זמן רב יותר", "באתגר הסתגלותי המנהל פותר הכל בעצמו עם ידע קיים", "אין דרך ממשית להבחין ביניהם"], 
        "answer": 0, 
        "hint": "אם זה לא דורש מהעובד לשנות גישה עמוקה או לוותר על משהו אמוציונלי - זה כנראה לא אתגר הסתגלותי.",
        "explanation": "באופן מהותי, בניגוד לבעיה טכנית (כמו חריגה בתקציב הניתנת לחישוב מחדש), אתגר הסתגלותי מחייב את האדם לבחור בין ערכים מנוגדים ולוותר על תפיסה קיימת."
    },
    {
        "question": "איזו פעולה מומלצת כדי ל'הוריד את הטמפרטורה' כשהארגון מצוי בלחץ סביב אתגר?", 
        "options": ["פירוק הבעיה לגורמים טכניים וחיזוק מערכות יחסים", "הסבת תשומת הלב לבעיות הקשות כדי להגביר דריכות", "הסרת המנהל מתפקידו", "התעלמות מוחלטת מהעובדים"], 
        "answer": 0, 
        "hint": "פישוט הבעיה המורכבת לתת-משימות כדי להרגיע את כולם.",
        "explanation": "כדי להוריד לחץ (טמפרטורה), מתמקדים זמנית בדברים טכניים (מי עושה מה ומתי) במקום באתגר הרגשי, ומחזקים את יחסי העבודה והגיבוש בצוות."
    },
    {
        "question": "שיטת תקצוב המכונה 'גזור-הדבק' שמבוססת על השנה הקודמת היא:", 
        "options": ["תקציב תוספתי", "תקציב בסיס אפס", "תקציב פעולות", "תקצוב לפי יעדים"], 
        "answer": 0, 
        "hint": "לוקחים את מה שהיה בשנה שעברה, ומוסיפים דלתא קטנה.",
        "explanation": "תקציב תוספתי פשוט מבוסס על השנה הקודמת בתוספת התאמות מדדיות קטנות. היתרון הוא שזה נוח לתכנון, החיסרון הוא שאין חשיבה מחודשת על המטרות."
    },
    {
        "question": "מהי אחת הסכנות המרכזיות בשימוש ב'תקציב בסיס אפס'?", 
        "options": ["זה לא מתאים לארגונים גדולים ועלול לגרור פיטורים ולערער את ליבת המוסד", "זה מונע לחלוטין את אפשרות ההתייעלות", "זה מונע מאנשים לתכנן פרויקטים חדשים", "אין בזה שום סיכון"], 
        "answer": 0, 
        "hint": "אם שואלים כל שנה מחדש 'למה המחלקה הזו בכלל קיימת?', אפשר לפרק את החברה.",
        "explanation": "תקציב בסיס אפס בוחן מחדש כל שנה את עצם קיום המחלקות. בארגון שיש בו 80% שכר קבוע, מהלך כזה עלול להוביל ישירות לפיטורים המוניים ולחוסר יציבות."
    },
    {
        "question": "על מי מוטלת האחריות לעריכת התקציב הכולל בארגון?", 
        "options": ["על המנהל (בשיתוף רכזים), כשהוא מוציא לפועל את המדיניות שקבעה ההנהלה", "על רואה החשבון בלבד", "על הלקוחות האסטרטגיים", "על ההנהלה הבכירה שמבצעת אותו לבדה"], 
        "answer": 0, 
        "hint": "ההנהלה רק קובעת את הכיוון (מדיניות), אבל איש השטח הוא שבונה את המספרים.",
        "explanation": "ההנהלה נותנת את מדיניות העל. על המנהל מוטלת האחריות לאסוף נתונים ולבנות את התקציב יחד עם מנהלי התחומים והרכזים שלו."
    },
    {
        "question": "מה תפקידו של 'דו\"ח תזרים' בשונה מ'מאזן בוחן'?", 
        "options": ["דו\"ח תזרים משקף את הכסף הזמין בפועל (המזומן) שעומד לרשות העסק", "דו\"ח תזרים מראה רק הוצאות ומאזן בוחן רק הכנסות", "דו\"ח תזרים מלמד האם העסק מורווח היסטורית בטווח הארוך", "אין הבדל ממשי ביניהם"], 
        "answer": 0, 
        "hint": "אפשר להיות סופר רווחי על הנייר (מאזן בוחן), אבל לפשוט רגל כי פשוט אין מזומן בקופה היום.",
        "explanation": "בעוד מאזן בוחן מראה רווחיות על הנייר (הכנסות מול הוצאות), דו\"ח התזרים קריטי להישרדות העסק כי הוא מראה את היכולת הממשית שלו לפעול עם הכסף הזמין שיש לו כרגע."
    },
    {
        "question": "איזו תקשורת זורמת מהעובד למנהל (מלמטה למעלה)?", 
        "options": ["תקשורת מדווחת, הדורשת בקרת קבלה של המסר בלבד", "תקשורת נותנת הוראות, שדורשת ביצוע", "תקשורת אופקית, שאין בה יחסי מרות", "תקשורת רב-ערוצית אוטומטית"], 
        "answer": 0, 
        "hint": "העובד לא מחלק פקודות למנהל, הוא רק משקף לו מצב.",
        "explanation": "תקשורת מלמטה למעלה נועדה בעיקר לדווח (על קשיים, בעיות, רעיונות). בניגוד לתקשורת מלמעלה למטה שדורשת פעולה מהעובד, כאן דרוש רק שהמנהל יקבל את המסר (ויבצע בקרה)."
    },
    {
        "question": "בתהליך של מניעת קונפליקטים (ניהול הסתגלותי), מהי סביבה תומכת?", 
        "options": ["מרחב שמצליח להכיל את הלהט ולווסת את הלחץ כדי להתמודד עם המחלוקת בלי לברוח", "סביבה שבה לא מדברים כלל על הבעיות הרגשיות", "סביבה שנותנת בונוסים כספיים לכל עובד ממורמר", "הורדה מיידית של מטרות הארגון"], 
        "answer": 0, 
        "hint": "כמו 'מרחב פיזי מוגן' ושפה משותפת שמאפשרים לשים את הבעיות על השולחן.",
        "explanation": "יצירת סביבה תומכת (למשל נסיעה משותפת לעבודה במלון או ישיבת צוות מובנית) מאפשרת לצוות להתמודד חזיתית עם מחלוקות עמוקות מבלי לברוח מהן וללא חשש."
    },
    {
        "question": "מדוע התקשורת הארגונית לעיתים קרובות מורכבת?", 
        "options": ["משום שיש בה סוגי הפרעות שונות כמו הבדלי סטטוס ותחרותיות אישית", "כי היא תמיד מתבצעת בשפה זרה", "כי אין מספיק שעות ביום", "כי הציוד הטכנולוגי בארגון לקוי בדרך כלל"], 
        "answer": 0, 
        "hint": "למשל, כשסטודנט פונה ישירות לרקטור ויש פער ברמות התפקיד, או כשיש אינטרסים סמויים.",
        "explanation": "התקשורת הופכת מורכבת עקב 4 הפרעות עיקריות, ביניהן הבדלי סטטוס מובהקים בין השולח למקבל, ופרשנויות שונות של סיטואציות ממניעים של תחרות ומיצוב (תחרות סמויה)."
    }
]

if "game_state" not in st.session_state:
    st.session_state.game_state = "start"
    st.session_state.selected_questions = []
    st.session_state.current_question = 0
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
    st.subheader("ברוכים הבאים לאתגר הזמנים (יסודות הניהול)!")
    st.write("ענו נכון על 15 שאלות מהר ככל האפשר. הטיימר מתחיל לרוץ מיד עם הלחיצה!")
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("התחל במשחק והפעל שעון", type="primary", use_container_width=True):
        reset_game()
        st.rerun()

elif st.session_state.game_state == "playing":
    q_idx = st.session_state.current_question
    current_q = st.session_state.selected_questions[q_idx]

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
                    letters = ["א'", "ב'", "ג'", "ד'"]
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

        col1, col2 = st.columns(2)
        letters = ["א'", "ב'", "ג'", "ד'"]

        for i, option in enumerate(options_list):
            target_col = col1 if i % 2 == 0 else col2
            with target_col:
                if i in st.session_state.hidden_options:
                    st.button(f"{letters[i]}. (הוסתר)", disabled=True, key=f"opt_{i}", use_container_width=True)
                else:
                    if st.button(f"{letters[i]}. {option}", key=f"opt_{i}", use_container_width=True):
                        st.session_state.is_correct = (i == correct_answer_idx)
                        
                        if not st.session_state.is_correct or q_idx == 14:
                            st.session_state.end_time = time.time()
                            
                        st.session_state.history.append({
                            "question": current_q['question'],
                            "user_ans": option,
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
