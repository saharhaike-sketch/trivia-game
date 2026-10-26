import random
import streamlit as st
import time

st.set_page_config(page_title="מיליונר - הגות צבאית", page_icon="⚔️", layout="wide")

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
        .stApp { background: radial-gradient(circle at 50% 50%, #1c2833 0%, #000000 100%); }
        [data-testid="stSidebar"] { background: linear-gradient(180deg, #1c2833 0%, #000000 100%) !important; border-left: 2px solid #ce9b2c; }
        [data-testid="stSidebar"] * { color: #ffffff !important; }
        h1, h2, h3, h4, p, span, .stMarkdown, li { color: white !important; }
        
        .stButton>button {
            background-color: #0b172a;
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
        "question": "במה שונה גישתו של סון טסו מקלאוזביץ ביחס להפעלת כוח צבאי?",
        "options": [
            "סון טסו רואה בשימוש בכוח מפלט אחרון ומעדיף ניצחון ללא קרב, בעוד קלאוזביץ רואה בהשמדת האויב את מטרת הקרב.",
            "סון טסו מאמין שיש להשמיד ערים מיד בתחילת המלחמה, וקלאוזביץ מעדיף רק לוחמת גרילה.",
            "שניהם מאמינים שיש להימנע לחלוטין משימוש בכלי נשק תחת כל מצב.",
            "קלאוזביץ מאמין שמלחמה היא משחק דיפלומטי שאינו כולל אלימות."
        ],
        "answer": 0,
        "hint": "מי אמר ש'שיא הכשרון הוא לנצח ללא לחימה'?",
        "explanation": "סון טסו מחפש את הדרך הזולה ביותר והשגת ניצחון ללא שפיכות דמים. קלאוזביץ ריאליסטי יותר ומאמין שפיתרון ללא קרב הוא אשליה, וההכרעה דורשת אלימות והשמדת כוח האויב."
    },
    {
        "question": "מהו סדר העדיפויות של סון טסו לתקיפת 'מרכזי הכובד' של האויב?",
        "options": [
            "תחילה לתקוף את האסטרטגיה והתוכניות, אחר כך את הבריתות, אחר כך את הצבא, ולבסוף את הערים.",
            "תחילה את ערי הבירה, אחר כך את הצבא, ולבסוף את הכלכלה.",
            "תחילה את צבא האויב בקרב מכריע, ואחר כך את המנהיג הפוליטי.",
            "לסון טסו אין סדר עדיפויות מוגדר, הכל תלוי במזג האוויר ביום הפלישה."
        ],
        "answer": 0,
        "hint": "הוא מעדיף לפרק את האויב פוליטית לפני שהקרב מתחיל.",
        "explanation": "סדר העדיפויות של סון טסו הוא מהקל אל הכבד: קודם לשבש תוכניות, אחר כך בריתות, רק אז לתקוף את הצבא, וכיבוש ערים הוא המוצא האחרון והיקר ביותר."
    },
    {
        "question": "מהו סדר העדיפויות לתקיפת 'מרכז כובד' על פי קלאוזביץ?",
        "options": [
            "השמדת צבא האויב, לאחר מכן כיבוש הבירה, ואז מהלומה נגד בעל הברית העיקרי.",
            "תקיפת תוכניות האויב, לאחר מכן שיבוש בריתותיו, ורק לבסוף תקיפת צבאו.",
            "לוחמה פסיכולוגית מול העם, ולאחר מכן ניסיון להתנקש במנהיג.",
            "כיבוש ערי גבול קטנות והתקדמות איטית ללא חיכוך."
        ],
        "answer": 0,
        "hint": "הוא הולך ישר אל הלב הפיזי והשלטוני של היריב.",
        "explanation": "בניגוד לסון טסו, קלאוזביץ מציב את השמדת צבא האויב כעדיפות עליונה (הגישה הישירה), ומיד לאחר מכן את כיבוש בירתו. דיפלומטיה ובריתות נמצאות אצלו בתחתית הרשימה."
    },
    {
        "question": "מהו 'השילוש הפרדוקסלי' שמרכיב את אופי המלחמה לפי קלאוזביץ?",
        "options": [
            "העם (אלימות ולהט), הצבא והמצביא (רוח יצירתית והסתברות), והממשלה (תבונה ויעדים מדיניים).",
            "מודיעין (עיניים), כוח אדם (רגליים), ולוגיסטיקה (ידיים).",
            "חיל האוויר, חיל הים, וחיל היבשה.",
            "אסטרטגיה, טקטיקה, ולוחמת גרילה."
        ],
        "answer": 0,
        "hint": "הלב, הידיים והראש של המדינה.",
        "explanation": "השילוש של קלאוזביץ מורכב משלוש מגמות שולטות: העם (אלימות קמאית ושנאה), הצבא (מקריות, אומץ ורוח יצירתית) והממשלה (שיקולים רציונליים ויעדים מדיניים)."
    },
    {
        "question": "מהי המשמעות של 'לרבע את המשולש' בהקשר לתיאוריה של קלאוזביץ?",
        "options": [
            "הוספת הצלע החומרית-כלכלית-טכנולוגית לשילוש המקורי, שכן אי אפשר לנצח בכוח רצון בלבד.",
            "הכפלת כמות הדיביזיות התוקפות כנגד עמדות הגנה.",
            "ביטול סמכות הממשלה והעברתה לצבא באופן זמני.",
            "הוספת דעת הקהל הבינלאומית כגורם מכריע בפני עצמו."
        ],
        "answer": 0,
        "hint": "חסר מרכיב פיזי כמו טווח נשק, ניידות ותעשייה.",
        "explanation": "השילוש המקורי מורכב מגורמים לא חומריים (מטאפיזיים). כדי לקבל הבנה מלאה ומציאותית, יש 'לרבע את המשולש' ולהוסיף את הסביבה החומרית: טכנולוגיה, ניידות, כלכלה וכלי נשק."
    },
    {
        "question": "מהו 'חיכוך' (Friction) בתורת המלחמה של קלאוזביץ?",
        "options": [
            "הפער בין התכנון לביצוע הנובע מאי-ודאות, מקריות, עייפות, מזל ומודיעין שגוי.",
            "התנגשות פוליטית בין הצבא לממשלה לפני פרוץ המלחמה.",
            "חוסר היכולת של דיפלומטים להסכים על תנאי שלום סופיים.",
            "התהליך שבו הצבא מפרק מנשקם את אזרחי האויב המובסים."
        ],
        "answer": 0,
        "hint": "מה הופך פעולה פשוטה לקשה מאוד בשטח?",
        "explanation": "חיכוך הוא כל מה שהופך את המלחמה במציאות לשונה מזו שעל הנייר. זהו כוח מצטבר של אי-ודאות, סכנה, עייפות וטעויות שאי אפשר לחשב מראש ('הדבר הפשוט ביותר הוא קשה')."
    },
    {
        "question": "במה מאופיין גישת ז'ומיני לאמנות המלחמה?",
        "options": [
            "הוא ניסה לבנות תיאוריה מדעית בעלת חוקים קבועים, ודגל בעליונות הצבא על המדיניות מרגע שהמלחמה פרצה.",
            "הוא התנגד לחלוטין לשימוש בטכנולוגיה חדישה ודבק בסוסים בלבד.",
            "הוא האמין שרק הדרג המדיני צריך לקבל החלטות טקטיות בשטח.",
            "הוא המציא את מודל 'מעגל הזהב' של השיווק הצבאי."
        ],
        "answer": 0,
        "hint": "הוא ראה את המפקד כ'מדען' שצריך חופש מהפוליטיקאים.",
        "explanation": "ז'ומיני היה מודע מאוד לטכנולוגיה וחימוש, וחיפש תיאוריה 'מדעית' של המלחמה. הוא האמין שלאחר פרוץ המלחמה יש לתת עדיפות לשיקולים צבאיים מקצועיים על פני התערבות הדרג המדיני."
    },
    {
        "question": "מהם שלושת השלבים של מלחמה ממושכת על פי מאו טסה-טונג?",
        "options": [
            "הגנה/נסיגה אסטרטגית, שיווי משקל (מלחמת התשה), ומתקפת נגד להכרעה.",
            "הונאה דיפלומטית, כיבוש מהיר, ופירוק הבריתות.",
            "התקפה קצרה, נסיגה לערי הבירה, וחתימה על הסכם שלום.",
            "הפצצות אוויריות, פלישה רגלית, ומשא ומתן כלכלי."
        ],
        "answer": 0,
        "hint": "תהליך הדרגתי שמתחיל בנסיגה ומסתיים במתקפה.",
        "explanation": "בניגוד לקלאוזביץ שרואה שני מצבים (הגנה והתקפה) עם מעבר מהיר, מאו מתאר תהליך הדרגתי: נסיגה עד 'הנקודה הסופית לנסיגה', שלב מעבר של קיפאון/שיווי משקל, ורק אז מעבר למתקפת נגד."
    },
    {
        "question": "מה מבטאת 'דוקטרינת ויינברגר' (שיושמה בהצלחה במלחמת המפרץ 1991)?",
        "options": [
            "ארה\"ב תיכנס למלחמה רק כאינטרס חיוני, עם כוח מכריע, יעדים ברורים, תמיכת דעת הקהל, וכמוצא אחרון.",
            "ארה\"ב מחויבת להילחם בכל מקום בעולם כנגד קומוניזם ללא קשר לדעת הקהל.",
            "שימוש קבוע בנשק גרעיני טקטי בסכסוכים מקומיים כדי לסיים אותם מהר.",
            "חובה לבצע הונאה אסטרטגית בכל עימות צבאי במזרח התיכון."
        ],
        "answer": 0,
        "hint": "רשימת תנאים זהירה לאחר טראומת וייטנאם.",
        "explanation": "הדוקטרינה היא יישום מעשי של תפיסות קלאוזביץ, המגבילה יציאה למלחמה ל-6 תנאים רציונליים, ביניהם תמיכת הציבור והקונגרס, והגדרת יעדים ברורים וברי-השגה."
    },
    {
        "question": "מהי 'טקטיקיזציה של האסטרטגיה'?",
        "options": [
            "מצב שבו שיקולים צבאיים-מבצעיים (הדקדוק של הקרב) מכתיבים את המדיניות, או העתקת ניסיון טקטי לאסטרטגיה.",
            "הפיכת חיילים פשוטים לקציני מטה ללא הכשרה אסטרטגית מוקדמת.",
            "שימוש נרחב מדי בנשק מדויק ללא פקודות ברורות מהדרג העליון.",
            "העדפת כלי נשק ישנים על פני טכנולוגיה מודרנית בשדה הקרב."
        ],
        "answer": 0,
        "hint": "כש'הדקדוק של הקרב' מנהל את הפוליטיקה (למשל, גרמניה ב-WW1).",
        "explanation": "טקטיקיזציה קורית כשמפקדים (כמו נפוליאון, היטלר או המטה הגרמני) מאפשרים לאילוצי הקרב או לניסיונם בשטח להשתלט על היעדים הפוליטיים והאסטרטגיים הרחבים."
    },
    {
        "question": "כיצד תופס סון טסו את השימוש בצ'נג (Cheng) וצ'י (Ch'i)?",
        "options": [
            "צ'נג הוא הכוח הרגיל שמרתק את האויב חזיתית, וצ'י הוא הכוח העקיף שמכה באגף בהפתעה.",
            "צ'נג הוא מערכת המודיעין האנושי, וצ'י הוא כוח השריון הראשי.",
            "צ'נג מציין תקיפה באור יום, וצ'י מציין תקיפה תחת מעטה הלילה.",
            "אין להם שימוש צבאי, אלו הם מונחים מתוך אסטרטגיה דיפלומטית לפני המלחמה."
        ],
        "answer": 0,
        "hint": "אחד נגד הפנים כדי למשוך תשומת לב, השני מגיע מהצד.",
        "explanation": "זהו שילוב של תמרון והונאה: הכוח הרגיל (צ'נג) מעסיק את האויב חזיתית, בעוד הכוח המיוחד/עקיף (צ'י) מכה בנקודה החלשה. הם פועלים יחד ויכולים להחליף תפקידים תוך כדי קרב."
    },
    {
        "question": "מדוע קלאוזביץ סקפטי לגבי השימוש במודיעין במלחמה?",
        "options": [
            "הוא רואה בו לרוב עוד מקור של רעש, ערפל וחיכוך שאי אפשר לסמוך עליו בזמן אמת.",
            "הוא סבור שמרגלים תמיד בוגדים במדינה שלהם עקב פיתוי כספי.",
            "כי אין לו ערך במלחמה טוטלית שמוכרעת רק בכוח אש מאסיבי.",
            "הוא דווקא מעריץ מודיעין ורואה בו את מכפיל הכוח החשוב ביותר, בניגוד לסון טסו."
        ],
        "answer": 0,
        "hint": "הוא מעדיף לסמוך על האינטואיציה של המפקד במקום על דוחות שסותרים זה את זה.",
        "explanation": "בשונה מסון טסו שמקדש את המודיעין כעיניים ואוזניים, קלאוזביץ טוען שבשל המורכבות והכאוס, המודיעין לרוב מוטעה או סותר. במקומו הוא סומך על אינטואיציית המפקד ('טביעת העין')."
    },
    {
        "question": "מהי 'נקודת שיא ההתקפה' לפי קלאוזביץ?",
        "options": [
            "הנקודה הדינמית שבה כוח התוקף נשחק מספיק כך שמאזן הכוחות עומד להתהפך לטובת המגן.",
            "הרגע שבו האויב חותם על הסכם כניעה מוחלט וללא תנאים.",
            "הנקודה הגיאוגרפית הגבוהה ביותר בשדה הקרב שיש לכבוש כדי להציב ארטילריה.",
            "הרגע שבו הדרג המדיני מאשר שימוש בנשק השמדה המוני."
        ],
        "answer": 0,
        "hint": "כמו גומייה שנמתחת עד שהיא קרובה להיקרע.",
        "explanation": "ככל שההתקפה מתקדמת, התוקף מאבד כוח (קווי אספקה מתארכים, עייפות) והמגן צובר יתרון. הסכנה היא שמפקד נועז יחצה את נקודת השיא ללא אבחנה, ויאבד את יתרונו."
    },
    {
        "question": "מהו 'עקרון ההמשכיות' (או עקרון הרדיפה) לפי קלאוזביץ?",
        "options": [
            "צד שהשיג יתרון חייב להפעיל לחץ רצוף ולא לתת לאויב מנוחה להשיב את שיווי משקלו.",
            "החובה לשמור על אותה ממשלה ואותו רמטכ\"ל לאורך כל שנות המלחמה.",
            "העיקרון שיש להמשיך להילחם תמיד באותה טקטיקה כדי למנוע בלבול בקרב החיילים.",
            "התלות המוחלטת של הצבא בקווי אספקה מתמשכים שמגיעים מהעורף."
        ],
        "answer": 0,
        "hint": "אם פגעת באויב והוא נפל, אל תיתן לו זמן לקום.",
        "explanation": "עיקרון זה קובע שאין הגיון במתן שהות לאויב להתאושש. לעומתו, הצד החלש שואף ל'ניתוק המשכיות' (עקרון ההמתנה) כדי להרוויח זמן, לסגת ולהיבנות מחדש."
    },
    {
        "question": "מדוע בדרך כלל יש הפסקות וחוסר פעולה במלחמה, למרות עקרון ההמשכיות?",
        "options": [
            "בשל עליונות ההגנה על ההתקפה, ועקב 'עקרון הידע החסר' הגורם לתוקף לא להבין את יתרונו.",
            "בשל התערבות ממושכת של גורמים בינלאומיים המחייבת הפסקות אש שבועיות.",
            "כי החיילים דורשים זמני מנוחה קבועים לפי חוקי מלחמה המעוגנים באמנות בינלאומיות.",
            "כי הטכנולוגיה המודרנית דורשת זמן רב לתחזוקה לאחר כל הפעלת אש כבדה."
        ],
        "answer": 0,
        "hint": "יותר קל להחזיק שטח מלקחת אותו, ולפעמים גם כשיש לך יתרון אתה לא יודע את זה.",
        "explanation": "ההגנה חזקה מההתקפה (לפי קלאוזביץ, פי 2), ולכן אם הכוחות שווים, התוקף יהסס לפעול. בנוסף, 'הידע החסר' (מודיעין לקוי) גורם לתוקף להעריך בחסר את כוחו, מה שמוביל להמתנה."
    },
    {
        "question": "לפי מקיאוולי, כיצד הרפובליקה הרומית נהגה לסיים מלחמות באופן יציב?",
        "options": [
            "על ידי בחירה באחת משתי אפשרויות קיצון: להשמיד ולשעבד לחלוטין, או להעניק תנאי שלום נדיבים ושוויון.",
            "על ידי הטלת קנסות כספיים קטנים בלבד שאפשרו לאויב להשתקם באופן עצמאי.",
            "על ידי בניית חומות הגנה והתעלמות מוחלטת מהאויב המובס עד שייכנע רשמית.",
            "על ידי חילופי שבויים וויתור על כל השטחים שנכבשו כדי להפגין רצון טוב."
        ],
        "answer": 0,
        "hint": "או שאתה מוחץ אותו עד עפר, או שאתה הופך אותו לחבר שווה.",
        "explanation": "מקיאוולי טען שפתרון של 'אמצע' (כפיית תנאים משפילים מבלי להשמיד) לא יחזיק מעמד ויעורר נקמה. לכן הרומאים בחרו בקיצון: או השמדה ושעבוד מוחלטים, או שותפות ונדיבות."
    },
    {
        "question": "מהי משמעות 'השליטה האובייקטיבית' של הדרג המדיני על פי סמואל הנטינגטון?",
        "options": [
            "המדינאי קובע את המטרות אך אינו מתערב בעניינים הצבאיים המקצועיים של המפקד בשטח.",
            "המדינאי מנהל את הצבא ישירות מהחפ\"ק ומכתיב כל מהלך מבצעי וטקטי.",
            "הצבא שולט במדינה ומוביל את המהלכים המדיניים לפי צרכיו האובייקטיביים.",
            "שליטה הנשענת אך ורק על שימוש במחשבי-על ומודלים מתמטיים כדי לנהל את המלחמה."
        ],
        "answer": 0,
        "hint": "הפוליטיקאי מגדיר 'מה', החייל מחליט 'איך'.",
        "explanation": "בשליטה אובייקטיבית המנהיג המדיני שולט ביעדי המלחמה, אך נותן למפקד את המרחב המקצועי להוציא אותם לפועל. בשליטה סובייקטיבית, הפוליטיקאי מתערב טקטית בהחלטות שדה."
    },
    {
        "question": "לפי מאו טסה-טונג, מהי 'הערכה נטו' (Net Assessment)?",
        "options": [
            "ניתוח מקיף ואובייקטיבי של כלל היכולות (צבאיות, פוליטיות, כלכליות) של הצדדים כדי לזהות יתרון יחסי.",
            "ספירה פשוטה של כמות הטנקים של האויב כדי לקבוע מי ינצח בקרב הקרוב.",
            "הערכת כמות הפיצויים שהאויב ישלם לאחר תום המלחמה.",
            "שיטה לחישוב עלות פיתוח כלי נשק עתידיים והצדקתם מול הממשל."
        ],
        "answer": 0,
        "hint": "לשקול את כל הכוחות בשני הצדדים כדי להחליט איך בדיוק להילחם.",
        "explanation": "מאו האמין שאפשר להשיג תמונה אובייקטיבית דרך ניתוח יסודי של יחסי הכוחות ('הערכה נטו') בכל המישורים. ניתוח זה מאפשר לזהות נקודות תורפה ולהכתיב את אופי המלחמה."
    },
    {
        "question": "על פי תורת המשחקים, איזה סגנון מנהיגות מאפיין את קלאוזביץ לעומת סון טסו?",
        "options": [
            "קלאוזביץ מעדיף 'מקסי-מקס' (סיכון מרבי, רווח מרבי), בעוד סון טסו מעדיף 'מיני-מקס' (סיכון מזערי, רווח מרבי).",
            "קלאוזביץ מעדיף 'מיני-מקס', וסון טסו מעדיף 'מקסי-מקס'.",
            "שניהם מעדיפים סיכון מזערי בכל מחיר, כדי לשמור על חיי אדם.",
            "שניהם מעדיפים סיכון מרבי ללא כל שיקול דעת, כדי לסיים את המלחמה מהר."
        ],
        "answer": 0,
        "hint": "קלאוזביץ אוהב תעוזה ולשבור קדימה; סון טסו אוהב חוכמה וחישוב זהיר.",
        "explanation": "קלאוזביץ נוטה לצד המצביא הנועז שמעדיף סיכון מרבי עבור רווח מרבי (סגנון רומל). סון טסו שמרן ומחושב יותר, ומעדיף מינימום סיכון למקסימום רווח (סגנון מונטגומרי)."
    },
    {
        "question": "מה היה 'מרכז הכובד' האמיתי של עיראק במלחמת המפרץ, שפספסו (ולכן המלחמה לא הסתיימה פוליטית)?",
        "options": [
            "סדאם חוסיין עצמו (מרכז כובד פוליטי ומנהיגותי).",
            "הצבא העיראקי בשטח כווית.",
            "מאגרי הנפט ומתקני הזיקוק בכווית.",
            "הברית החשאית של עיראק עם ברית המועצות."
        ],
        "answer": 0,
        "hint": "תבוסת הצבא בשטח לא סיימה את הסיפור כי הראש נשאר על הכתפיים.",
        "explanation": "הקואליציה התייחסה לצבא העיראקי כמרכז הכובד. למעשה, מרכז הכובד הפוליטי האמיתי היה השלטון של סדאם חוסיין - ולכן נצחון צבאי מוחץ לא תורגם לניצחון מדיני סופי."
    },
    {
        "question": "מהי גישת סון טסו למודיעין צבאי?",
        "options": [
            "זהו מכפיל כוח קריטי: 'צבא ללא סוכנים חשאיים משול לאדם ללא עיניים ואוזניים'.",
            "הוא חסר משמעות, שכן ניתן להכריע כל אויב רק באמצעות מסה קריטית של חיילים.",
            "יש לסמוך רק על מודיעין גלוי המגיע מדיפלומטים רשמיים.",
            "אין להשתמש בסוכנים חשאיים כי הדבר מנוגד לכללי המוסר והדיפלומטיה."
        ],
        "answer": 0,
        "hint": "הוא מאמין שלפני שזזים חייבים לדעת הכל.",
        "explanation": "בעוד קלאוזביץ ספקן לגבי מודיעין, סון טסו רואה בו תנאי הכרחי לניצחון וליישומה של ההערכה נטו, וטוען שהסוכנים החשאיים צריכים להיות האנשים הקרובים ביותר למצביא."
    },
    {
        "question": "מה מאפיין מפקד 'קלאוזביצי' בהשוואה למפקד של 'סון טסו' (בהנחה של תנאים שווים)?",
        "options": [
            "יש לו סיכוי טוב יותר לנצח משום שהוא מציאותי, ריכז את כוחו ומוכן לאלימות, בעוד השני עלול לראות במלחמה תרגיל אינטלקטואלי.",
            "הוא תמיד יפסיד משום שהוא מתעלם לחלוטין ממודיעין ותכנון.",
            "הוא יסכים תמיד להצעות שלום מצד האויב ברגע הראשון שיוצגו.",
            "הוא ישתמש בהונאה כדי להימנע מקרב חזיתי בכל מחיר."
        ],
        "answer": 0,
        "hint": "מול כוח ברוטלי ומרוכז שבא להשמיד אותך, תחבולות עדינות לא תמיד עובדות.",
        "explanation": "חולשת הגישה של סון טסו היא ההרתעה משפיכות דמים שהופכת את המלחמה למשחק שחמט עדין. מפקד קלאוזביצי שמרכז כוח ומוכן לאלימות ישירה ינצח ככל הנראה מפקד שסומך יותר מדי על הונאה כ'תרופת פלא'."
    },
    {
        "question": "מדוע קלאוזביץ מתנגד לתיאוריות המנסות לצמצם את המלחמה ל'מדע' מתמטי מדויק?",
        "options": [
            "כי הן מתעלמות מהגורמים הנפשיים והמוסריים, שאי אפשר לכמת אך הם לרוב מכריעים יותר מהכוח החומרי.",
            "משום שמתמטיקה לא הייתה מפותחת מספיק במאה ה-19.",
            "מפני שהוא האמין שמלחמה צריכה להיות מנוהלת על ידי אנשי דת ופילוסופים.",
            "כי הוא פחד שטכנולוגיה חדישה תחליף את תפקיד הגנרל האנושי לחלוטין."
        ],
        "answer": 0,
        "hint": "אי אפשר להכניס 'אומץ' או 'שנאה' לתוך משוואה.",
        "explanation": "קלאוזביץ ראה בניסיונות לכמת את המלחמה (כפי שעשה ז'ומיני) דבר ש'מעורר סלידה אינטלקטואלית', שכן המלחמה מלאה בגורמים נפשיים ונייטרליים (פחד, אומץ, חיכוך) שמשנים הכל."
    },
    {
        "question": "מה הייתה הטעות בהבנת 'אופי המלחמה' של ארצות הברית בווייטנאם?",
        "options": [
            "ארה\"ב ניהלה מלחמה קונבנציונלית חזיתית מול לוחמת גרילה של האויב, והתעלמה מהצורך בתמיכה מדינית מבית.",
            "ארה\"ב השתמשה רק בכוחות דיפלומטיים ללא נשק חם.",
            "ארה\"ב התעלמה מדעת הקהל בווייטנאם, אך זכתה לתמיכה מלאה בתוך ארה\"ב.",
            "ארה\"ב זיהתה בטעות את סין כמרכז הכובד במקום את הצפון וייטנאמים."
        ],
        "answer": 0,
        "hint": "הם ניסו להשתמש בפטיש כבד נגד יתוש זריז, ולא הבינו שהציבור שלהם מאבד סבלנות.",
        "explanation": "אי הבנת 'אופי המלחמה' גרם לאמריקאים להשתמש בטכנולוגיה וכוח קונבנציונלי כבד מול מלחמת גרילה שחקה את כוח הרצון. המלחמה אבדה בגלל שדעת הקהל האמריקאית (אחת מצלעות השילוש) נשברה."
    },
    {
        "question": "מהו תפקידו של ה'גאון הצבאי' (ומאפיין 'טביעת העין' - Coup d'oeil) לפי קלאוזביץ?",
        "options": [
            "לראות את התמונה המלאה במבט אחד בתוך ערפל הקרב, ולפצות על חוסר במודיעין אמין דרך אינטואיציה ותעוזה.",
            "לכתוב פקודות ברורות ומפורטות שכל חייל יוכל להבין ולשנן.",
            "להפעיל מחשבי-על כדי לחשב את סבירות הניצחון באחוזים.",
            "להיות המתווך הדיפלומטי מול מנהיגי האויב בשיחות שלום."
        ],
        "answer": 0,
        "hint": "כשיש כאוס ולא יודעים כלום, צריך מישהו שמבין בבטן מה צריך לעשות.",
        "explanation": "מכיוון שהמלחמה רוויה בחיכוך ומודיעין חסר, אי אפשר להסתמך רק על חישובים. נדרש מנהיג עם 'טביעת עין' - אינטואיציה מולדת שמסוגלת לקלוט את קשרי הגומלין המורכבים ולקבל החלטות נכונות גם בחוסר ודאות."
    },
    {
        "question": "מה הייתה תפיסתו של סון טסו לגבי מלחמה ממושכת?",
        "options": [
            "יש להימנע ממנה בכל מחיר; המלחמה צריכה להיות קצרה ומכרעת ככל האפשר כדי לא לאבד את תמיכת העם.",
            "היא הדרך הטובה ביותר לשחוק את האויב, ולכן עדיף להאריך אותה כמה שניתן.",
            "היא אינה משפיעה על הכלכלה כל עוד הצבא ממשיך לנצח בקרבות.",
            "היא מאפשרת למפקדים לצבור ניסיון יקר ערך ולכן היא מבורכת."
        ],
        "answer": 0,
        "hint": "גם סון טסו וגם קלאוזביץ הסכימו על זה - הזמן עולה בדם וכסף.",
        "explanation": "סון טסו מזהיר שמלחמה ממושכת שואבת משאבים ומייאשת את העם (אובדן תמיכה). לכן הוא דוגל בניצחון מהיר ומכריע. גם קלאוזביץ תמים דעים ש'כל השתהות מיותרת היא בזבוז כוח'."
    },
    {
        "question": "כיצד מגדיר סון טסו את ה'גישה העקיפה'?",
        "options": [
            "תמרון והונאה שמטרתם לעקוף את מוקדי הכוח של האויב ולהכות בו היכן שהוא חלש או לא מוכן.",
            "שליחת דיפלומטים למדינה שלישית כדי שיעבירו מסרים לאויב בעקיפין.",
            "בניית קווי אספקה עוקפים מסביב לשדה הקרב כדי לחסוך בדלק.",
            "שימוש בנשק ארטילרי שיורה במסלול תלול ועקיף מעל חומות."
        ],
        "answer": 0,
        "hint": "לא ללכת ראש בראש מול קיר הלבנים, אלא למצוא את הדלת האחורית פתוחה.",
        "explanation": "הגישה העקיפה מתבססת על תמרון (כמו השימוש בכוח ה'צ'י') כדי להימנע מהתנגשות חזיתית עם העוצמה העיקרית של האויב, ותקיפתו באגפים או בנקודות תורפה תוך ניצול ההפתעה."
    },
    {
        "question": "מהו הפרדוקס של ה'גישה העקיפה' המודרנית?",
        "options": [
            "אם האויב צופה מראש את המהלך העקיף, הרי שהוא נערך אליו - ואז הגישה הופכת למעשה לישירה וחזיתית.",
            "ככל שהיא עקיפה יותר, כך היא דורשת יותר כוח אדם, ולכן היא יקרה יותר מגישה ישירה.",
            "היא עובדת רק על אויבים חכמים מאוד, ואויב טיפש לא יבין שמנסים לעקוף אותו.",
            "היא מחייבת את התוקף לפצל את כוחותיו כך שהוא תמיד מפסיד."
        ],
        "answer": 0,
        "hint": "אם עשית תרגיל כדי להפתיע מישהו, והוא ידע שתעשה אותו... חזרת להתחלה.",
        "explanation": "חולשת הגישה העקיפה (למשל של סון טסו) היא שאם האויב מבצע הערכה נטו נכונה וצופה את המהלך ה'עקיף', הוא מציב שם את כוחותיו. ברגע שזה קורה, הגישה העקיפה מאבדת את יתרון ההפתעה והופכת להתנגשות ישירה לכל דבר."
    },
    {
        "question": "מה קובע 'עקרון ההשמדה' בתפיסתו של קלאוזביץ?",
        "options": [
            "השמדת כוחות האויב בקרב גדול חייבת תמיד להיות השיקול העיקרי במלחמה כדי להשיג את היעדים המדיניים.",
            "יש להשמיד את ערי האויב עד היסוד כדי לשבור את מורל האזרחים לחלוטין.",
            "יש להשמיד את מאגרי המזון של האויב עוד לפני פרוץ הקרבות.",
            "השמדה היא אמצעי פסול מבחינה מוסרית ויש להימנע ממנו בכל מחיר."
        ],
        "answer": 0,
        "hint": "הדרך הקצרה ביותר למטרה היא דרך חיסול כוח ההתנגדות הפיזי.",
        "explanation": "קלאוזביץ מאמין שהדרך הבטוחה והתכליתית ביותר (הגישה הישירה) לניצחון היא ריכוז הכוח לשם השמדת צבא האויב בקרב מכריע, כיוון שזו שוללת ממנו את היכולת הפיזית להתנגד."
    },
    {
        "question": "איך 'סיום המלחמה' בא לידי ביטוי במציאות לעומת 'הטיפוס האידיאלי' של קלאוזביץ?",
        "options": [
            "במציאות התוצאה לעולם אינה סופית והמובס רואה בה 'רע זמני'; לכן שלום יציב דורש תהליך מדיני שמתחשב באינטרסים של המנוצח.",
            "במציאות המנצח תמיד משמיד את המנוצח לחלוטין, בדיוק כמו בטיפוס האידיאלי של 'המלחמה המוחלטת'.",
            "במציאות מלחמות לעולם אינן מסתיימות, הן רק הופכות למלחמות כלכליות בלבד.",
            "במציאות סיום המלחמה נקבע אך ורק על ידי כמות ההרוגים בכל צד."
        ],
        "answer": 0,
        "hint": "אם תכריח מישהו להיכנע ותשפיל אותו, הוא יחכה להזדמנות הראשונה לנקום.",
        "explanation": "ב'מלחמה המוחלטת' התיאורטית המנצח מכתיב הכל. במציאות, הפסד צבאי לא מוחק את רצון הצד השני, שימתין להתאושש. לכן ניצחון צבאי הוא רק תנאי הכרחי; כדי לסיים באמת צריך משא ומתן מדיני שמעניק תנאים שהמובס יוכל לחיות איתם לאורך זמן."
    }
]

# --- ניהול מצב המשחק ---
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
    st.subheader("ברוכים הבאים לאתגר: מבוא להיסטוריה והגות צבאית ⚔️")
    st.write("ענו נכון על 15 שאלות (סון טסו, קלאוזביץ, ז'ומיני ומאו). הטיימר מתחיל לרוץ מיד עם הלחיצה!")
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("התחל במשחק והפעל שעון", type="primary", use_container_width=True):
        reset_game()
        st.rerun()

elif st.session_state.game_state == "playing":
    q_idx = st.session_state.current_question
    current_q = st.session_state.selected_questions[q_idx]

    # ערבוב תשובות כאשר שאלה חדשה מופיעה
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
            st.markdown("<p class='correct-answer'>🎉 תשובה נכונה!</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p class='wrong-answer'>❌ טעות בתשובה!</p>", unsafe_allow_html=True)
            st.warning(f"התשובה הנכונה היא: **{options_list[correct_answer_idx]}**")
        
        st.info(f"💡 **הסבר:** {current_q['explanation']}")
        
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
        
        # שורה ראשונה (א' ו-ב')
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

        # שורה שנייה (ג' ו-ד')
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
