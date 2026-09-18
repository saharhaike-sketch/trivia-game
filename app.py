import random
import streamlit as st

# סולם הזכיות
PRIZE_LADDER = [
    100, 200, 300, 500, 1000, 2000, 4000, 8000,
    16000, 32000, 64000, 125000, 250000, 500000, 1000000,
]

# מאגר השאלות
QUESTIONS = [
    {
        "question": "מהו בעל החיים היבשתי הגדול בעולם?",
        "options": ["קרנף רחב-שפה", "פיל סוואנה אפריקאי", "היפופוטם", "ג'ירפה"],
        "answer": 1,
    },
    {
        "question": "באיזו שנה הוקמה מדינת ישראל?",
        "options": ["1945", "1948", "1950", "1947"],
        "answer": 1,
    },
    {
        "question": "כמה צבעים יש בקשת בענן?",
        "options": ["5", "6", "7", "8"],
        "answer": 2,
    },
    {
        "question": "מי כתב את המחזה 'רומיאו ויוליה'?",
        "options": ["ויליאם שייקספיר", "שארל בודלר", "ויקטור הוגו", "מולייר"],
        "answer": 0,
    },
    {
        "question": "מהי הבירה של אוסטרליה?",
        "options": ["סידני", "מלבורן", "קנברה", "בריזביין"],
        "answer": 2,
    },
    {
        "question": "מהו היסוד הכימי הנפוץ ביותר ביקום?",
        "options": ["חמצן", "פחמן", "הליום", "מימן"],
        "answer": 3,
    },
    {
        "question": "באיזה יבשת נמצא מדבר סהרה?",
        "options": ["אסיה", "אפריקה", "דרום אמריקה", "אוסטרליה"],
        "answer": 1,
    },
    {
        "question": "כמה שחקנים יש בקבוצת כדורגל על המגרש (מצד אחד)?",
        "options": ["10", "11", "12", "9"],
        "answer": 1,
    },
    {
        "question": "מי צייר את המונה ליזה?",
        "options": ["וינסנט ואן גוך", "פבלו פיקאסו", "לאונרדו דה וינצ'י", "קלוד מונה"],
        "answer": 2,
    },
    {
        "question": "מהו הר געש פעיל באיטליה?",
        "options": ["ווזוב", "פוג'י", "קלימנג'רו", "סנט הלנס"],
        "answer": 0,
    },
    {
        "question": "כמה עצמות יש בגוף האדם הבוגר (בקירוב)?",
        "options": ["150", "206", "300", "450"],
        "answer": 1,
    },
    {
        "question": "מהו המרחק בקירוב בין כדור הארץ לשמש?",
        "options": ["15 מיליון ק\"מ", "150 מיליון ק\"מ", "1.5 מיליארד ק\"מ", "1.5 מיליון ק\"מ"],
        "answer": 1,
    },
    {
        "question": "איזו מדינה היא האי הגדול ביותר בעולם מבחינת שטח?",
        "options": ["מדגסקר", "גרינלנד", "איסלנד", "בריטניה"],
        "answer": 1,
    },
    {
        "question": "באיזו שנה נחת האדם הראשון על הירח?",
        "options": ["1965", "1969", "1972", "1967"],
        "answer": 1,
    },
    {
        "question": "מהי השפה המדוברת ביותר בעולם מבחינת דוברים שפת אם?",
        "options": ["אנגלית", "ספרדית", "מנדרינית (סינית)", "הינדי"],
        "answer": 2,
    },
]

st.set_page_config(page_title="מי רוצה להיות מיליונר", page_icon="💰", layout="wide")

if "game_state" not in st.session_state:
  st.session_state.game_state = "start"
  st.session_state.current_question = 0
  st.session_state.lifelines = {"5050": True, "friend": True}
  st.session_state.hidden_options = []
  st.session_state.friend_advice = ""

def reset_game():
  st.session_state.game_state = "playing"
  st.session_state.current_question = 0
  st.session_state.lifelines = {"5050": True, "friend": True}
  st.session_state.hidden_options = []
  st.session_state.friend_advice = ""

st.title("💰 מי רוצה להיות מיליונר?")
st.markdown("---")

if st.session_state.game_state == "start":
  st.subheader("ברוכים הבאים למשחק הטריוויה האישי שלך!")
  st.write("ענו נכונה על 15 שאלות, טיפסו בסולם הזכיות והגיעו לפרס הגדול של מיליון שקלים.")
  if st.button("התחל במשחק", type="primary", use_container_width=True):
    reset_game()
    st.rerun()

elif st.session_state.game_state == "playing":
  q_idx = st.session_state.current_question
  current_q = QUESTIONS[q_idx]

  col_l1, col_l2, col_info = st.columns([1, 1, 2])
  with col_l1:
    if st.session_state.lifelines["5050"]:
      if st.button("✂️ 50:50", use_container_width=True):
        correct = current_q["answer"]
        wrong_indices = [i for i in range(4) if i != correct]
        st.session_state.hidden_options = random.sample(wrong_indices, 2)
        st.session_state.lifelines["5050"] = False
        st.rerun()
    else:
      st.button("✂️ 50:50 (נוצל)", disabled=True, use_container_width=True)

  with col_l2:
    if st.session_state.lifelines["friend"]:
      if st.button("📞 עזרה מחבר", use_container_width=True):
        correct = current_q["answer"]
        suggested = correct if random.random() < 0.8 else random.choice([i for i in range(4) if i != correct])
        letters = ["א'", "ב'", "ג'", "ד'"]
        st.session_state.friend_advice = f"החבר שלך חושב שהתשובה הנכונה היא: {letters[suggested]} ({current_q['options'][suggested]})"
        st.session_state.lifelines["friend"] = False
        st.rerun()
    else:
      st.button("📞 עזרה מחבר (נוצל)", disabled=True, use_container_width=True)

  with col_info:
    current_prize = PRIZE_LADDER[q_idx - 1] if q_idx > 0 else 0
    st.markdown(f"**שאלה מספר {q_idx + 1} מתוך {len(QUESTIONS)}**<br>סכום מובטח כרגע: **{current_prize:,} ₪**", unsafe_allow_html=True)

  if st.session_state.friend_advice:
    st.info(st.session_state.friend_advice)

  st.markdown("---")
  st.subheader(f"שאלה {q_idx + 1}: {current_q['question']}")
  st.markdown("")

  col1, col2 = st.columns(2)
  letters = ["א'", "ב'", "ג'", "ד'"]

  for i, option in enumerate(current_q["options"]):
    target_col = col1 if i % 2 == 0 else col2
    with target_col:
      if i in st.session_state.hidden_options:
        st.button(f"{letters[i]}. (הוסתר)", disabled=True, key=f"opt_{i}", use_container_width=True)
      else:
        if st.button(f"{letters[i]}. {option}", key=f"opt_{i}", use_container_width=True):
          if i == current_q["answer"]:
            st.session_state.hidden_options = []
            st.session_state.friend_advice = ""
            if q_idx + 1 >= len(QUESTIONS):
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
  if st.button("שחק שוב", type="primary"):
    reset_game()
    st.rerun()

elif st.session_state.game_state == "lost":
  st.error("❌ טעות! תשובה שגויה.")
  q_idx = st.session_state.current_question
  final_prize = 32000 if q_idx >= 10 else 1000 if q_idx >= 5 else 0
  st.warning(f"הפסדת את המשחק, אך סיימת עם סכום זכייה של: **{final_prize:,} ₪**")
  if st.button("נסה שוב", type="primary"):
    reset_game()
    st.rerun()