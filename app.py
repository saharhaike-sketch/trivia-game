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
        "hint": "תחשוב על מי נשאר אשם אם משהו משתבש.",
        "explanation": "האצלת סמכות היא לטווח קצר והאחריות נשארת אצל המאציל. בביזור סמכות (העברה קבועה המעוגנת לרוב בתקנון), גם האחריות עוברת למקבל הסמכות."
    },
    {
        "question": "מתי נכון להשתמש בסגנון ניהול 'מכוון'?",
        "options": [
            "כשלעובד אין מיומנות ואין למנהל זמן ללמד אותו.",
            "כשיש מיומנות גבוהה אבל חסר זמן לביצוע.",
            "כשיש לעובד מיומנות נמוכה אך יש למנהל זמן רב ללמד.",
            "כאשר העובד מיומן מאוד והמשימה אינה שגרתית."
        ],
        "answer": 0,
        "hint": "מצב חירום שדורש עבודה בסגנון 'תוכי'.",
        "explanation": "סגנון מכוון מתאפיין ברמות שליטה ומעורבות גבוהות מאוד. הוא מתאים לסיטואציה בה המיומנות של העובד נמוכה, ואין למנהל זמן לייעץ או ללמד (למשל, חניכה בצבא בשעת חירום)."
    },
    {
        "question": "מה מאפיין את סגנון הניהול ה'מייעץ'?",
        "options": [
            "מיומנות העובד נמוכה, יש למנהל זמן, המעורבות גבוהה והמנהל משתמש בשאלות מנחות.",
            "מיומנות העובד גבוהה, אין זמן, והמנהל מספק פתרונות מהירים.",
            "מיומנות העובד גבוהה, המעורבות נמוכה, והמנהל משאיר את ההחלטה לעובד.",
            "מיומנות העובד נמוכה, אין זמן, והמנהל מבצע את הפעולה בעצמו."
        ],
        "answer": 0,
        "hint": "סגנון של מנטור שדורש סבלנות.",
        "explanation": "בסגנון מייעץ המנהל מנחה דרך שאלות ולא נותן פתרונות מוכנים. זה דורש מעורבות ושליטה גבוהות, ולכן מתאים למצב שבו יש למנהל זמן להשקיע בעובד הלא-מיומן."
    },
    {
        "question": "באיזה סגנון ניהול רמות השליטה והמעורבות של המנהל הן נמוכות?",
        "options": [
            "מאציל",
            "מכוון",
            "משתף",
            "מייעץ"
        ],
        "answer": 0,
        "hint": "כמו לבקש מהילד לזרוק את הפח.",
        "explanation": "בסגנון מאציל, המנהל פונה לעובד מיומן כשאין לו זמן להתעסק במשימה. לכן הוא משחרר אותה במעורבות ושליטה נמוכות, ומסתפק בבקרה."
    },
    {
        "question": "על פי מודל 'מעגל הזהב' (טבעת הזהב), מה מייחד ארגונים מסוג 'Why'?",
        "options": [
            "הם אינם מתחילים בהסבר על המוצר אלא פונים לייחודיות האדם ומסבירים במה הם מאמינים.",
            "הם מתמקדים רק בשורת הרווח ומתעלמים משירות הלקוחות.",
            "הם מתמקדים בתהליך הייצור הפנימי ובאיכות החומרים בלבד.",
            "הם ארגונים שמונעים רק ממוטיבציה חברתית של העובדים ולא מרווח."
        ],
        "answer": 0,
        "hint": "הם מסבירים קודם כל 'למה' הם קיימים ומתאימים ללקוח.",
        "explanation": "ארגוני Why (כמו אפל) פונים לרגש וללקוח עצמו לפני שהם מציעים את המוצר. לפי 'חוק פריצת תודעת הלקוח', 13.5% מהלקוחות קונים קודם כל לפי ה-Why, והשאר נגררים אחריהם."
    },
    {
        "question": "לפי מקס וובר, אילו בעיות עיקריות נפתרות כאשר משרטטים 'מבנה ארגוני' מסודר?",
        "options": [
            "איתור כפילויות ומניעת קונפליקטים סמכותיים.",
            "העלאת שכר העובדים ושיפור שביעות הרצון.",
            "הפחתת המיסוי הארגוני וייעול התקציב.",
            "מעבר אוטומטי מייצור המוני לייצור מותאם אישית."
        ],
        "answer": 0,
        "hint": "כשיש עץ, יודעים מי כפוף למי ומי עושה מה.",
        "explanation": "מקס וובר (אבי תורת הבירוקרטיה) טען ששרטוט עץ ארגוני חושף כפילויות בפונקציות, ומונע קונפליקטים כי כל תפקיד מוצא את מקומו וברור למי הוא כפוף."
    },
    {
        "question": "מה ההבדל בין ארגון שבנוי על בסיס התמחות (תשומות) לארגון על בסיס לקוחות (תפוקות)?",
        "options": [
            "ארגון על בסיס לקוחות נועד לקצר את התהליך עבור הלקוח, בעוד ארגון התמחותי מאריך אותו.",
            "ארגון התמחותי מיועד אך ורק לחברות הייטק, ואילו לקוחות מתאים רק לחנויות.",
            "בארגון על בסיס לקוחות אין היררכיה ניהולית כלל.",
            "אין הבדל משמעותי, שניהם מבוססים על אותו מודל של פאיול."
        ],
        "answer": 0,
        "hint": "איפה הלקוח מקבל שירות מהר יותר, ואיפה הוא עובר בין תחנות?",
        "explanation": "מבנה על בסיס התמחות מאריך את התהליך (הלקוח עובר בין מחלקות שונות). מבנה על בסיס לקוחות (תפוקות) מקצר את התהליך ומעניק ללקוח פתרון מקיף במקום אחד."
    },
    {
        "question": "מהם השלבים של ארגון הפועל כ'מערכת פתוחה'?",
        "options": [
            "תשומה, המרה, תפוקה, משוב.",
            "תכנון, ביצוע, שליטה, קנסות.",
            "חזון, מטרה, אסטרטגיה, שיווק.",
            "סמכות, אחראיות, האצלה, ביזור."
        ],
        "answer": 0,
        "hint": "הארגון לוקח משהו מהסביבה, משנה אותו, מוציא אותו, ומקשיב לתגובות.",
        "explanation": "תאוריית המנהל המודרנית רואה בארגון מערכת פתוחה המקיימת יחסי חליפין עם הסביבה דרך קליטת משאבים (תשומה), עיבודם (המרה), ייצור תוצר (תפוקה), והתאמה עתידית לפי תגובת הסביבה (משוב)."
    },
    {
        "question": "אילו גורמים מרכיבים את 'סביבת המיקרו' (הסביבה האוהדת) של הארגון?",
        "options": [
            "ספקים, לקוחות, עובדים ומוסדות פיננסיים.",
            "ממשלות, חוקים, מיסים ותקנות סביבה.",
            "ארגונים מתחרים, תרבות גלובלית ואקלים.",
            "ההנהלה הבכירה ויושב ראש הדירקטוריון בלבד."
        ],
        "answer": 0,
        "hint": "השותפים הקרובים שמקיימים יחסי גומלין עסקיים ישירים כדי שהארגון יצליח.",
        "explanation": "סביבת המיקרו האוהדת מורכבת מגורמים הקרובים לארגון שמושפעים ומשפיעים עליו באופן יומיומי: הלקוחות (הפרטיים והמוסדיים), הספקים, העובדים והבנקים."
    },
    {
        "question": "לפי החוקר עציוני, מה תפקידה של התרבות הארגונית?",
        "options": [
            "מאפשרת לשלוט בקונפליקטים, מפחיתה התנגדויות, ויוצרת זהות ארגונית להכוונה.",
            "מחליפה את הצורך בתקנון חוקים או במבנה ארגוני פורמלי.",
            "מיועדת רק לשיפור שיווק המוצר כלפי לקוחות חיצוניים.",
            "פועלת להגדלת תקציב הרווחה ופעילויות הפנאי של העובד."
        ],
        "answer": 0,
        "hint": "זוהי מעין 'מערכת הפעלה' סמויה ששומרת על יציבות ושקט תעשייתי.",
        "explanation": "תרבות ארגונית היא מערכת של ערכים ונורמות המהווה תשתית לארגון. עציוני טען שבעזרתה ניתן לשלוט בפעולות העובדים ולהפחית התנגדויות מבלי להפעיל כוח ישיר."
    },
    {
        "question": "איזו מבין התרבויות הארגוניות מאופיינת בהתייחסות ללקוחות כ'שותפים', ערכי נאמנות ופיתוח מורל העובד?",
        "options": [
            "תרבות שבטית",
            "תרבות היררכית",
            "תרבות מכירתית",
            "תרבות מכוונת מטרה"
        ],
        "answer": 0,
        "hint": "תרבות שרואה בארגון מעין משפחה גדולה.",
        "explanation": "התרבות השבטית מדגישה עבודת צוות, מורל ונאמנות. היא משקיעה בפיתוח העובד לטווח ארוך ורואה בלקוחות חלק מהמשפחה/הקהילה של הארגון."
    },
    {
        "question": "אילו 5 פונקציות ניהוליות הוגדרו על ידי הנרי פאיול?",
        "options": [
            "תכנון, ארגון, תיאום, פיקוד, שליטה ובקרה.",
            "שיווק, ייצור, הפצה, כספים, משאבי אנוש.",
            "סמכות, ביזור, השגחה, תגמול, פיטורים.",
            "יבוא, יצוא, פרסום, תמחור, משוב."
        ],
        "answer": 0,
        "hint": "פונקציות קלאסיות של ניהול כתפעול.",
        "explanation": "הנרי פאיול הציע עקרונות לניהול מובנה ואחיד, אותם חילק ל-5 פונקציות מרכזיות המאפיינות את עבודת המנהל: תכנון, ארגון, תיאום, פיקוד, ושליטה/בקרה."
    },
    {
        "question": "מה הוכיחו ניסויי האוטורן בראשות אלטון מאיו?",
        "options": [
            "תשומת לב מיוחדת ומוטיבציה חברתית משפרות רמת ביצוע יותר משינוי תנאים פיזיים.",
            "העלאת שכר היא הדרך היחידה להגביר תפוקה.",
            "בירוקרטיה נוקשה מונעת טעויות אנוש באופן מוחלט.",
            "ביזור סמכויות תמיד גורם לאנרכיה בארגון."
        ],
        "answer": 0,
        "hint": "הניסוי עם האור במפעל שהוכיח שלעובדים אכפת שמתעניינים בהם.",
        "explanation": "גישת יחסי האנוש של מאיו גילתה שדווקא תשומת הלב של החוקרים (הפן הרגשי והחברתי) היא שהעלתה את תפוקת העובדים, ולא השינויים בתאורה או בחימום."
    },
    {
        "question": "מתי ואיפה ארגון יישם 'מוטת שליטה צרה' (השגחה ותשומת לב רבה)?",
        "options": [
            "בתחומים מורכבים ורב-תחומיים הנוגעים לכסף, חיי אדם או שלום הציבור.",
            "במשימות שגרתיות ופשוטות בהן העובדים מבצעים פעולות חוזרות.",
            "כאשר רוב העבודה מבוצעת על ידי מערכות רובוטיות.",
            "במקומות שבהם העובדים מפוזרים גיאוגרפית באופן צפוף וקרוב."
        ],
        "answer": 0,
        "hint": "כשמדובר בנושאים שאסור לטעות בהם אפילו במילימטר.",
        "explanation": "מוטת שליטה צרה (המשקפת מדרג ניהולי תלול והשגחה אינטנסיבית) נדרשת במקצועות מורכבים הנוגעים לחיי אדם ולכסף, בניגוד לעבודות שגרתיות (מוטת שליטה רחבה)."
    },
    {
        "question": "מה ההבדל בין סמכות חוקית/לגיטימית לבין 'סמכותניות'?",
        "options": [
            "סמכותניות נובעת מקונפליקטים אישיים ואמוציות שגוררים חבלה בעבודה, בעוד סמכות היא הפעלת זכות לגיטימית מתוקף תפקיד.",
            "סמכותניות מבוססת על ידע מקצועי וניסיון (מומחה), בעוד סמכות חוקית קשורה לגיל המנהל.",
            "בסמכותניות המנהל נותן חופש פעולה מוחלט, בעוד בסמכות הוא אוכף ציות.",
            "אין הבדל, מדובר במילים נרדפות לאותו סגנון ניהול בדיוק."
        ],
        "answer": 0,
        "hint": "מנהל שצועק ומשליך אחריות לעומת מנהל שמקבל החלטות בקור רוח.",
        "explanation": "סמכות היא זכות פורמלית שמקבל המנהל. סמכותניות, לעומת זאת, היא הפעלת הכוח מתוך קונפליקט רגשי, זלזול, צעקות או התנהגות אמוציונלית, הגוררת למרירות, היעדרויות ונטישת עובדים."
    },
    {
        "question": "כיצד מבחין ד\"ר טאוב בין 'בעיה טכנית' ל'אתגר הסתגלותי'?",
        "options": [
            "אתגר הסתגלותי דורש שינוי אמונות ותפיסות ומלווה באובדן או כאב, בעוד בעיה טכנית נפתרת באמצעות ידע קיים.",
            "אתגר הסתגלותי הוא תמיד פיננסי, ואילו בעיה טכנית קשורה למכונות בלבד.",
            "בעיה טכנית נמשכת זמן רב יותר ודורשת מעורבות של כל העובדים בארגון.",
            "אתגר הסתגלותי נפתר תמיד על ידי המנהל לבדו ללא מעורבות העובדים."
        ],
        "answer": 0,
        "hint": "אם אין כאב או ויתור אישי, זה כנראה לא אתגר הסתגלותי.",
        "explanation": "בעיה טכנית נפתרת על ידי בעל הסמכות עם כלים ידועים. אתגר הסתגלותי דורש למידה חדשה, שינוי מהותי בהתנהגות העובד וויתור על ערכים נוכחיים, מה שגורר תחושת אובדן וכאב."
    },
    {
        "question": "איזו פעולה מומלצת כדי 'להוריד טמפרטורה' בארגון שמצוי בלחץ סביב אתגר הסתגלותי?",
        "options": [
            "מיקוד בבעיות טכניות (פירוק לגורמים), וחיזוק מערכות יחסים בינאישיות.",
            "הסבת תשומת הלב לבעיות הקשות כדי לגרום לעובדים להרגיש את כובד האחריות.",
            "פיטורים מיידיים של העובדים שמתקשים להסתגל.",
            "ביטול מוחלט של יעדי הארגון והעלאת המשכורות."
        ],
        "answer": 0,
        "hint": "פישוט הבעיה המסובכת והרגעה של העובד מול האתגר.",
        "explanation": "כדי להוריד לחץ במצבי משבר (הורדת טמפרטורה), המנהל יכול לפרק את הבעיה לתת-משימות טכניות קטנות, לקחת על עצמו יותר אחריות באופן זמני, ולחזק את הגיבוש בצוות."
    },
    {
        "question": "מהו 'תקציב תוספתי' (גזור-הדבק)?",
        "options": [
            "תקציב המבוסס תמיד על שנת התקציב הקודמת בתוספת התאמות מדדיות קטנות (דלתא).",
            "תקציב שבו בוחנים מחדש כל סעיף מאפס.",
            "תקציב המתמקד בתוצרים ותפוקות של פרויקטים ספציפיים בלבד.",
            "תקציב שכולל רק סעיפי הוצאה על משכורות לעובדים זמניים."
        ],
        "answer": 0,
        "hint": "לוקחים את מה שהיה ומוסיפים לו קצת.",
        "explanation": "תקציב תוספתי מתבסס על הוצאות השנה הקודמת פלוס עלויות אינפלציה/מדד. היתרון הוא שזה נוח ומונע זעזועים, אך החיסרון הוא שאין חשיבה מחודשת על התייעלות."
    },
    {
        "question": "מהי אחת הסכנות המרכזיות ביישום 'תקציב בסיס אפס' בארגונים גדולים?",
        "options": [
            "בארגון עם כוח אדם קבוע רב, שאילת שאלות יסוד כל שנה עלולה להוביל לפיטורים המוניים ולערעור ליבת המוסד.",
            "הוא מעודד הוצאות מיותרות של פרויקטים כפולים.",
            "לא ניתן לבצע בו שום בקרה אתית על תפוקות הארגון.",
            "הוא מבוסס רק על תקציב השנה הקודמת ואינו מאפשר חדשנות."
        ],
        "answer": 0,
        "hint": "אם בודקים כל מחלקה מאפס, מגלים מהר מאוד שלא כולם נחוצים.",
        "explanation": "תקציב בסיס אפס בוחן מחדש כל פריט בכל שנה. למרות שהוא מצוין להתייעלות, בארגונים שבהם השכר הוא 80% מהתקציב, המהלך הזה יוביל לזעזועים ולפיטורים שעלולים לפרק את הארגון."
    },
    {
        "question": "כיצד 'תקצוב פעולות' שונה מסוגי תקציב אחרים?",
        "options": [
            "הוא מתמקד במהות הפרויקטים ובתפוקות, ללא קשר לחלוקה המסורתית של מחלקות הארגון.",
            "הוא רושם רק פריטי חומרים וציוד ללא שכר.",
            "הוא מאציל את כל סמכויות התקצוב לדרג הזוטר בלבד.",
            "הוא מתעדכן בכל יום מחדש לפי מצב המניות של החברה בבורסה."
        ],
        "answer": 0,
        "hint": "מה שמודדים זה הפעולה, לא המבנה הארגוני הרגיל.",
        "explanation": "תקצוב פעולות ממוקד בפרויקט עצמו ותפוקותיו. הוא מאפשר לכמת במדויק עלויות פרויקט, אך החיסרון הוא שקשה לבקר דרכו את סך ההוצאות הרגילות של המחלקות השונות."
    },
    {
        "question": "מה תפקידו של 'דו\"ח תזרים' בשונה מ'מאזן בוחן'?",
        "options": [
            "דו\"ח תזרים משקף את הכסף הזמין (המזומן) שקיים כרגע להפעלת העסק, בעוד מאזן בוחן מלמד על רווחיות כוללת (הכנסות מול הוצאות).",
            "דו\"ח תזרים מופק רק פעם בשנה, בעוד מאזן בוחן מופק כל יום.",
            "דו\"ח תזרים בודק רק הוצאות עתידיות, ומאזן בוחן בודק רק הכנסות מהעבר.",
            "אין הבדל, שניהם הם בדיוק אותו הדבר בשפה חשבונאית."
        ],
        "answer": 0,
        "hint": "עסק מורווח על הנייר יכול לפשוט רגל אם אין לו מזומן לשלם לעובדים ב-10 לחודש.",
        "explanation": "מאזן הבוחן מראה האם בסך הכל נכנס יותר משיצא (רווח), אך התזרים בודק את תזמון הכספים - האם יש כרגע מספיק כסף זמין בקופה כדי לשלם משכורות וחובות בזמן אמת."
    },
    {
        "question": "איזו תקשורת זורמת בדרך כלל 'מלמטה למעלה' (מעובד למנהל)?",
        "options": [
            "תקשורת מדווחת, שדורשת בקרה של קבלת המסר בלבד.",
            "תקשורת נותנת הוראות, שדורשת גם קבלה וגם ביצוע.",
            "תקשורת אופקית המשמשת רק לפתרון קונפליקטים אישיים.",
            "תקשורת רב-ערוצית אוטומטית שאינה דורשת מעורבות אנושית."
        ],
        "answer": 0,
        "hint": "העובד לא מנחית פקודות על המנהל, הוא פשוט מעדכן אותו.",
        "explanation": "תקשורת מעובד למנהל נועדה בעיקר לדיווח. בניגוד לתקשורת שיורדת מהמנהל ודורשת ביצוע, כאן המטרה היא שהמנהל יקבל את המסר ויבצע עליו בקרה."
    },
    {
        "question": "מה מאפיין 'תקשורת רב-ערוצית' בהשוואה למערכת חד-ערוצית מסורתית?",
        "options": [
            "היא מנתבת שיחות אוטומטית לפי אופי הלקוח, ומקטינה את הסמכות ההיררכית הישירה של המנהל לכדי בקרות בלבד.",
            "היא מרכזת את כל הפניות לאדם אחד (מרכזייה) שמעביר אותן הלאה ידנית.",
            "היא מבוססת רק על שיחות פנים-אל-פנים במשרדי החברה.",
            "היא מבטלת את הצורך בבקרת איכות."
        ],
        "answer": 0,
        "hint": "כמו הנתבים האוטומטיים בחברות הסלולר.",
        "explanation": "במערכת רב ערוצית, הניתוב נעשה בצורה אוטומטית ללא מגע יד אדם (או התערבות מנהל), מה שמשנה את תפקיד המנהל מהיררכי קלאסי לניהול באמצעות בקרות."
    },
    {
        "question": "מהי מטרת ה'בקרה' בארגון על פי הסיכום הנלמד?",
        "options": [
            "זהו תהליך מתמיד של השוואה בין ביצוע לתכנון, במטרה להכניס שינויים ולהקטין פערים בלתי רצויים.",
            "להעניש עובדים שלא עמדו ביעדי המכירות החודשיים.",
            "לסנן מידע פנימי כדי שלא יגיע לידיים של מתחרים.",
            "ליצור תקציב שנתי מבוסס רק על הוצאות העבר."
        ],
        "answer": 0,
        "hint": "בדיקה מול התוכנית המקורית כדי לתקן סטיות בזמן.",
        "explanation": "הבקרה נתפסת ככלי ניהולי חיוני. הגישה המובילה היא לבצע אותה לאורך התהליך, להשוות כל העת בין התכנון לביצוע בשטח, וליזום שינויים מידיים כדי לצמצם תקלות (הקטנת פערים)."
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
    st.subheader("ברוכים הבאים למשחק - יסודות הניהול (סגנונות, מבנים, תקציב)")
    st.write("ענו נכון על 15 שאלות. הטיימר מתחיל לרוץ מיד עם הלחיצה!")
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
        
        with row1_col_right: # העמודה הימנית (א')
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
                    
        with row1_col_left: # העמודה השמאלית (ב')
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
        
        with row2_col_right: # העמודה הימנית (ג')
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
                    
        with row2_col_left: # העמודה השמאלית (ד')
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
