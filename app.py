# מבצע הגות צבאית – משחק למידה (Streamlit)
# קובץ יחיד: כל המשחק נמצא בתוך המשתנה GAME_HTML שבתחתית הקובץ.
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


def show_game():
    if hasattr(st, "iframe"):  # גרסאות חדשות של Streamlit
        st.iframe(GAME_HTML, height=1600)
    else:  # גרסאות ישנות
        import streamlit.components.v1 as components
        components.html(GAME_HTML, height=1600, scrolling=True)


GAME_HTML = r'''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>מבצע הגות צבאית – משחק למידה</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;700;800&family=Frank+Ruhl+Libre:wght@700;900&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#070d18; --bg2:#0e1a2e; --card:#111f36; --card2:#162a48; --line:#24395c;
  --gold:#e0b04a; --gold2:#f5d27a; --ink:#eef2f8; --mute:#93a3bd;
  --ok:#3fbf7f; --bad:#e8585a; --blue:#4f8de0; --sun:#e0703c; --clz:#6f8ff0;
  --r:16px;
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{min-height:100%}
body{
  font-family:Heebo,system-ui,sans-serif; color:var(--ink); line-height:1.55;
  background:
    radial-gradient(1200px 600px at 80% -10%, rgba(224,176,74,.13), transparent 60%),
    radial-gradient(900px 600px at -10% 110%, rgba(79,141,224,.12), transparent 60%),
    var(--bg);
  background-attachment:fixed;
}
body::before{content:"";position:fixed;inset:0;pointer-events:none;opacity:.5;
  background-image:linear-gradient(rgba(255,255,255,.025) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.025) 1px,transparent 1px);
  background-size:42px 42px}
button{font:inherit;color:inherit;cursor:pointer;border:0;background:none}
input{font:inherit}
.wrap{max-width:1080px;margin:0 auto;padding:18px 16px 60px;position:relative}
.top{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:18px}
.brand{display:flex;align-items:center;gap:10px;font-weight:800;letter-spacing:.2px}
.brand .logo{width:38px;height:38px;border-radius:10px;display:grid;place-items:center;
  background:linear-gradient(135deg,var(--gold),#a5741c);color:#1a1205;font-size:20px;box-shadow:0 4px 14px rgba(224,176,74,.35)}
.brand small{display:block;font-weight:500;color:var(--mute);font-size:12px}
.chips{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.chip{background:var(--card);border:1px solid var(--line);border-radius:999px;padding:6px 12px;font-size:13px;display:flex;gap:6px;align-items:center;white-space:nowrap}
.chip b{color:var(--gold2)}
.iconbtn{width:36px;height:36px;border-radius:50%;background:var(--card);border:1px solid var(--line);display:grid;place-items:center}
.iconbtn:hover{border-color:var(--gold)}
h1,.display{font-family:"Frank Ruhl Libre",serif}
.hero{padding:26px 24px;border-radius:22px;border:1px solid var(--line);margin-bottom:18px;position:relative;overflow:hidden;
  background:linear-gradient(135deg,rgba(224,176,74,.10),rgba(79,141,224,.06) 60%,transparent),var(--bg2)}
.hero h1{font-size:clamp(30px,5vw,46px);line-height:1.1;margin-bottom:8px}
.hero h1 span{color:var(--gold)}
.hero p{color:var(--mute);max-width:640px}
.hero .vs{position:absolute;left:22px;top:50%;transform:translateY(-50%);font-size:64px;opacity:.9;display:flex;gap:6px;align-items:center}
.hero .vs i{font-style:normal;font-size:18px;color:var(--gold);font-weight:800;font-family:Heebo}
@media(max-width:720px){.hero .vs{display:none}}
.namebox{display:flex;gap:8px;margin-top:16px;flex-wrap:wrap;align-items:center}
.namebox input{background:var(--bg);border:1px solid var(--line);border-radius:10px;padding:9px 12px;color:var(--ink);min-width:200px}
.namebox input:focus{outline:none;border-color:var(--gold)}
.rankcard{display:flex;align-items:center;gap:14px;margin-top:16px;flex-wrap:wrap}
.rankbadge{font-size:13px;color:var(--mute)}
.rankbadge b{font-size:18px;color:var(--gold2);display:block}
.xpbar{flex:1;min-width:180px;max-width:380px;height:10px;border-radius:99px;background:#0a1424;border:1px solid var(--line);overflow:hidden}
.xpbar i{display:block;height:100%;background:linear-gradient(90deg,#a5741c,var(--gold2));border-radius:99px;transition:width .6s}
.section-title{font-size:15px;color:var(--mute);font-weight:700;margin:22px 2px 10px;letter-spacing:.3px}
.modes{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:12px}
.mode{text-align:right;background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:18px;transition:.2s;position:relative;overflow:hidden}
.mode:hover{transform:translateY(-3px);border-color:var(--gold);box-shadow:0 10px 30px rgba(0,0,0,.35)}
.mode .em{font-size:30px;margin-bottom:8px;display:block}
.mode h3{font-size:18px;margin-bottom:4px}
.mode p{font-size:13.5px;color:var(--mute)}
.mode .tag{position:absolute;top:14px;left:14px;font-size:11px;font-weight:700;padding:3px 8px;border-radius:99px;background:rgba(224,176,74,.15);color:var(--gold2)}
.mode.feature{grid-column:span 2;background:linear-gradient(135deg,#1b2f52,#111f36)}
@media(max-width:560px){.mode.feature{grid-column:span 1}}
.mode .best{margin-top:10px;font-size:12px;color:var(--gold2)}
.topics{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:10px}
.topic{display:flex;align-items:center;gap:12px;text-align:right;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:12px 14px;transition:.2s}
.topic:hover{border-color:var(--gold)}
.ring{--p:0;width:44px;height:44px;border-radius:50%;flex:none;display:grid;place-items:center;font-size:11px;font-weight:800;
  background:conic-gradient(var(--gold) calc(var(--p)*1%),#1d2e4a 0)}
.ring span{width:34px;height:34px;border-radius:50%;background:var(--card);display:grid;place-items:center}
.topic .t{font-size:14px;font-weight:700;line-height:1.3}
.topic .s{font-size:12px;color:var(--mute)}
.panel{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:22px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;border-radius:12px;padding:11px 20px;font-weight:700;
  background:linear-gradient(135deg,var(--gold),#b8862b);color:#1a1205;transition:.15s;box-shadow:0 6px 18px rgba(224,176,74,.25)}
.btn:hover{filter:brightness(1.08);transform:translateY(-1px)}
.btn.ghost{background:transparent;color:var(--ink);border:1px solid var(--line);box-shadow:none}
.btn.ghost:hover{border-color:var(--gold)}
.btn:disabled{opacity:.4;cursor:not-allowed;transform:none}
.row{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.spacer{flex:1}
/* game layout */
.game{display:grid;grid-template-columns:1fr 230px;gap:16px}
@media(max-width:860px){.game{grid-template-columns:1fr}.ladder{order:-1}}
.qhead{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:14px}
.pill{font-size:12.5px;padding:5px 11px;border-radius:99px;background:#0a1424;border:1px solid var(--line);color:var(--mute)}
.pill.gold{color:var(--gold2);border-color:rgba(224,176,74,.5)}
.qbox{background:linear-gradient(180deg,#14284a,#0f1d36);border:1px solid #2c4672;border-radius:18px;padding:22px;margin-bottom:16px;position:relative}
.qbox .qt{font-size:clamp(18px,2.4vw,23px);font-weight:700;line-height:1.45}
.qbox .topicname{font-size:12px;color:var(--gold2);margin-bottom:8px;font-weight:700}
.opts{display:grid;grid-template-columns:1fr 1fr;gap:10px}
@media(max-width:700px){.opts{grid-template-columns:1fr}}
.opt{display:flex;gap:12px;align-items:flex-start;text-align:right;background:#0c1830;border:1.5px solid #2c4672;border-radius:14px;padding:13px 14px;transition:.15s;font-size:15px;min-height:58px}
.opt:hover:not(:disabled){border-color:var(--gold);background:#12233f}
.opt .L{flex:none;width:28px;height:28px;border-radius:50%;display:grid;place-items:center;font-weight:800;font-size:14px;background:#1b2f52;color:var(--gold2)}
.opt.sel{border-color:var(--gold);background:#2a2412}
.opt.ok{border-color:var(--ok);background:rgba(63,191,127,.14)}
.opt.ok .L{background:var(--ok);color:#06210f}
.opt.bad{border-color:var(--bad);background:rgba(232,88,90,.13)}
.opt.bad .L{background:var(--bad);color:#2a0607}
.opt.hide{visibility:hidden}
.opt:disabled{cursor:default}
.opt.dim{opacity:.45}
.lifelines{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14px}
.life{display:flex;align-items:center;gap:6px;padding:8px 14px;border-radius:99px;border:1px solid var(--line);background:var(--card);font-weight:700;font-size:14px}
.life:hover:not(:disabled){border-color:var(--gold)}
.life:disabled{opacity:.35;text-decoration:line-through;cursor:not-allowed}
.feedback{margin-top:16px;border-radius:16px;padding:16px 18px;border:1px solid var(--line);background:#0b172b;animation:pop .25s ease}
.feedback.ok{border-color:rgba(63,191,127,.6)}
.feedback.bad{border-color:rgba(232,88,90,.6)}
.feedback h4{font-size:17px;margin-bottom:6px}
.feedback.ok h4{color:var(--ok)} .feedback.bad h4{color:var(--bad)}
.feedback p{color:#cdd6e6;font-size:15px}
.feedback .why{margin-top:6px}
.hintbox{margin-bottom:14px;border-radius:14px;padding:12px 14px;background:rgba(79,141,224,.1);border:1px solid rgba(79,141,224,.4);font-size:14.5px;animation:pop .25s}
.aud{display:flex;gap:10px;align-items:flex-end;height:110px;margin-top:8px}
.aud div{flex:1;display:flex;flex-direction:column;align-items:center;gap:4px;font-size:12px;height:100%;justify-content:flex-end}
.aud b{width:100%;max-width:46px;border-radius:6px 6px 0 0;background:linear-gradient(180deg,var(--blue),#2a5aa0);transition:height .8s}
.ladder{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:12px;align-self:start}
.ladder h4{font-size:13px;color:var(--mute);margin:2px 6px 8px}
.rung{display:flex;justify-content:space-between;padding:4px 10px;border-radius:8px;font-size:13.5px;color:var(--mute);font-variant-numeric:tabular-nums}
.rung.safe{color:var(--ink);font-weight:700}
.rung.done{color:var(--ok)}
.rung.cur{background:linear-gradient(90deg,var(--gold),#b8862b);color:#1a1205;font-weight:800}
@media(max-width:860px){.ladder .rung:not(.cur){display:none}.ladder h4{display:none}.ladder{padding:6px}}
/* blitz */
.blitz-card{min-height:170px;display:grid;place-items:center;text-align:center;font-size:clamp(19px,2.8vw,26px);font-weight:700;padding:26px;border-radius:20px;
  background:linear-gradient(180deg,#14284a,#0f1d36);border:1px solid #2c4672;margin:12px 0 14px;animation:pop .2s}
.blitz-card.flash-ok{border-color:var(--ok);box-shadow:0 0 0 3px rgba(63,191,127,.25)}
.blitz-card.flash-bad{border-color:var(--bad);box-shadow:0 0 0 3px rgba(232,88,90,.25)}
.who{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
@media(max-width:560px){.who{grid-template-columns:repeat(2,1fr)}}
.whob{padding:14px 8px;border-radius:14px;border:1.5px solid var(--line);background:var(--card);font-weight:800;font-size:15px;transition:.12s}
.whob:hover{border-color:var(--gold);transform:translateY(-2px)}
.whob .k{display:block;font-size:11px;color:var(--mute);font-weight:500}
.whob .e{font-size:22px;display:block}
.timerbar{height:8px;border-radius:99px;background:#0a1424;overflow:hidden;border:1px solid var(--line)}
.timerbar i{display:block;height:100%;background:linear-gradient(90deg,var(--bad),var(--gold));transition:width .25s linear}
.big{font-size:42px;font-weight:800;color:var(--gold2);font-family:"Frank Ruhl Libre",serif;line-height:1}
.combo{color:var(--sun);font-weight:800}
.lastfb{min-height:26px;font-size:14px;color:var(--mute);text-align:center}
/* exam */
.qgrid{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}
.qdot{width:32px;height:32px;border-radius:8px;border:1px solid var(--line);background:#0c1830;font-size:12.5px;font-weight:700;color:var(--mute)}
.qdot.ans{background:#1b2f52;color:var(--ink)}
.qdot.flag{border-color:var(--sun);color:var(--sun)}
.qdot.cur{outline:2px solid var(--gold);outline-offset:1px}
.qdot.ok{background:rgba(63,191,127,.25);color:var(--ok);border-color:var(--ok)}
.qdot.bad{background:rgba(232,88,90,.2);color:var(--bad);border-color:var(--bad)}
/* results */
.score{display:flex;gap:14px;flex-wrap:wrap;margin:14px 0}
.stat{flex:1;min-width:140px;background:#0b172b;border:1px solid var(--line);border-radius:14px;padding:14px}
.stat .v{font-size:28px;font-weight:800;color:var(--gold2);font-family:"Frank Ruhl Libre",serif}
.stat .k{font-size:12.5px;color:var(--mute)}
.bars .b{display:grid;grid-template-columns:minmax(120px,240px) 1fr 46px;gap:10px;align-items:center;font-size:13.5px;margin:7px 0}
.bars .track{height:10px;background:#0a1424;border-radius:99px;overflow:hidden;border:1px solid var(--line)}
.bars .track i{display:block;height:100%;border-radius:99px}
details.rev{background:#0b172b;border:1px solid var(--line);border-radius:12px;margin:8px 0;padding:0 14px}
details.rev summary{cursor:pointer;padding:12px 0;font-weight:600;list-style:none;display:flex;gap:10px}
details.rev summary::-webkit-details-marker{display:none}
details.rev .body{padding:0 0 14px;font-size:14.5px;color:#cdd6e6}
details.rev .body p{margin:5px 0}
.okc{color:var(--ok)} .badc{color:var(--bad)} .goldc{color:var(--gold2)} .mutec{color:var(--mute)}
/* flashcards */
.flip{perspective:1200px;cursor:pointer;margin:14px 0}
.flip .inner{position:relative;min-height:260px;transition:transform .55s;transform-style:preserve-3d}
.flip.on .inner{transform:rotateY(180deg)}
.face{position:absolute;inset:0;backface-visibility:hidden;border-radius:20px;padding:26px;display:flex;flex-direction:column;justify-content:center;gap:10px;
  background:linear-gradient(180deg,#14284a,#0f1d36);border:1px solid #2c4672}
.face.back{transform:rotateY(180deg);background:linear-gradient(180deg,#1c2a17,#0f1d1a);border-color:rgba(63,191,127,.5)}
.face .q{font-size:clamp(18px,2.6vw,23px);font-weight:700}
.face .a{font-size:17px;font-weight:700;color:var(--ok)}
.face .x{color:#cdd6e6;font-size:14.5px}
.face .tap{font-size:12px;color:var(--mute);position:absolute;bottom:12px;left:0;right:0;text-align:center}
.modal{position:fixed;inset:0;background:rgba(3,6,12,.75);display:grid;place-items:center;z-index:50;padding:16px;animation:fade .2s}
.modal .panel{max-width:520px;width:100%}
.toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%);background:var(--card2);border:1px solid var(--gold);padding:10px 18px;border-radius:12px;z-index:60;animation:pop .2s;font-weight:600}
.kbd{font-size:11px;color:var(--mute);margin-top:12px;text-align:center}
.cheat{width:100%;border-collapse:collapse;font-size:14px}
.cheat th,.cheat td{padding:9px 10px;border-bottom:1px solid var(--line);text-align:right;vertical-align:top}
.cheat th{color:var(--gold2);font-size:13px}
.cheat td:first-child{font-weight:700;white-space:nowrap}
canvas#fx{position:fixed;inset:0;pointer-events:none;z-index:70}
@keyframes pop{from{transform:scale(.97);opacity:0}to{transform:none;opacity:1}}
@keyframes fade{from{opacity:0}}
@keyframes shake{20%,60%{transform:translateX(-6px)}40%,80%{transform:translateX(6px)}}
.shake{animation:shake .35s}
@media(max-width:560px){.brand small{display:none}.chip{padding:5px 9px}}
footer{margin-top:40px;text-align:center;color:var(--mute);font-size:12px}
</style>
</head>
<body>
<canvas id="fx"></canvas>
<div class="wrap">
  <div class="top">
    <button class="brand" data-a="home" aria-label="מסך הבית">
      <div class="logo">⚔️</div>
      <div>מבצע הגות צבאית<small>מבוא להיסטוריה והגות צבאית</small></div>
    </button>
    <div class="chips" id="chips"></div>
  </div>
  <main id="app"></main>
  <footer>מבוסס על 13 שיעורי הקורס ועל סיכומי המבחן · ההתקדמות נשמרת בדפדפן שלך בלבד</footer>
</div>
<script>
// מאגר שאלות – מבוא להיסטוריה והגות צבאית (על בסיס 13 שיעורי ד״ר עופר ישראלי)
// QUESTIONS: [נושא, קושי 1-3, שאלה, [נכונה, מסיח, מסיח, מסיח], רמז, הסבר] – התשובה הנכונה ראשונה; המשחק מערבב.
// WHO: [היגד, מפתח הוגה, הסבר]. S=סון טסו C=קלאוזביץ B=שניהם M=מאו J=ז׳ומיני MA=מקיאוולי
const TOPICS = {
 "books": {
  "name": "ההוגים והספרים",
  "icon": "📜"
 },
 "nature": {
  "name": "מהי מלחמה – הסכמות והבדלים",
  "icon": "⚖️"
 },
 "policy": {
  "name": "מלחמה, מדיניות ורמות המלחמה",
  "icon": "🏛️"
 },
 "theory": {
  "name": "תיאוריה מול מעשה, חיכוך והערכה נטו",
  "icon": "🌫️"
 },
 "moral": {
  "name": "גורמים נפשיים, אופי המלחמה והשילוש",
  "icon": "🔺"
 },
 "cog": {
  "name": "מרכזי כובד",
  "icon": "🎯"
 },
 "win": {
  "name": "ניצחון, מכפילי כוח וריכוז",
  "icon": "♟️"
 },
 "cont": {
  "name": "המשכיות, המתנה ונקודת השיא",
  "icon": "📈"
 },
 "end": {
  "name": "סיום המלחמה",
  "icon": "🕊️"
 },
 "intel": {
  "name": "הונאה, הפתעה ומודיעין",
  "icon": "🕵️"
 },
 "lead": {
  "name": "מנהיגות צבאית",
  "icon": "🎖️"
 }
};
const QUESTIONS = [
["books",1,"מה שמו של חיבורו של סון טסו, ומתי בערך נכתב?",["״אמנות המלחמה״, בערך 500 לפנה״ס","״על המלחמה״, בערך 500 לפנה״ס","״אמנות המלחמה״, בשנת 1832","״הנסיך״, בערך 300 לפנה״ס"],"שם הספר זהה לשם ספרו של ז׳ומיני.","סון טסו כתב את ״אמנות המלחמה״ בסין, בערך 500 לפנה״ס. ״על המלחמה״ הוא של קלאוזביץ (1832)."],
["books",1,"מה שמו של חיבורו של קלאוזביץ, ומתי פורסם?",["״על המלחמה״, 1832","״אמנות המלחמה״, 1832","״על המלחמה״, 1914","״תורת הקרב״, 1806"],"קלאוזביץ היה קצין פרוסי בתקופת נפוליאון.","״על המלחמה״ של קלאוזביץ פורסם ב-1832 והוא חיבור של כמעט 600 עמודים."],
["books",2,"איזה הוגה כתב גם הוא ספר בשם ״אמנות המלחמה״, בנוסף לסון טסו?",["ז׳ומיני","קלאוזביץ","מאו טסה-טונג","הנטינגטון"],"הוגה מהמאה ה-19 שהיה מודע מאוד לחשיבות הטכנולוגיה.","גם לז׳ומיני ספר בשם ״אמנות המלחמה״. זו שאלה שקל להתבלבל בה – שני הוגים, אותו שם ספר."],
["books",2,"מה ההבדל בסגנון הכתיבה בין ״אמנות המלחמה״ ל״על המלחמה״?",["סון טסו כתב מסה תמציתית של אמרות בלי הסבר; קלאוזביץ כתב חיבור ארוך ומנומק שצריך לקרוא כמה פעמים","סון טסו כתב חיבור ארוך ומנומק; קלאוזביץ כתב אוסף קצר של אמרות ופתגמים צבאיים","שניהם כתבו מסות קצרות של פחות מ-40 עמודים, אך קלאוזביץ הוסיף להן נספחים היסטוריים","שניהם כתבו חיבורים ארוכים, אך סון טסו נמנע לחלוטין משימוש במטפורות ובדימויים"],"פחות מ-40 עמודים מול כמעט 600.","״אמנות המלחמה״ – פחות מ-40 עמודים בתרגום לאנגלית, אמרות קצרות. ״על המלחמה״ – כמעט 600 עמודים, ויש לקרוא אותו מתחילתו ועד סופו כמה פעמים."],
["books",2,"משל ״התפוח הנופל״ בא להמחיש הבדל בין סון טסו לקלאוזביץ. מהו?",["סון טסו אומר שהתפוח נופל (עובדה), וקלאוזביץ מסביר מדוע הוא נופל (כוח הכבידה – הסבר תיאורטי)","סון טסו מסביר מדוע התפוח נופל, וקלאוזביץ מסתפק בקביעה שהוא נופל תמיד","שניהם מסבירים מדוע התפוח נופל, אך כל אחד נותן הסבר מדעי אחר לתופעה","סון טסו טוען שהתפוח לא תמיד נופל, וקלאוזביץ טוען שהוא נופל לפי חוק קבוע"],"מי נותן את ה״למה״?","לכן מקורא ״אמנות המלחמה״ נדרשת בעיקר הבנת המסקנות, ומקורא ״על המלחמה״ נדרש תהליך למידה."],
["books",2,"מהן שתי הסיבות שבגללן ספרים עתיקים כמו של סון טסו וקלאוזביץ עדיין רלוונטיים?",["ההיגיון של הטבע האנושי והפעילות הפוליטית לא השתנה, והלוחמה המודרנית מורכבת מכדי לכתוב תיאוריה כוללת חדשה בכרך אחד","הטכנולוגיה הצבאית לא השתנתה מהותית מאז, והצבאות המודרניים עדיין משתמשים באותן טקטיקות בדיוק","הספרים תורגמו לשפות רבות, ולכן הם הספרים היחידים שזמינים לכל צבאות העולם באותה מידה","הם נכתבו בידי מצביאים שניצחו בכל מלחמותיהם, ולכן אי אפשר להפריך את מסקנותיהם"],"אחת קשורה לאדם, השנייה למורכבות של היום.","(1) ההיגיון של הטבע האנושי ושל הפעילות הפוליטית לא השתנה; (2) המורכבות של הלוחמה המודרנית הפכה בניית אסטרטגיה כוללת חדשה לבלתי אפשרית."],
["books",3,"לפי הקורס, האם קיימת גישה ״מערבית״ וגישה ״מזרחית״ ייחודיות למלחמה?",["לא – קיימים רק ביטויים יעילים או לא יעילים, רציונליים או לא רציונליים, של מדיניות ואסטרטגיה","כן – הגישה המערבית מבוססת על כוח, והמזרחית מבוססת על הונאה, ואין ביניהן נקודות השקה","כן – אך רק ברמה הטקטית; ברמה האסטרטגית אין הבדל בין המערב למזרח","לא – כי שני הספרים נכתבו בהשפעה ישירה זה של זה ומתוך אותה מסורת"],"ההיגיון של המלחמה בשני הספרים אחיד.","שני הספרים משקפים את ההקשר התרבותי שבו נכתבו, אבל ההיגיון הרציונלי של המלחמה בהם אחיד – אין גישה ״מערבית״ או ״מזרחית״ ייחודית."],
["books",2,"מה הייתה מחלוקתו של מאו טסה-טונג עם קלאוזביץ בנוגע לנשק?",["מאו הזהיר מהסתמכות יתר על גורמים חומריים: ״אנשים, לא עצמים, הם המכריעים״","מאו טען שהנשק הוא הגורם המכריע במלחמה, וקלאוזביץ טען שרק המורל קובע","מאו טען שאין לנשק כל חשיבות, וקלאוזביץ טען שהנשק חשוב יותר מהאנשים","מאו וקלאוזביץ הסכימו לחלוטין, והמחלוקת הייתה בעצם בין מאו לסון טסו"],"מאו כתב בעיצומו של העידן התעשייתי.","מאו: כלי נשק הם גורם חשוב אך לא מכריע – ״אנשים, לא עצמים, הם המכריעים״. המחלוקת משמשת אזהרה בתקופה שבה נוטים לראות בטכנולוגיה חזות הכול."],
["books",2,"במה שונה ז׳ומיני מקלאוזביץ ביחס לטכנולוגיה?",["ז׳ומיני היה מודע מאוד לחשיבות החימוש המודרני וצפה שתהיה לו השפעה מכרעת יותר; קלאוזביץ ראה את השינויים העמוקים כמדיניים וחברתיים","ז׳ומיני התעלם לחלוטין מהטכנולוגיה, ואילו קלאוזביץ ראה בה את הגורם המכריע בכל מלחמה","שניהם ראו בטכנולוגיה את הגורם המכריע, אך ז׳ומיני התמקד בצי וקלאוזביץ ביבשה","ז׳ומיני טען שטכנולוגיה מזיקה לצבא, וקלאוזביץ טען שהיא מחליפה את הצורך במפקד"],"מה שז׳ומיני זיהה היה בעצם תחילת המהפכה התעשייתית.","ז׳ומיני הבחין באופי הדינמי של ההמצאות הצבאיות. קלאוזביץ האמין (אולי בצדק לגבי תקופתו) שהשינויים העמוקים במלחמה היו מדיניים וחברתיים, לא חומריים."],
["books",3,"מה למדו ממלחמת המפרץ (1991) על מקומה של הטכנולוגיה?",["טכנולוגיה עדיפה היא במקרה הטוב תנאי הכרחי, אך לעולם אינה תנאי מספיק לניצחון","טכנולוגיה עדיפה היא תנאי מספיק לניצחון, גם בלי תכנון מדיני או תמיכה ציבורית","הטכנולוגיה אינה תורמת דבר לניצחון, והמלחמה הוכרעה רק בזכות מורל הלוחמים","הטכנולוגיה מכריעה במלחמות קצרות בלבד, ובמלחמות ממושכות היא הגורם היחיד"],"ויטנאם וגרמניה הן דוגמאות נוספות.","הניצחון ב-1991 הושג בראש ובראשונה בזכות תכנון והכנה פוליטיים נבונים. גם הניצחונות המוקדמים של גרמניה בשתי מלחמות העולם נבעו מתכנון ומנהיגות, לא רק מטכנולוגיה."],
["nature",1,"מהי הגדרת המלחמה של קלאוזביץ?",["מעשה של כוח שמטרתו לאכוף על האויב לעשות כרצוננו","מאבק בין שני צבאות שמטרתו השמדה מוחלטת של אחד מהם","פעילות דיפלומטית שבה משתמשים באיומים במקום במשא ומתן","תופעה טבעית שאין לה קשר למדיניות ולשיקולים רציונליים"],"יש בה ״כוח״ ו״רצון״.","״המלחמה היא מעשה של כוח שמטרתו לאכוף על האויב לעשות כרצוננו״. היא מכשיר של המדיניות, ורציונלית רק אם יש לה מטרה מדינית."],
["nature",1,"לפי קלאוזביץ, מתי המלחמה היא פעילות רציונלית?",["כאשר יש לה מטרה מדינית – כי היא מכשיר של המדיניות","כאשר הצבא מצליח להשמיד את כל כוחות האויב בקרב אחד","כאשר המלחמה מתנהלת לפי חוקים מדעיים קבועים ומוכחים","כאשר ההחלטה עליה מתקבלת בידי המפקדים הצבאיים בלבד"],"המלחמה כ״המשך המדיניות באמצעים אחרים״.","המלחמה היא ההמשך של המדיניות באמצעים אחרים, ולכן היא רציונלית רק כשהיא משרתת מטרה מדינית."],
["nature",2,"מה עמדתם המשותפת של סון טסו וקלאוזביץ בשאלה אם המלחמה היא אמנות או מדע?",["המלחמה היא אמנות; לכל בעיה יש פתרונות נכונים רבים שמגיעים אליהם בדמיון, ביצירתיות ובאינטואיציה","המלחמה היא מדע מדויק; לכל בעיה צבאית יש פתרון אופטימלי יחיד שאפשר לחשב מראש","סון טסו רואה בה מדע וקלאוזביץ רואה בה אמנות, ולכן אין ביניהם הסכמה בנושא","שניהם נמנעו מלהכריע בשאלה, כי ראו בה שאלה פילוסופית שאינה רלוונטית לשדה הקרב"],"״באמנות המלחמה אין כללים קבועים״.","שניהם רואים במלחמה אמנות (קלאוזביץ – אמנות עם היבטים מדעיים מסוימים). מי שרצה לבנות תיאוריה מדעית היה ז׳ומיני."],
["nature",2,"איזה הוגה רצה לבנות תיאוריה מדעית של המלחמה ומעולם לא הודה במלואו שהיא אמנות?",["ז׳ומיני","סון טסו","קלאוזביץ","מקיאוולי"],"הוא גם ייחס חשיבות רבה לטכנולוגיה.","ז׳ומיני נע בין רצונו בתיאוריה מדעית לבין ההכרה שהמלחמה היא פעולה יצירתית. בסוף נטה להודות שזו אמנות, אך לא הכיר בכך באופן מלא."],
["nature",2,"מדוע לפי סון טסו וקלאוזביץ אי אפשר לנסח תיאוריה ״פוזיטיבית״ של המלחמה?",["המורכבות העצומה של המלחמה, ו״עקרונות המלחמה״ תקפים רק באופן יחסי ולא מוחלט","כי המלחמה פשוטה מדי ואין בה מספיק משתנים כדי לבנות ממנה תיאוריה","כי אין בידי ההוגים מספיק נתונים היסטוריים, אך בעתיד הדבר יתאפשר","כי כל תיאוריה צבאית נאסרת לפרסום בידי הדרג המדיני מטעמי סודיות"],"״במלחמה יכולים לחול מאה שינויים בכל צעד״.","המורכבות האינסופית לא מאפשרת תיאוריה פוזיטיבית; ״חוקי״ המלחמה הם בעלי תוקף יחסי בלבד. סון טסו: ״כמו שלמים אין צורה קבועה, כך אין תנאים קבועים במלחמה״."],
["nature",2,"במה מסכימים סון טסו וקלאוזביץ לגבי היחס בין הדרג המדיני למפקד בשטח?",["המלחמה חייבת להיות בשליטת הדרג המדיני, אך למפקד בשטח צריך לתת חופש פעולה מספיק","המפקד בשטח מחליט על הכול, והדרג המדיני נכנס לתמונה רק בסיום המלחמה","הדרג המדיני צריך לנהל גם את הטקטיקה בשדה הקרב, בלי חופש פעולה למפקד","שניהם קבעו קריטריונים מפורטים למקרים שבהם מותר למפקד להפר פקודה"],"שימו לב – יש כאן מלכודת נפוצה לגבי ״קריטריונים״.","שניהם תומכים בעליונות המדיניות ובחופש פעולה למפקד – אבל אף אחד מהם לא פיתח קריטריונים לנסיבות שבהן מפקד רשאי להתעלם מפקודות."],
["nature",2,"איזו מהטענות הבאות אינה עמדה משותפת לסון טסו ולקלאוזביץ?",["יש להשתמש בכוח במידה מועטה ככל האפשר ורק כאמצעי אחרון","המלחמה צריכה להיות קצרה ומכרעת ככל האפשר","תמיכת העם הכרחית להצלחה במלחמה","המפתח הוא עדיפות יחסית בנקודת ההכרעה ולא יתרון מספרי מוחלט"],"חפשו את העמדה של אחד מהם בלבד.","השימוש בכוח רק כמוצא אחרון ובמידה מזערית הוא עמדת סון טסו. קלאוזביץ רואה בכוח אמצעי הכרחי ויעיל ומעדיף להפעיל את מרביתו מההתחלה."],
["nature",3,"מהי ״שיטת הטיפוס האידיאלי״, וכיצד כל אחד מההוגים משתמש בה?",["כלי תיאורטי של מודל קיצוני: אצל קלאוזביץ – ״המלחמה המוחלטת״; אצל סון טסו – ״הבסת האויב ללא לחימה היא שיא הכשרון״","תיאור של המצביא המושלם: אצל קלאוזביץ – נפוליאון; אצל סון טסו – הקיסר הסיני","שיטה סטטיסטית לחישוב סיכויי ניצחון, שבה השתמש רק קלאוזביץ ולא סון טסו","רשימת עקרונות שכל צבא חייב לקיים, שאותה ניסחו שניהם במשותף"],"המודל אינו מתאר את המציאות – הוא נקודת ייחוס.","קלאוזביץ מפתח את הטיפוס האידיאלי של מלחמה ״מוחלטת״ – בכל הכוחות, ללא הפסקה. סון טסו משתמש בו באופן מפורש ומוגבל יותר: ניצחון ללא קרב הוא אידיאל, ״אך אינו יותר מזה״."],
["nature",2,"מהי ״המלחמה בתיאוריה״ (המלחמה המוחלטת) של קלאוזביץ?",["מלחמה שמנוהלת בכל הכוחות והאמצעים, ללא הפסקה, עד שצד אחד יכול להכתיב את תנאי הניצחון","מלחמה שמתנהלת רק על הנייר, בתרגילים ובמשחקי מלחמה, בלי לחימה אמיתית","מלחמה מוגבלת שבה כל צד משתמש רק בחלק קטן מכוחו כדי לחסוך בחיי אדם","מלחמה שבה הדרג המדיני מוותר לחלוטין על שליטתו לטובת הצבא"],"זה הטיפוס האידיאלי – לא המציאות.","זהו מודל מופשט. במציאות פועלות נטיות הפוכות (חיכוך, עקרון ההמתנה, שיקולים מדיניים) שמגבילות את המלחמה."],
["nature",3,"מהי ההבחנה בין מלחמה לשלום אצל סון טסו לעומת קלאוזביץ?",["אצל סון טסו ההבחנה מטושטשת – מצב מתמיד של סכסוך; אצל קלאוזביץ ההבחנה חדה וברורה","אצל סון טסו ההבחנה חדה וברורה; אצל קלאוזביץ מלחמה ושלום הם אותו מצב","שניהם רואים במלחמה ובשלום מצבים נפרדים לחלוטין שאין ביניהם קשר","שניהם רואים במלחמה ובשלום מצב אחד מתמשך שאין דרך להבחין בתוכו"],"למי דיפלומטיה ומלחמה הן רצף אחד?","אצל סון טסו דיפלומטיה ומלחמה הן פעילות רצופה אחת ללא קו מפריד. אצל קלאוזביץ הניתוח מתחיל בנקודה שבה הדיפלומטיה נכשלה."],
["nature",3,"איזו ביקורת מופנית לסון טסו בעניין הרתיעה משפיכות דמים?",["חוסר רצון לשפוך דם עלול לשחק לידי היריב, שיעמיד פנים שהוא מוכן להקריב יותר","הרתיעה משפיכות דמים גורמת תמיד למלחמה ממושכת ויקרה יותר מכל חלופה אחרת","הרתיעה משפיכות דמים מונעת מהמדינה לבנות צבא ולהשקיע בטכנולוגיה צבאית","אין כל ביקורת על כך, כי זו נקודת ההסכמה המרכזית בין סון טסו לקלאוזביץ"],"הנקודה תופסת מקום מרכזי אצל קלאוזביץ.","היריב שיודע שהצד השני אינו ששׂ ״להחליף מהלומות״ יכול להונות בהעמדת פנים שהוא מוכן להפעיל יותר כוח. וגם ההונאה היא ״חרב פיפיות״ – אין לאיש מונופול עליה."],
["policy",1,"מהן שלוש רמות המלחמה, מהגבוהה לנמוכה?",["אסטרטגית ← מערכתית ← טקטית","טקטית ← מערכתית ← אסטרטגית","מדינית ← לוגיסטית ← מודיעינית","מערכתית ← אסטרטגית ← טקטית"],"מכלל המלחמה, דרך המערכה, ועד הקרב.","אסטרטגית (כלל המלחמה, מדינית) ← מערכתית (המערכה) ← טקטית (הקרב). הקשר ביניהן מורכב ואינו היררכי פשוט – יש ביניהן יחסי גומלין."],
["policy",2,"באיזו רמת ניתוח עוסק בעיקר כל אחד מההוגים?",["סון טסו – ברמה האסטרטגית-מדינית הגבוהה; קלאוזביץ – בעיקר ברמה המערכתית","סון טסו – ברמה הטקטית בלבד; קלאוזביץ – ברמה המדינית הגבוהה","שניהם עוסקים אך ורק ברמה הטקטית של הקרב הבודד","סון טסו – ברמה המערכתית; קלאוזביץ – ברמה הטקטית"],"זה מסביר למה ההונאה פחות יעילה בעיני קלאוזביץ.","סון טסו מסתכל על התמונה הרחבה (מדיניות ודיפלומטיה). קלאוזביץ עוסק בעיקר ברמה המערכתית – ולכן מעדיף תעוזה, וההונאה נראית לו פחות יעילה."],
["policy",2,"איך מתייחס קלאוזביץ לדיפלומטיה ולכלכלה בספרו?",["כמעט לא דן בהן – לא מזלזל, אלא שהן מחוץ למיקוד הספר; את הסיוע הכלכלי-לוגיסטי הוא מניח מראש","רואה בהן את העיקר, ומקדיש להן את רוב פרקי הספר ״על המלחמה״","מזלזל בהן במפורש וטוען שאין להן כל תפקיד בהשגת יעדי המדינה","דן בהן בהרחבה, אך רק בהקשר של סיום המלחמה ולא בתחילתה"],"״שלילה נפוצה״ במבחן – היזהרו מ״מזלזל״.","קלאוזביץ לא מזלזל בדיפלומטיה – היא פשוט מחוץ לנושא הספר. אצל סון טסו, לעומת זאת, דיפלומטיה היא האמצעי הטוב ביותר לניצחון ללא שפיכות דמים."],
["policy",2,"מה מסמל הביטוי ״הדקדוק של הקרב״ אצל קלאוזביץ?",["שהשגת המטרות המדיניות תלויה בהישגים המערכתיים והטקטיים, ולכן הקרב משנה לעיתים את המטרות המדיניות","שלכל קרב יש חוקים קבועים שאפשר ללמוד כמו כללי דקדוק בשפה","שהפקודות הצבאיות חייבות להיות מנוסחות בשפה ברורה וללא טעויות","שהקרב הוא ״המשפט״ והמדיניות היא רק ״סימן הפיסוק״ בסופו"],"הקשר בין הרמות הוא דו-כיווני.","למלחמה יש ״דקדוק״ משלה אך לא ״היגיון״ משלה – ההיגיון הוא המדיניות. ובכל זאת, מה שקורה בשדה משפיע על מה שאפשר להשיג מדינית."],
["policy",2,"מהי ״טקטיקיזציה של האסטרטגיה״?",["מצב שבו שיקולים צבאיים-מבצעיים גוברים על השיקולים המדיניים, או שמפקד מיישם ניסיון מרמה נמוכה ברמה האסטרטגית","מצב שבו הדרג המדיני מתערב בכל החלטה טקטית קטנה בשדה הקרב ומונע מהמפקדים חופש פעולה","תרגום של תוכנית אסטרטגית לסדרת פקודות טקטיות מפורטות עוד לפני פרוץ המלחמה","מעבר מתוכנן מלחימה טקטית מקומית ללחימה אסטרטגית רחבה בשלב מתקדם של המלחמה"],"דוגמאות: נפוליאון, היטלר, המטה הכללי הגרמני ב-1914.","כאשר ״הדקדוק״ הצבאי מכתיב את המדיניות. דוגמאות: נפוליאון והיטלר, והמטה הכללי הגרמני במלחמת העולם הראשונה."],
["policy",2,"מה עמדתו של ז׳ומיני לגבי היחס בין המדיניות לצבא אחרי פרוץ המלחמה?",["לשיקולים הצבאיים צריכה להינתן עדיפות – בפועל עליונות הצבא על המדיניות","לדרג המדיני צריכה להיות שליטה מלאה בכל החלטה, גם הטקטית ביותר","הצבא והמדיניות שווים, וכל החלטה מתקבלת בהסכמה משותפת בלבד","הצבא צריך לפעול רק לפי הוראות הציבור, באמצעות משאלי עם"],"המפקד כ״מדען״; שליפן ולודנדורף.","ז׳ומיני קובע שאחרי שהמלחמה החלה יש לתת עדיפות לשיקולים המבצעיים. בפועל זו עליונות הצבא על המדיניות – גישה שאפיינה את שליפן ולודנדורף."],
["policy",2,"מהו ההבדל בין ״שליטה אובייקטיבית״ ל״שליטה סובייקטיבית״ לפי הנטינגטון?",["אובייקטיבית – המדינאי לא מתערב בעניינים מקצועיים-צבאיים; סובייקטיבית – המדינאי מתערב בהם","אובייקטיבית – הצבא שולט במדינה; סובייקטיבית – המדינה שולטת בצבא","אובייקטיבית – שליטה באמצעות נתונים; סובייקטיבית – שליטה באמצעות אינטואיציה","אובייקטיבית – מתאימה למלחמה קצרה; סובייקטיבית – מתאימה רק למלחמת גרילה"],"השאלה היא אם המדינאי נכנס לפרטים המקצועיים.","הנטינגטון: בשליטה אובייקטיבית המדינאי קובע מטרות ואינו מתערב בעניינים המקצועיים של הצבא; בשליטה סובייקטיבית הוא מתערב."],
["policy",2,"מה עמדתו של מקיאוולי לגבי חופש הפעולה של המפקד בשטח?",["בעד חופש פעולה מרבי (כמו ברומא); פיקוח מקרוב ״בשלט רחוק״ הכשיל את ערי איטליה","בעד פיקוח הדוק של השליט על כל צעד של המפקד, כמו שנהגו ערי איטליה","המפקד צריך לקבל אישור מהסנאט לכל קרב, אחרת הוא מסכן את הרפובליקה","מקיאוולי לא עסק כלל ביחסים בין השליט למפקדיו בשדה"],"הרומאים נתנו לקונסולים שלהם לפעול בחופשיות.","מקיאוולי מצביע על רומא כדוגמה לחופש פעולה מרבי, וטוען שניהול מלחמה ״בשלט רחוק״ מסוכן."],
["policy",3,"אילו שיקולים צריך מפקד לשקול לפני שהוא מפר פקודה מדינית?",["נסיבות מקומיות, סיכונים, ריכוזיות מערכת השליטה, איכות התקשורת, אינטואיציה וניסיון, רווח והפסד אפשריים","רק את דעתם של החיילים שתחתיו, כי הם אלו שיישאו בתוצאות של כל החלטה שיקבל","רק את חוקי המלחמה הבין-לאומיים ואת דעת הקהל, כי שאר השיקולים אינם רלוונטיים למפקד","אין שיקולים כאלה – לפי הקורס מפקד לעולם אינו רשאי לסטות מפקודה מדינית, בשום נסיבות"],"סון טסו וקלאוזביץ עצמם לא נתנו קריטריונים – אלה שיקולים שהוצעו בקורס.","מאחר שאף אחד מההוגים לא הגדיר קריטריונים, הקורס מציע שורת שיקולים: הנסיבות המקומיות, הסיכון, ריכוזיות השליטה, איכות התקשורת, ניסיון ואינטואיציה, והרווח וההפסד."],
["policy",1,"מה הלקח המרכזי של ארה״ב ממלחמת ויטנאם?",["ניצחון צבאי אינו מבטיח ניצחון מדיני – ארה״ב לא הובסה באף קרב חשוב ובכל זאת הפסידה","ארה״ב הובסה בכל הקרבות החשובים בגלל נחיתות טכנולוגית מול צפון ויטנאם","ניצחון צבאי תמיד מוביל לניצחון מדיני, ולכן ויטנאם הייתה ניצחון אמריקאי","המלחמה הוכיחה שגרילה לעולם אינה יכולה להצליח מול צבא סדיר"],"הטכנולוגיה כמעט לא נכשלה שם.","הכישלון לא הוסבר במונחים צבאיים. המסקנות: אי אפשר להפריד מלחמה ממדיניות, מלחמה מחייבת תמיכה פוליטית, והצבא הוא רק אחד משלושה יסודות (עם הממשלה והעם)."],
["policy",2,"לפי לקחי ויטנאם, מה צריך לעשות אם אי אפשר לזהות יעדים מדיניים ואסטרטגיים ברורים?",["עדיף להימנע ממלחמה","להתחיל במלחמה ולהגדיר את היעדים תוך כדי לחימה","להעביר את ההחלטה על היעדים למפקד בשטח","להפעיל את מרב הכוח כדי שהיעדים יתבררו מעצמם"],"״לא לצעוד את הצעד הראשון בלי להביא בחשבון את האחרון״.","אם לא ניתן לזהות יעדים כאלה, עדיף להימנע ממלחמה. קלאוזביץ: ״חיוני לא לצעוד את הצעד הראשון בלא להביא בחשבון את האחרון״."],
["policy",2,"כמה תנאים יש בדוקטרינת ויינברגר, ומה עומד מאחוריה?",["שישה תנאים; יישום רעיונותיו של קלאוזביץ לתקופה שאחרי ויטנאם","שלושה תנאים; יישום רעיונותיו של סון טסו לעידן הגרעיני","חמישה תנאים; יישום רעיונותיו של ז׳ומיני למלחמה בגרילה","שישה תנאים; יישום רעיונותיו של מאו למלחמות ממושכות"],"הדוקטרינה הוכחה במלחמת המפרץ 1991.","דוקטרינת ויינברגר: 6 תנאים לכניסת ארה״ב למלחמה. היא משקפת אימוץ של רעיונות קלאוזביץ והתאמתם לתקופה שאחרי ויטנאם."],
["policy",2,"איזה מהבאים אינו אחד מתנאי דוקטרינת ויינברגר?",["הלחימה תתחיל רק לאחר שהושגה הפתעה אסטרטגית מלאה","אינטרסים חיוניים של ארה״ב או בנות בריתה מונחים על הכף","היעדים המדיניים והצבאיים מוגדרים בבירור ונבחנים ברציפות","ודאות סבירה שדעת הקהל האמריקאית תתמוך בלחימה"],"התנאים: אינטרס חיוני, כוח מספיק, יעדים ברורים, בחינה רציפה, דעת קהל, מוצא אחרון.","ששת התנאים: (1) אינטרסים חיוניים; (2) כוח מספיק להבהיר כוונה לנצח; (3) יעדים ברורים; (4) בחינה רציפה; (5) תמיכת דעת הקהל; (6) לחימה כמוצא אחרון. הפתעה אינה תנאי."],
["policy",3,"אילו מתנאי ויינברגר קשורים להתנהגות רציונלית של מדינות ונמצאים אצל שני ההוגים?",["הראשון (אינטרס חיוני) והשישי (לחימה כמוצא אחרון)","השלישי (יעדים ברורים) והחמישי (תמיכת דעת הקהל)","השני (כוח מספיק) והרביעי (בחינה רציפה של היעדים)","רק החמישי (דעת הקהל), שהוא הרעיון המרכזי אצל שניהם"],"השלישי, הרביעי והחמישי נדונים כולם אצל קלאוזביץ.","תנאים 1 ו-6 קשורים להתנהגות הרציונלית של מדינות (קלאוזביץ וסון טסו). תנאים 3, 4 ו-5 נדונים כולם אצל קלאוזביץ."],
["policy",2,"לפי הקורס, מה אפשר בראש ובראשונה את הניצחון האמריקאי במלחמת המפרץ 1991?",["תכנון והכנה פוליטיים נבונים – דעת קהל, קואליציה רחבה, יעדים ברורים וחופש פעולה לצבא","העליונות הטכנולוגית בלבד, שאפשרה לנצח בלי כל הכנה מדינית","מספר החיילים העצום, שהיה גדול פי עשרה מזה של הצבא העירקי","ההחלטה לפתוח במלחמה מיד, בלי להמתין לריכוז כוחות או לדיפלומטיה"],"הנשיא בוש האב, צ׳ייני ופאוול.","הטכנולוגיה חשובה, אך הניצחון הושג בעיקר בזכות המנהיגות המדינית של בוש: גיוס דעת הקהל, בידוד עיראק בקואליציה רחבה, הגדרת יעדים, ומתן חופש פעולה לצבא."],
["policy",3,"מהו ״הצבא הוא רק אחד משלושת היסודות״ – ומי הם השניים האחרים?",["הממשלה והעם","המודיעין והלוגיסטיקה","הצי וחיל האוויר","בעלות הברית והאו״ם"],"רמז: זה מתחבר לשילוש של קלאוזביץ.","לפי לקחי ויטנאם, הצבא הוא רק אחד משלושה יסודות חיוניים – יחד עם הממשלה והעם. בלי איזון הרמוני ביניהם אי אפשר לנצח."],
["theory",1,"מהו ״חיכוך״ לפי קלאוזביץ?",["כל מה שהופך את המלחמה במציאות לשונה מהמלחמה על הנייר – אי-ודאות, מקריות, מזל, מודיעין שגוי, עייפות וסכנה","המתח הפוליטי בין הדרג המדיני לדרג הצבאי לפני שמחליטים לצאת למלחמה","המגע הפיזי הראשון בין שני צבאות בשדה הקרב, שבו מתחיל הקרב","הוויכוח בין המפקדים במטה הכללי על בחירת התוכנית הטובה ביותר"],"״הכול במלחמה פשוט מאוד, אך גם הדבר הפשוט ביותר קשה״.","החיכוך הוא אחד ה״גורמים הנייטרליים״ שמונעים ניהול מלחמה רציונלי טהור, ויוצר ״תהום גדולה בין תכנון לביצוע״."],
["theory",2,"מה אומר קלאוזביץ על הפער בין התיאוריה (הרצוי) למעשה (המצוי)?",["הפער לעולם לא נסגר לגמרי – אפשר רק לצמצם אותו","הפער נסגר לחלוטין כשיש מספיק מודיעין ותכנון מוקדם","אין פער כזה – מפקד טוב תמיד מבצע בדיוק את מה שתכנן","הפער קיים רק בצבאות חלשים ולא בצבאות של מעצמות"],"״תהום גדולה בין תכנון לביצוע״.","עקרונות המלחמה ידועים – הבעיה היא היישום. הפער בין תכנון לביצוע לעולם לא נסגר לגמרי, רק מצטמצם."],
["theory",2,"איזה מהבאים אינו גורם שיוצר את הפער בין התכנון לביצוע במלחמה?",["העובדה שעקרונות המלחמה אינם ידועים לאף מפקד","כמות עצומה של משתנים ויסודות שאי אפשר למדוד","האופי ההדדי של פעולה-תגובה בין הצדדים","חיכוך, מקריות, מזל ומודיעין לקוי"],"הבעיה אינה הידיעה – אלא היישום.","עקרונות המלחמה דווקא ידועים (ריכוז, הפתעה, מטרות ברורות וכו׳). הפער נוצר ממשתנים רבים, יסודות לא מדידים, פעולה-תגובה, חיכוך, חשאיות, מודיעין לקוי, סיכון ומורל."],
["theory",2,"מהי ״הערכה נטו״ (Net Assessment)?",["ניתוח היכולות הצבאיות, הטכנולוגיות, הפוליטיות והכלכליות של כל הצדדים כדי לזהות איומים, הזדמנויות ויתרון יחסי","חישוב מדויק של מספר החיילים, הטנקים והמטוסים בלבד, כדי לקבוע מראש מי הצד החזק","הערכה של הנזק שנגרם לאויב בסוף כל יום לחימה, לצורך דיווח שוטף לדרג המדיני","ניכוי האבדות של הצד שלנו מהאבדות של האויב בסוף המלחמה, כדי לקבוע מי ניצח בה"],"נקראת גם ״הערכת יחסי כוחות״.","הערכה נטו (correlation of forces) – ניתוח כולל של כל סוגי היכולות. המטרה: לזהות יתרון יחסי, לנצל את חוזקותינו ואת חולשות היריב ולהכתיב את אופי המלחמה."],
["theory",2,"מי האמין שהערכה נטו יכולה להפיק תמונה אובייקטיבית ומדויקת?",["מאו טסה-טונג (בהשראת סון טסו והמטריאליזם הדיאלקטי)","קלאוזביץ, בהשראת הפיזיקה של ניוטון","מקיאוולי, בהשראת הרפובליקה הרומית","הנטינגטון, בהשראת המדע המדיני האמריקאי"],"הוא גם לא האמין בגאונות מולדת.","מאו ראה בהערכה נטו פתרון ״אובייקטיבי-מדעי״ – ניתוח קונקרטי של תנאים ממשיים. קלאוזביץ, לעומתו, סמך על ניסיון ואינטואיציה של המפקד."],
["theory",3,"כיצד קלאוזביץ ומאו מציעים לסגור את הפער בין תיאוריה למעשה?",["קלאוזביץ – ניסיון ו״טביעת עין״ של גאון צבאי; מאו – עבודה קשה, למידה והערכה נטו","קלאוזביץ – הערכה נטו מדעית; מאו – הסתמכות על גאון צבאי מולד","שניהם מציעים להסתמך אך ורק על טכנולוגיה מתקדמת ומחשבים","שניהם טוענים שאין צורך לסגור את הפער, כי הוא אינו משפיע על התוצאה"],"אחד מאמין בגאונות, השני לא.","קלאוזביץ – סובייקטיבי: ניסיון ואינטואיציה. מאו – ״אובייקטיבי-מדעי״: עבודה קשה והערכה נטו. מסקנת המצגת: השתיים חופפות, שתיהן סובייקטיביות למעשה, ושתיהן לא מספקות פתרון מלא."],
["theory",3,"מהן שתי הטעויות בהערכת האויב לפי מאו?",["הגזמה בכוח האויב (נצמדים להגנה ומשאירים לו יוזמה) וזלזול בו (מאיצים מעבר לשלב הבא מוקדם מדי)","הסתמכות על מודיעין זר ושימוש בטכנולוגיה מיושנת במהלך הלחימה","פתיחה במלחמה בחורף ולחימה בשתי חזיתות במקביל","האמנה בתעמולת האויב וזלזול בכוח בעלי הברית שלנו"],"אחת קשורה להערכת יתר, השנייה להערכת חסר.","(1) הגזמה בכוח האויב – נצמדים להגנה ומשאירים לו את היוזמה; (2) זלזול באויב – מאיצים מעבר לשלב הבא מוקדם מדי."],
["theory",3,"מהי הבעיה בניסיון של מפקד כפתרון לפער בין תיאוריה למעשה?",["הניסיון עלול להפוך למכשול – תגובה אוטומטית שאינה רואה נסיבות חדשות, או העברת ניסיון מרמה לרמה","הניסיון תמיד מוביל להחלטות מהירות מדי ולכן אסור להסתמך עליו כלל","לניסיון אין שום ערך במלחמה, כי כל קרב שונה לחלוטין מקודמו","ניסיון רלוונטי רק למפקדים זוטרים ולא למצביאים בכירים"],"נפוליאון והיטלר.","ניסיון עלול לגרום לתגובה אוטומטית או להעברת לקחים מרמה טקטית לאסטרטגית. במלחמות היי-טק התיאוריה קודמת לניסיון (סימולציות) – והפער גדל."],
["theory",2,"לפי סון טסו, מה אפשר לעשות לאחר מודיעין טוב והערכה נטו?",["לחזות בדייקנות את תוצאת המלחמה – עמדה שקלאוזביץ חולק עליה","לוותר לחלוטין על הצבא ולסמוך על הדיפלומטיה בלבד","להבטיח שהמלחמה לא תפרוץ לעולם, בכל מצב","לא כלום – לדעתו גם מודיעין טוב אינו משנה את התוצאה"],"קלאוזביץ סבור שחיזוי כזה בלתי אפשרי.","סון טסו מאמין שאחרי מודיעין והערכה נטו אפשר לחזות את התוצאה. קלאוזביץ סבור שבגלל המורכבות, אי-הוודאות והחיכוך – חיזוי בלתי אפשרי."],
["theory",3,"מהי הביקורת על ההערכה נטו?",["המציאות הצבאית חמקמקה; ככל שהדרג גבוה יותר יש יותר עיוותים (מאוויים, פוליטיקה, אידאולוגיה, מודיעין לקוי)","ההערכה נטו מדויקת מדי, ולכן היא גורמת למפקדים לפחד לצאת לקרב ומשתקת את היוזמה","ההערכה נטו מתאימה רק למלחמות ימיות ולמלחמות אוויר, ולא למלחמות יבשתיות","אין עליה ביקורת – כל ההוגים בקורס הסכימו שהיא מדויקת לחלוטין בכל דרג ובכל מצב"],"ובמלחמה ממושכת יש פיתוי ל״קיצורי דרך״.","הביקורת: המציאות חמקמקה; בדרגים הגבוהים יש יותר עיוותים; ובמלחמה ממושכת קיים פיתוי לקיצורי דרך."],
["theory",2,"מה מסמלת אצל קלאוזביץ ההשוואה לבעיות ״הראויות לכשרון של ניוטון״?",["שהעיסוק במורכבות ובאי-היכולת לחזות במלחמה הוא אתגר אינטלקטואלי עצום – אולי תרומתו החשובה ביותר","שאפשר לפתור כל בעיה צבאית בעזרת נוסחה מתמטית אחת, כמו חוקי התנועה של ניוטון","שהמלחמה צריכה להיחקר בעיקר בידי פיזיקאים ומתמטיקאים ולא בידי קצינים","שהטכנולוגיה הצבאית מתקדמת כל כך מהר שרק מדען בדרגת ניוטון יכול להבין אותה"],"הכאוס של המלחמה.","העיסוק של קלאוזביץ במורכבות, בכאוס ובאי-היכולת לחזות הוא אולי תרומתו החשובה ביותר."],
["moral",1,"מהן שלוש הצלעות של ״השילוש הפרדוקסלי״ של קלאוזביץ?",["העם (אלימות ולהט), המצביא וצבאו (מקריות ויצירתיות), הממשלה (תבונה ויעדים מדיניים)","העם (תבונה), הצבא (אלימות), הממשלה (מקריות והסתברות)","המודיעין, הלוגיסטיקה והתמרון","הכלכלה, הטכנולוגיה והדיפלומטיה"],"איזו צלע קשורה לרגש, איזו למזל ואיזו להיגיון?","העם – אלימות קמאית, שנאה ולהט; המצביא וצבאו – מקריות, הסתברות, כשרון ואומץ; הממשלה – תבונה ויעדים מדיניים."],
["moral",2,"איזו צלע בשילוש קשורה ל״מקריות, הסתברות, רוח יצירתית, כשרון ואומץ״?",["המצביא וצבאו","העם","הממשלה","בעלות הברית"],"מי פועל בתוך ״ערפל הקרב״?","הצלע של המצביא וצבאו מאופיינת במקריות ובהסתברות, וגם ברוח היצירתית ובכשרון של המפקד."],
["moral",2,"מה משמעות ״לרבע את המשולש״?",["להוסיף מגמה רביעית – חומרית-כלכלית-טכנולוגית – כי השילוש מתעלם מהצד החומרי","להוסיף את בעלות הברית כצלע רביעית, כי השילוש מתעלם מהזירה הבין-לאומית","לחלק את המלחמה לארבעה שלבים במקום שלושה","להוסיף את התקשורת כצלע רביעית, כי היא משפיעה על העם"],"אי אפשר לנצח בכוח רצון בלבד.","הביקורת: שלוש המגמות הן לא חומריות. לכן מוסיפים מגמה רביעית: טווח כלי הנשק, ניידות, דיוק וקצב אש, מערכות שליטה ובקרה."],
["moral",3,"לפי ״הניתוח הווקטורי״ של השילוש, מה מאפיין מלחמה גרעינית?",["כמעט הכול בידי הממשלה; הצבא מגיע ל״לחיצה על כפתורים״ והעם רק סובל","לשלוש הצלעות משקל שווה, בדיוק כמו במלחמה קונבנציונלית","העם בולט יותר מהצבא, והממשלה כמעט אינה משפיעה","הצבא שולט בכול, והממשלה והעם אינם משפיעים כלל"],"השוו לקונבנציונלית ולגרילה.","קונבנציונלית – משקל שווה לשלוש. גרילה – העם בולט יותר מהצבא. גרעינית – כמעט הכול בידי הממשלה."],
["moral",3,"לפי הניתוח הווקטורי של השילוש, מה מאפיין מלחמת גרילה?",["העם בולט יותר מהצבא, והממשלה חשובה כמו במלחמה קונבנציונלית","הצבא בולט יותר מהעם, והממשלה כמעט אינה רלוונטית","כמעט הכול בידי הממשלה, והצבא רק לוחץ על כפתורים","לשלוש הצלעות אין כל משקל, כי גרילה אינה נחשבת מלחמה"],"בגרילה, מי נושא את הלחימה?","במלחמת גרילה העם בולט יותר מהצבא, בעוד שחשיבות הממשלה נשארת כמו במלחמה קונבנציונלית."],
["moral",2,"מה עמדת קלאוזביץ לגבי ״הגורמים הנפשיים״ לעומת החומריים?",["הגורמים הנפשיים חשובים יותר; עוצמה צבאית היא מכפלה של האמצעים החומריים בכוח הרצון","הגורמים החומריים חשובים יותר; אפשר לנצח רק בזכות נשק וכסף","הגורמים הנפשיים אינם קיימים במלחמה מודרנית ולכן אין לעסוק בהם","שני סוגי הגורמים חסרי חשיבות לעומת מזג האוויר והשטח"],"״כוחות רוחניים״.","קלאוזביץ: הגורמים הנפשיים חשובים יותר מהחומריים, ופעולה צבאית מכוונת תמיד גם נגדם. עוצמה צבאית = אמצעים חומריים × כוח רצון."],
["moral",2,"מה המגבלה בדיון של קלאוזביץ בגורמים הנפשיים?",["הוא מסביר כמה הם חשובים, אבל לא נותן הנחיה איך למדוד אותם","הוא מתעלם מהם לחלוטין ועוסק רק בגורמים החומריים","הוא טוען שאפשר למדוד אותם בדיוק בעזרת סקרים בקרב החיילים","הוא מתאר אותם רק בהקשר של הצי ולא של הצבא היבשתי"],"שלילה נפוצה במבחן: קלאוזביץ לא מזלזל בהם.","קלאוזביץ מקדיש לגורמים הלא רציונליים יותר מכל תיאורטיקן אחר – ולכן הוא מציאותי יותר – אבל אינו מסביר איך לכמת אותם."],
["moral",3,"מדוע קלאוזביץ מתנגד לתיאוריות ״מדעיות״ שמצמצמות את המלחמה למשתנים מדידים?",["הן מחפשות את הפתרון רק במקום שיש נתונים ומתעלמות מהגורמים הנפשיים – הן ״מעוררות סלידה אינטלקטואלית״","הן מסובכות מדי לחישוב בשדה הקרב, ולכן אין למפקדים זמן ללמוד ולהפעיל אותן","הן נכתבו בידי אויביה של פרוסיה, ולכן לדעתו אינן אמינות ואין להסתמך עליהן","הוא לא מתנגד להן – הוא עצמו כתב תיאוריה מתמטית מדויקת שמצמצמת את המלחמה למספרים"],"רלוונטי היום נגד ״המהפכה בעניינים צבאיים״.","תיאוריות כאלה מחפשות את הפתרון רק היכן שיש נתונים. קלאוזביץ סבור שאת המלחמה חוקרים כמכלול (גשטלט), ורק אינטואיציית הגאון הצבאי חושפת את קשרי הגומלין."],
["moral",2,"מה ההבדל בגישה לגורמים לא רציונליים בין סון טסו לקלאוזביץ?",["סון טסו – ״המודל הרציונלי הטהור״ עם חישוב שהוא כמעט מתכון להצלחה; קלאוזביץ – פסימי ומציאותי יותר, עם ציפיות מוגבלות מחישוב","סון טסו – פסימי ומתעלם מחישוב רציונלי; קלאוזביץ – מאמין בחישוב שכמעט מבטיח הצלחה","שניהם התעלמו לחלוטין מגורמים לא רציונליים כמו מורל, מזל ומוטיבציה של הלוחמים","שניהם טענו שהמלחמה כולה אינה רציונלית, ולכן אין כל טעם לתכנן אותה מראש"],"מי יותר אופטימי לגבי החישוב?","שניהם רואים במלחמה פעילות רציונלית בעיקרה. אבל סון טסו מייצג את המודל הרציונלי הטהור, וקלאוזביץ מכיר יותר בחיכוך, במקריות ובמורכבות."],
["moral",2,"על מי מוטלת קודם כל האחריות לזהות את אופייה של המלחמה?",["על המנהיג המדיני (בהתייעצות עם המצביא)","על המפקדים הזוטרים בשטח, כי הם הראשונים שפוגשים את האויב בפועל","על אנשי המודיעין בלבד, שמגישים את ההערכה לדרג המדיני לאישור","על העם, באמצעות בחירות ומשאלי עם לפני היציאה למלחמה"],"מנהיגים שלא מבינים זאת ״יילחמו את המלחמה הקודמת״.","כל מלחמה ייחודית. האחריות לזהות את אופיה מוטלת קודם כל על המנהיג המדיני, בהתייעצות עם המצביא."],
["moral",3,"איך מתאר הקורס את תהליך ההבנה של אופי המלחמה?",["תהליך הדדי, דיאלקטי ומתמשך – מעדכנים ללא הרף ומבינים באמת רק אחרי שהמלחמה פרצה","תהליך חד-פעמי שמסתיים לפני פרוץ המלחמה, ואין לשנותו אחר כך","תהליך שמבצע המודיעין לבדו, ותוצאתו מדויקת במאה אחוז","תהליך שאינו אפשרי כלל, ולכן אין טעם לנסות להבין את אופי המלחמה"],"דיוק של 25% עדיף על 10%.","ההבנה היא תהליך מתמשך. צריך גמישות לשנות ואף לנטוש את האסטרטגיה המקורית, ודיוק חלקי עדיף על פני דיוק נמוך עוד יותר."],
["moral",2,"מה טוען מקיאוולי לגבי ההסתגלות של רפובליקות לעומת משטרים סמכותיים?",["רפובליקות מסתגלות טוב יותר כי הן מחליפות מנהיגים; משטרים סמכותיים מדכאים חדשנות","משטרים סמכותיים מסתגלים טוב יותר כי ההחלטות בהם מהירות","אין הבדל – שני סוגי המשטרים מסתגלים באותה מידה","רפובליקות לעולם אינן מסתגלות, ולכן הן מפסידות בכל מלחמה"],"החלפת מנהיגים כיתרון.","מקיאוולי: רפובליקות (דמוקרטיות) מסתגלות טוב יותר לאופי המלחמה המשתנה, כי הן יכולות להחליף מנהיגים."],
["moral",3,"איזו מהדוגמאות הבאות לא הוצגה בקורס ככישלון בהבנת אופי המלחמה?",["רומא מול קרתגו במלחמה הפונית השנייה","בריטניה במהפכה האמריקנית","מעצמות אירופה מול המהפכה הצרפתית","ארה״ב בויטנאם"],"הדוגמאות בקורס: בריטניה, אירופה, מלחמת העולם הראשונה, ויטנאם וסדאם.","הדוגמאות בקורס: בריטניה במהפכה האמריקנית, מעצמות אירופה מול המהפכה הצרפתית, מלחמת העולם הראשונה (ציפו למלחמה קצרה), ארה״ב בויטנאם וסדאם ב-1991."],
["moral",2,"מה היה המשמעות של מלחמות המהפכה הצרפתית ונפוליאון לגבי ״האומה החמושה״?",["הן היו הראשונות שניצלו את כל האוכלוסייה; הגיוס הכללי היה תחילת המלחמה הטוטלית המודרנית","הן היו המלחמות האחרונות שבהן לחמו רק שכירי חרב מקצועיים","הן הוכיחו שאפשר לנצח בלי תמיכת העם","הן היו מלחמות שבהן הממשלה הייתה הצלע היחידה בשילוש"],"Levée en masse.","מלחמות המהפכה הצרפתית ונפוליאון היו הראשונות שניצלו את כל האוכלוסייה – הגיוס הכללי סימן את תחילת המלחמה הטוטלית המודרנית."],
["cog",1,"מהו ״מרכז כובד״ לפי קלאוזביץ?",["״מקור כל העוצמה והתנועה, שהכל תלוי בו״ – הנקודה שאליה יש לכוון את כל המאמצים","הנקודה הגיאוגרפית שבה נמצא מרכז הארץ של האויב, שאליה יש להגיע בכל מחיר","המקום שבו מוצב המטה הכללי של הצבא שלנו, שאותו יש להגן מפני כל תקיפה","נקודת האיזון בין הדרג המדיני לדרג הצבאי, שמבטיחה שליטה אזרחית בצבא"],"המושג מבוסס על הפיזיקה של ניוטון.","מרכז הכובד מתפתח מתוך המאפיינים של שני הצדדים. אם האויב איבד את שיווי המשקל – לא לתת לו להתאושש, מכה אחר מכה לאותו מקום."],
["cog",1,"מהו סדר העדיפויות של סון טסו בתקיפה?",["אסטרטגיית האויב ותוכניותיו ← בריתותיו ← צבאו ← ערים (מוצא אחרון)","צבא האויב ← עיר הבירה ← בעל הברית העיקרי ← דעת הקהל","ערים ← צבא ← בריתות ← אסטרטגיה","בריתות ← ערים ← אסטרטגיה ← צבא"],"הערים הן הכי יקרות לתקיפה.","סון טסו: (1) תקיפת תוכניות האויב בתחילתן; (2) שיבוש בריתותיו; (3) תקיפת צבאו; (4) תקיפת ערים – המוצא האחרון והיקר ביותר."],
["cog",1,"מהו סדר העדיפויות של קלאוזביץ בתקיפת מרכזי הכובד?",["השמדת צבא האויב ← כיבוש הבירה ← מהלומה נגד בעל הברית העיקרי ← דעת הקהל והמנהיגים","תקיפת תוכניות האויב ← שיבוש בריתותיו ← תקיפת צבאו ← תקיפת ערים כמוצא אחרון","כיבוש הבירה ← שבירת דעת הקהל ← השמדת צבא האויב ← מהלומה נגד בעל הברית","מהלומה נגד בעל הברית ← השמדת צבא האויב ← כיבוש הבירה ← פגיעה בכלכלה"],"הסדר ״הפוך״ לזה של סון טסו.","קלאוזביץ: (1) השמדת צבא האויב; (2) כיבוש הבירה; (3) מהלומה נגד בעל הברית העיקרי; (4) דעת הקהל והמנהיגים. ז׳ומיני מסכים איתו (צבא ואז בירה)."],
["cog",2,"מה מיוחד בשיבוש הבריתות אצל קלאוזביץ לעומת סון טסו?",["אצל סון טסו זו עדיפות גבוהה ודיפלומטית; אצל קלאוזביץ היא בעדיפות נמוכה – וגם אז בדרך צבאית","אצל שניהם שיבוש הבריתות הוא העדיפות הראשונה, ונעשה בדרך דיפלומטית","אצל קלאוזביץ זו העדיפות הראשונה, ואצל סון טסו היא לא מוזכרת כלל","שניהם מתנגדים לשיבוש בריתות, כי זה מאריך את המלחמה"],"הספר של קלאוזביץ לא עוסק בדיפלומטיה.","העדיפות הראשונה של סון טסו – ניצחון דיפלומטי דרך שיבוש בריתות – היא מהאחרונות אצל קלאוזביץ, ואצלו השיבוש הוא באמצעות מהלומה צבאית."],
["cog",2,"מהו מרכז הכובד העיקרי של האויב לפי כל אחד מההוגים?",["סון טסו – כוח הרצון של האויב ומערכת הבריתות; קלאוזביץ – צבא האויב","סון טסו – צבא האויב; קלאוזביץ – כוח הרצון ומערכת הבריתות","שניהם – עיר הבירה של האויב","שניהם – הכלכלה והתעשייה של האויב"],"אחד ״שובר רצון״, השני ״משמיד״.","סון טסו: כוח הרצון והבריתות. קלאוזביץ: צבא האויב (עם מרכזי כובד נוספים – המנהיג ודעת הקהל)."],
["cog",2,"מה ההבדל בפיתוח מושג מרכז הכובד אצל שני ההוגים?",["קלאוזביץ – מפורש ושיטתי עם הנחיות קונקרטיות; סון טסו – מובלע, בעיקר כמטפורה ובהנחיות כלליות","סון טסו – מפורש ושיטתי עם הנחיות קונקרטיות; קלאוזביץ – מובלע, בעיקר כמטפורה","שניהם פיתחו את המושג בדיוק באותו אופן, באותם מונחים ובאותה רמת פירוט","המושג אינו מופיע אצל אף אחד מהם במפורש – הוא פותח רק מאוחר יותר בידי ז׳ומיני"],"המושג ״מרכז כובד״ עצמו שייך לקלאוזביץ.","אצל קלאוזביץ מרכז הכובד הוא מושג מפורש ושיטתי. אצל סון טסו הוא מובלע – אמרות ללא הסבר והנחיות כלליות."],
["cog",2,"אילו מרכזי כובד נוספים מזכיר קלאוזביץ מעבר לצבא האויב?",["המנהיג (נפוליאון, היטלר, סדאם) ודעת הקהל (צרפת באלג׳יריה, ארה״ב בויטנאם)","הצי (בריטניה במלחמות נפוליאון) וחיל האוויר (גרמניה במלחמת העולם השנייה)","המדע והתעשייה (פרוסיה במאה ה-19) והדת (ספרד במלחמות הדת)","מזג האוויר (רוסיה בחורף 1812) והשטח ההררי (שווייץ במלחמות אירופה)"],"המלחמה לא נגמרה כל עוד הם שלטו.","המנהיג ודעת הקהל: צרפת וארה״ב לא הובסו בשטח – הן הפסידו בבית. סון טסו לא מזכיר אותם במפורש, אך הם נכנסים אצלו תחת ״תקיפת אסטרטגיית האויב״."],
["cog",2,"מדוע מלחמת המפרץ 1991 הופסקה ״טרם זמנה״ לפי הקורס?",["מרכז הכובד זוהה בטעות כצבא העירקי, בעוד שהאמיתי היה פוליטי – סדאם חוסיין עצמו","הקואליציה נגמרה לה התחמושת לפני שהשיגה את יעדיה","האו״ם אסר על המשך הלחימה בגלל אבדות כבדות לקואליציה","הצבא העירקי ניצח בקרב המכריע וכפה הפסקת אש"],"צבא האויב היה רק תנאי מוקדם.","הצבא העירקי היה רק תנאי מוקדם לתקיפת מרכז הכובד האמיתי – סדאם. לכן הניצחון הצבאי המכריע לא היה שלם במובן המדיני."],
["cog",3,"לפי סון טסו, מדוע תקיפת ערים היא המוצא האחרון?",["כי זו הדרך היקרה ביותר – מצור על ערים גובה מחיר כבד בזמן, בכוח ובחיים","כי הערים אינן חשובות כלל למאמץ המלחמתי של האויב","כי סון טסו האמין שאסור מבחינה דתית לפגוע בערים","כי הערים תמיד נכנעות מעצמן בסוף המלחמה, בלי צורך בתקיפה"],"הניצחון האידיאלי – ״להשתלט על המדינה כשהיא שלמה״.","סון טסו מחפש את הדרך הזולה ביותר. מצור על ערים הוא הדרך היקרה ביותר, ולכן העדיפות האחרונה."],
["win",1,"מהו הניצחון האידיאלי לפי סון טסו?",["לנצח בלי להילחם – לשכנע את האויב להיכנע ואם אפשר אף לעבור צד","להשמיד את כוחות האויב בקרב גדול ומכריע אחד","לכבוש את עיר הבירה של האויב בהתקפה מהירה","להתיש את האויב במלחמה ארוכה עד שיתמוטט כלכלית"],"״שיא הכשרון״.","״הבסת האויב ללא לחימה היא שיא הכשרון״. הכוח – רק כמפלט אחרון. אצל קלאוזביץ ניצחון בלי קרב הוא יוצא דופן נדיר."],
["win",1,"מהו ״עקרון ההשמדה״ של קלאוזביץ?",["השמדת כוחות האויב בקרב גדול חייבת תמיד להיות השיקול העיקרי","השמדת ערי האויב כדי לשבור את רוח העם שלו","השמדת התוכניות של האויב לפני שהמלחמה מתחילה","השמדת הנשק שלנו בסוף המלחמה כדי להבטיח שלום"],"מה מטרת הקרב אצל קלאוזביץ?","״השמדת כוחות האויב חייבת תמיד להיות השיקול העיקרי״ – לפיו זו הדרך הקצרה ביותר להשגת היעדים המדיניים."],
["win",2,"לפי הקורס, מי ינצח בעימות בין מפקד קלאוזביצי למפקד שקורא את סון טסו מילולית, כששאר התנאים שווים?",["למפקד הקלאוזביצי סיכוי טוב יותר","למפקד שקורא את סון טסו מילולית סיכוי טוב יותר","לשניהם סיכוי שווה בדיוק","אי אפשר לדעת, כי הקורס לא עוסק בשאלה הזו"],"חולשת סון טסו: מלחמה כ״תרגיל אינטלקטואלי לא קטלני״.","לקלאוזביצי סיכוי טוב יותר. חולשת קלאוזביץ: פרשנות מוטעית של עקרון ההשמדה עלולה להוביל לשימוש קל מדי בכוח."],
["win",2,"איזה מהבאים אינו אחד ממכפילי הכוח של סון טסו?",["עדיפות מספרית מוחלטת","תמרון","הונאה והטעיה להשגת הפתעה","לוחמה פסיכולוגית"],"חמישה: תמרון, מודיעין, הונאה, גישה עקיפה, לוחמה פסיכולוגית.","חמשת מכפילי הכוח: תמרון, מודיעין, הונאה והטעיה, הגישה העקיפה ולוחמה פסיכולוגית. קלאוזביץ מייחס להם חשיבות פחותה."],
["win",3,"מהו הפרדוקס של ״הגישה העקיפה״?",["אם האויב צופה אותה היא הופכת לישירה, וכל מה שמצליח נהיה ״עקיף״ בדיעבד","היא תמיד מצליחה, ולכן האויב לעולם לא יכול להתכונן אליה","היא דורשת יותר כוח מהגישה הישירה, אף שמטרתה לחסוך בכוח","היא מתאימה רק להגנה ולא להתקפה, אף שהיא נחשבת התקפית"],"סון טסו לא מסביר איך מזהים את העקיפה ״הטובה ביותר״.","אם האויב מזהה את המהלך העקיף ונערך אליו – הוא הופך לישיר. ובדיעבד, כל מהלך שמצליח מתויג ״עקיף״."],
["win",2,"במה מסכימים סון טסו וקלאוזביץ לגבי עדיפות מספרית?",["המפתח הוא עדיפות יחסית בנקודת המפגש המכרעת, לא יתרון מספרי מוחלט – גם צבא קטן יכול לנצח","רק עדיפות מספרית מוחלטת מבטיחה ניצחון, ואין לצאת למלחמה בלעדיה","עדיפות מספרית אינה משנה דבר, והמלחמה מוכרעת רק בטכנולוגיה","שניהם מתנגדים לריכוז כוחות ומעדיפים לפזר את הצבא בשטח"],"צבא קטן עם מנהיגות מוכשרת.","שניהם: עדיפות יחסית בנקודת ההכרעה. קלאוזביץ מוסיף שעדיפות מספרית מכרעת היא אחת הדרכים הבודדות לנצח ללא קרב."],
["win",3,"איך משיגים עדיפות בנקודת המפגש – לפי הגישה ה״חיובית״ וה״שלילית״?",["קלאוזביץ (חיובית) – ריכוז מרבי של כוחותינו; סון טסו (שלילית) – למנוע מהאויב להתרכז בתחבולות שגורמות לו להתפצל","קלאוזביץ (שלילית) – הונאה והסחה; סון טסו (חיובית) – ריכוז מרבי של כוחותינו","שניהם (חיובית) – הגדלת הצבא באמצעות גיוס כללי בלבד","שניהם (שלילית) – הימנעות מוחלטת מכל מגע עם האויב"],"מי צריך הונאה כדי לפצל את האויב?","קלאוזביץ – הגישה ה״חיובית״: לרכז את כוחנו (חד-צדדי אבל בטוח). סון טסו – ה״שלילית״: לגרום לאויב לפצל כוחות. הרצוי: לשלב."],
["win",2,"מה עמדת שני ההוגים לגבי מהירות במלחמה?",["שניהם רואים במהירות דבר חיוני – סון טסו: ״נחישות ומהירות״; קלאוזביץ: כל השתהות מיותרת היא בזבוז כוח","סון טסו מעדיף מלחמה איטית וזהירה שמתישה את האויב; קלאוזביץ מעדיף מהירות","קלאוזביץ מעדיף מלחמה ממושכת שבה הזמן פועל לטובת התוקף; סון טסו מעדיף מהירות","שניהם טוענים שמהירות פוגעת בדיוק ובתכנון, ולכן יש להימנע ממנה ככל האפשר"],"שניהם רוצים מלחמה קצרה ומכרעת.","שניהם רואים במהירות דבר חיוני – חלק מההסכמה הכללית על מלחמה קצרה ומכרעת."],
["win",2,"מה ההבדל בין ההוגים ביחס להדדיות – לכך שגם האויב פועל?",["קלאוזביץ מדגיש את האופי ההדדי – אין פתרונות חד-צדדיים; סון טסו כמעט לא מתייחס לכך שגם האויב יפעל כך","סון טסו מדגיש את האופי ההדדי של המלחמה; קלאוזביץ מניח שהאויב יישאר פסיבי","שניהם מניחים שהאויב לא יגיב, ולכן מתכננים רק את הצעדים של הצד שלנו","שניהם טוענים שהאויב תמיד פועל בדיוק כפי שצפינו, ולכן אין צורך בתוכנית גיבוי"],"אי אפשר ״מעט כוח כדי להשיג הרבה״.","קלאוזביץ מדגיש את האופי ההדדי של המלחמה. סון טסו כמעט מתעלם מכך שגם האויב יכול להונות ולתמרן."],
["win",3,"מה מחפש כל אחד מההוגים כשהוא בוחר דרך פעולה?",["סון טסו – הדרך היעילה (הזולה) ביותר; קלאוזביץ – הדרך התכליתית ביותר, תוך ניתוח ״המקרה הגרוע ביותר״","סון טסו – הדרך התכליתית ביותר; קלאוזביץ – הדרך הזולה ביותר, גם אם היא איטית","שניהם – הדרך המהירה ביותר לניצחון, בלי להתחשב כלל במחיר ובאבדות","שניהם – הדרך שתזכה בתמיכת הציבור, גם אם אינה היעילה ביותר מבחינה צבאית"],"״ככל שמרכזים יותר בהתחלה, צריך פחות בהמשך״.","סון טסו מחפש את הזולה ביותר. קלאוזביץ את התכליתית ביותר – לרכז הרבה כוח מההתחלה."],
["win",2,"במציאות, מי נוטה להסתמך על הונאה ומי על כוח ישיר?",["אומות חזקות סומכות על כוח ישיר; ההונאה נשארת בעיקר לחלשים","אומות חזקות סומכות על הונאה; החלשים נוקטים כוח ישיר","כל האומות משתמשות רק בהונאה במלחמה המודרנית","כל האומות נמנעות מהונאה מסיבות מוסריות"],"קלאוזביץ: ההונאה היא ״המפלט האחרון של החלש״.","אף שהרצוי הוא שילוב שתי הגישות, במציאות אומות חזקות סומכות על כוח ישיר וההונאה נשארת לחלשים."],
["cont",1,"מהו ״עקרון ההמשכיות״?",["מי שהשיג יתרון חייב להפעיל לחץ רצוף ולא לתת לאויב מנוחה להשיב את שיווי משקלו","יש להמשיך לנהל משא ומתן עם האויב גם בזמן הלחימה","המלחמה חייבת להימשך לפחות כמה שנים כדי להיות מכרעת","יש לשמור על אותם מפקדים לאורך כל המלחמה בלי להחליפם"],"ברמה הטקטית נקרא ״עקרון הרדיפה״.","עקרון ההמשכיות (ניצול הצלחה / רדיפה): צד שהשיג יתרון חייב ללחוץ ברציפות. ההיגיון אוניברסלי, וסון טסו מסכים."],
["cont",2,"מה הצד החלש מנסה לעשות לפי היגיון ״ניתוק ההמשכיות״?",["לנתק מגע – נסיגה, הפסקת אש או משיכת משא ומתן – כדי לבנות כוח מחדש","להתקיף מיד בכל הכוח, כדי להפתיע את הצד החזק","להמשיך ללחום בלי הפסקה עד שהאויב יתעייף","לפזר את צבאו לחלוטין ולוותר על המלחמה"],"מה צריך מי שמפסיד? זמן.","הצד החלש רוצה לנתק את ההמשכיות – באמצעות נסיגה, הפסקת אש או משיכת מו״מ – כדי לבנות כוח."],
["cont",2,"מהו ״עקרון ההמתנה״ של קלאוזביץ?",["היפוך עקרון ההמשכיות: הסיבה ההגיונית היחידה להפסקה בלחימה היא שצד ממתין למצב נוח יותר","עיקרון שלפיו יש להמתין תמיד שהאויב יתקוף ראשון","עיקרון שלפיו יש להמתין עם המלחמה עד שהטכנולוגיה תשתפר","עיקרון שלפיו המפקד ממתין לפקודה מהדרג המדיני לפני כל קרב"],"אז למה בפועל יש כל כך הרבה הפסקות?","עקרון ההמתנה הופך את עקרון ההמשכיות. בפועל יש הפסקות בגלל עליונות ההגנה ובגלל עקרון הידע החסר."],
["cont",2,"מהן שתי הסיבות שבגללן יש בפועל הפסקות במלחמה?",["עליונות ההגנה על ההתקפה, ו״עקרון הידע החסר״ (מודיעין לקוי גורם לתוקף לא לדעת שיש לו יתרון)","מזג אוויר קשה בחורף, ומחסור בתחמושת ובמזון אצל שני הצדדים","חגים דתיים משותפים לשני הצדדים, ולחץ של מדינות ניטרליות באזור","הוראות של גופים בין-לאומיים, והתנגדות של הצבא להחלטות הדרג המדיני"],"אחת קשורה להגנה, השנייה למודיעין.","(1) עליונות ההגנה – קל יותר להחזיק שטח מלכבוש; (2) עקרון הידע החסר – גם עם יתרון, התוקף לא תמיד יודע עליו."],
["cont",3,"בדוגמת הדיביזיות של קלאוזביץ: 100 מול 100, וההגנה כפולה בעוצמתה. כמה דיביזיות צריך התוקף?",["200 דיביזיות – אחרת צפוי חוסר פעולה","100 דיביזיות – מספר שווה מספיק לתוקף","150 דיביזיות – יתרון של 50% מספיק תמיד","50 דיביזיות – ההגנה חלשה מההתקפה"],"ההגנה ״כפולה״.","אם ההגנה חזקה פי שניים, התוקף צריך פי שניים כוחות – 200 דיביזיות. אחרת שני הצדדים ממתינים, וזה מסביר את ההפסקות."],
["cont",2,"מהי ״נקודת שיא ההתקפה״ (נקודת שיא הניצחון)?",["הנקודה שבה המשך ההתקפה עלול להפוך לחיסרון – כוח התוקף נשחק ומאזן הכוחות עומד להתהפך","הרגע שבו התוקף מגיע פיזית לבירת האויב וכובש אותה, ובכך מסיים את המלחמה","הנקודה שבה מושגת הכרעה דיפלומטית בשולחן המשא ומתן, עוד לפני הקרב המכריע","הרגע שבו יש להפעיל את מרב הכוח הצבאי בבת אחת, כדי להשמיד את צבא האויב"],"ככל שההתקפה מצליחה – עוצמתה נחלשת.","ככל שהתוקף מתקדם הוא מתרחק מבסיסי ההספקה, נחשף באגפים ומתעייף. נקודת השיא דינמית ואי אפשר לזהות אותה באופן אובייקטיבי."],
["cont",2,"איזה מהבאים הוא חיסרון להתקדמות התוקף?",["התוקף מתרחק מבסיסי ההספקה שלו, ואילו המגן מתקרב לשלו","המגן מאבד שטח ומשאבים, והתוקף מתכלכל על חשבונו","אבדות המגן כבדות יותר והוא מאבד מחסנים ומצבורים","המגן מאבד לכידות ובעלי ברית ומתייאש במידת מה"],"שלוש התשובות האחרות הן יתרונות.","חסרונות התוקף: צריך להטיל מצור, לאייש שטח עוין, להתרחק מההספקה, ובעלי ברית באים לעזרת המגן. השאר הם יתרונות ההתקדמות."],
["cont",3,"מה הסתירה בין עקרון ההמשכיות לנקודת השיא?",["ההמשכיות מחייבת לנצל את ההצלחה עד הסוף, ונקודת השיא מחייבת זהירות – והנועזים עלולים ״לחצות את קו השיא בלי שיחושו בכך״","ההמשכיות מחייבת לעצור מיד אחרי כל הצלחה, ונקודת השיא מחייבת להמשיך בכל מחיר","אין ביניהם סתירה – שני המושגים אומרים בדיוק אותו דבר במילים שונות","ההמשכיות שייכת לסון טסו ונקודת השיא למאו, ולכן אין ביניהן קשר תיאורטי"],"קלאוזביץ נוטה למפקד הנועז – אבל מזהיר.","קלאוזביץ נוטה למפקד הנועז שרודף ללא רחמים, אבל מזהיר שהנועזים עלולים לחצות את קו השיא בלי להרגיש."],
["cont",2,"מה חשוב במעבר מהגנה להתקפה לפי קלאוזביץ?",["העיתוי הוא הכול – מוקדם מדי: סכנת תבוסה; מאוחר מדי: האויב מתבצר או נסוג בסדר","המספרים הם הכול – צריך פי שלושה כוחות מהאויב לפני כל מעבר להתקפה","מזג האוויר הוא הכול – אין לעבור להתקפה בעונת הגשמים או בחורף","אין חשיבות לעיתוי – אפשר לעבור להתקפה בכל רגע, כל עוד הכוחות מוכנים"],"מתקפת נגד מיד כשהתוקף מיצה את תנופתו.","מעבר מוקדם מדי מסכן בתבוסה; מאוחר מדי – האויב מתבצר או נסוג בסדר ומתקפת הנגד מתייקרת."],
["cont",2,"מהם שלושת השלבים של מלחמה ממושכת לפי מאו?",["הגנה אסטרטגית ← שיווי משקל/קיפאון ← מתקפת נגד","התקפה מהירה ← הגנה עיקשת ← משא ומתן לסיום","גיוס כללי ← אימון הצבא ← לחימה מכרעת","מודיעין ← הונאה ← הכרעה בקרב אחד גדול"],"המעבר ביניהם הדרגתי.","מאו: הגנה אסטרטגית ← שיווי משקל ← מתקפת נגד. בשלבים המוקדמים – ניתוק מגע והימנעות מקרב בתנאי האויב (כמו פריקלס ופביוס)."],
["cont",3,"מה ההבדל בין מאו לקלאוזביץ במעבר בין הגנה להתקפה?",["קלאוזביץ – שני מצבים בלבד ומתקפת נגד מיד כשהתוקף מיצה תנופתו; מאו – שלושה שלבים, מעבר הדרגתי ושיווי משקל ממושך אפשרי","קלאוזביץ – שלושה שלבים הדרגתיים ושיווי משקל ממושך; מאו – שני מצבים ומתקפת נגד מיידית","שניהם מתארים שלושה שלבים זהים לחלוטין, אך משתמשים במונחים שונים","שניהם מתארים שני מצבים בלבד – הגנה והתקפה – ללא אפשרות לשיווי משקל ממושך"],"מושגי מפתח: ״נקודת השיא״ מול ״הנקודה הסופית לנסיגה״.","קלאוזביץ: הגנה והתקפה, ונקודת שיא הניצחון. מאו: שלושה שלבים הדרגתיים, ו״הנקודה הסופית לנסיגה״."],
["cont",3,"מה עמדת קלאוזביץ ברמה המערכתית כשיש מידע חסר?",["עדיף לשמור על היוזמה ולהמשיך – הזמן עלול לפעול לטובת היריב וקשה לחדש פעילות","עדיף לעצור תמיד ולהמתין עד שהמודיעין יהיה מושלם","עדיף לסגת מיד ולחזור לקווי הפתיחה","עדיף להעביר את ההחלטה לדרג המדיני"],"היתרון המערכתי צריך להיתרגם ליתרון בשולחן המו״מ.","קלאוזביץ: גם עם מידע חסר – לשמור על היוזמה. יתרון מערכתי צריך להפוך ליתרון אסטרטגי ומדיני."],
["end",2,"איזה הוגה הקדיש פרק מיוחד לסיום המלחמה?",["מקיאוולי","קלאוזביץ","סון טסו","ז׳ומיני"],"השאר ראו בו תהליך נפרד באחריות המדינאים.","רק מקיאוולי מקדיש פרק מיוחד לסיום המלחמה. השאר רואים בו תהליך נפרד שבאחריות המדינאים."],
["end",2,"מה אומר קלאוזביץ על סופיות תוצאת המלחמה?",["״במלחמה התוצאה לעולם אינה סופית״ – המדינה המובסת רואה בה לעיתים רע זמני","התוצאה תמיד סופית, כי הצד המובס מפורק מנשקו לחלוטין","התוצאה סופית רק אם הבירה נכבשה","התוצאה תלויה רק בהחלטת בעלות הברית"],"המובס מחכה לתנאים מדיניים אחרים.","המדינה המובסת מתייחסת לעיתים לתוצאה כ״רע זמני בלבד״. לכן שלום מתמשך דורש להתחשב באינטרסים של המובס – זה עניין הדדי."],
["end",2,"מה הפרדוקס לגבי ניצחון מרשים בסיום המלחמה?",["ככל שהניצחון מרשים יותר, קשה למנצח ״השיכור מהישגו״ להכיר בצורך בתהליך מדיני","ככל שהניצחון מרשים יותר, כך המובס מקבל אותו בקלות רבה יותר","ניצחון מרשים תמיד מבטיח שלום נצחי","אין פרדוקס – ניצחון מרשים הוא תמיד סוף המלחמה"],"ניצחון צבאי = תנאי הכרחי אך לא מספיק.","סופיות המלחמה היא תהליך מדיני. ככל שהניצחון מרשים יותר, קשה יותר למנצח להכיר בכך."],
["end",2,"לפי מקיאוולי, אילו שתי אפשרויות קיצון נקטו הרומאים כלפי אויב מובס?",["לאבד, לפזר ולשעבד אותו – או להעניק לו תנאים נדיבים של שוויון","לגבות ממנו מס גבוה – או לגרש אותו מארצו לנצח","לכרות עמו ברית צבאית – או להכריז עליו מלחמה מחדש","להעמיד אותו למשפט – או לשחרר אותו בלי תנאים"],"או הכול – או נדיבות מלאה.","הרומאים נמנעו מ״דרך האמצע״: או השמדה ושעבוד, או תנאים נדיבים של שוויון."],
["end",2,"מהן שלוש המטרות לפירוק האויב מנשקו לפי קלאוזביץ?",["השמדת כוחותיו, כיבוש ארצו ושבירת רצון הלחימה שלו","שיבוש בריתותיו, הונאתו ותקיפת ערים","מצור כלכלי, תעמולה ומשא ומתן","הפתעה, ריכוז כוח ונסיגה"],"בדרך כלל שתי הראשונות מספיקות להביאו למו״מ.","(1) השמדת כוחותיו; (2) כיבוש ארצו; (3) שבירת רצון הלחימה. בדרך כלל 1+2 מספיקים כדי להביאו למשא ומתן."],
["end",3,"מהן הסיבות המעשיות לעשיית שלום, מלבד פירוק האויב מנשקו?",["סבירות ניצחון נמוכה, או מחיר ניצחון גבוה מדי","לחץ של התקשורת, או רצון לחסוך בתקציב הביטחון","החלפת שלטון אצל האויב, או חגים לאומיים","פקודה של בעלות הברית, או החלטה של המפקד בשטח"],"חישוב של עלות-תועלת.","סבירות ניצחון נמוכה או מחיר גבוה מדי. אבל החישוב קשה ליישום: קשה לכמת, ההערכות משתנות ומשאלת לב גורמת לחשוב ש״המתקפה הבאה תכריע״."],
["end",3,"מה הבעיה בסיום מלחמה במשא ומתן כשאין הכרעה צבאית?",["כל צד רואה את אותו מצב אחרת, ובמבוי סתום כל צד חושש שוויתור ייראה כחולשה","המשא ומתן תמיד מסתיים מהר מדי ולכן אינו יציב","אין בעיה – משא ומתן תמיד מצליח כשאין הכרעה צבאית","המשא ומתן אסור לפי כל ההוגים, ולכן אינו אפשרי"],"פעילות גומלין בשדה ובשולחן.","כשאין הכרעה – מסיימים במשא ומתן תוך פעילות גומלין בשדה ובשולחן. הקושי: תפיסות שונות של אותו מצב, וחשש שוויתור ייראה כחולשה."],
["intel",1,"מה הקשר בין הונאה, הפתעה ומודיעין?",["הונאה היא הדרך היעילה ביותר להשיג הפתעה; מודיעין מהימן מונע הפתעה והונאה","מודיעין הוא הדרך להשיג הונאה; הפתעה מונעת מודיעין","שלושתם מושגים נפרדים שאין ביניהם קשר","הפתעה היא הדרך להשיג מודיעין; הונאה מונעת הפתעה"],"שני הראשונים הם תת-קטגוריות של המודיעין.","הונאה ← הפתעה. מודיעין מהימן מונע את שתיהן."],
["intel",1,"מה עמדת קלאוזביץ כלפי הונאה?",["אינו מחשיב אותה – היא ״המפלט האחרון של החלש והנואש״","רואה בה את השיטה העיקרית לניצחון בכל הרמות","טוען שהיא חשובה רק ברמה האסטרטגית-מדינית","רואה בה את מכפיל הכוח החשוב ביותר"],"הוא בוחן אותה ברמה המערכתית-טקטית.","קלאוזביץ בוחן הונאה ברמה המערכתית-טקטית, שם היא פחות בטוחה ויעילה. סון טסו בוחן אותה ברמה האסטרטגית – שם היא יעילה מאוד."],
["intel",2,"מה גישתו של קלאוזביץ להפתעה אסטרטגית?",["כמעט בלתי אפשרית להשגה ברמות האסטרטגית והמערכתית הגבוהה – ולכן גם ההונאה מיותרת שם","אפשרית תמיד ורצויה בכל מצב, ברמה האסטרטגית בעיקר","בלתי אפשרית ברמה הטקטית, אך קלה להשגה ברמה האסטרטגית","היא השורש לכל מהלך מדיני חשוב"],"זו בדיוק שאלת הדוגמה מהנחיות המרצה!","קלאוזביץ סבור שהפתעה כמעט בלתי אפשרית ברמות האסטרטגית והמערכתית הגבוהה. אצל סון טסו – הפתעה אפשרית ורצויה תמיד."],
["intel",1,"מהי גישת סון טסו למודיעין?",["מכפיל כוח מרכזי: ״צבא ללא סוכנים חשאיים משול לאדם ללא עיניים ואוזניים״","מקור של רעש וחיכוך שאי אפשר לסמוך עליו, ועדיף להסתמך על אינטואיציה","דבר מיותר, כי המפקד המיומן רואה בעצמו את כל מה שקורה בשדה הקרב","כלי שמתאים בעיקר לדיפלומטים בימי שלום, ופחות למצביא בזמן מלחמה"],"״עיניים ואוזניים״.","אצל סון טסו המודיעין הוא מכפיל כוח מרכזי, בשליטה ישירה של המצביא. אצל קלאוזביץ – אין לסמוך עליו."],
["intel",2,"מדוע קלאוזביץ סקפטי לגבי מודיעין?",["הוא רואה בו לרוב עוד מקור של רעש וחיכוך שאי אפשר לסמוך עליו","הוא טוען שמודיעין אסור מבחינה מוסרית","הוא סבור שמודיעין תמיד מדויק מדי ומבלבל את המפקד","הוא חושב שרק הדרג המדיני צריך לקבל מודיעין"],"ערפל הקרב.","קלאוזביץ רואה במודיעין במלחמה לעיתים קרובות מידע סותר ושגוי – עוד מקור לחיכוך."],
["intel",3,"מהם שלושת ״תחליפי המודיעין״ של קלאוזביץ?",["אינטואיציית הגאון הצבאי, עוצמה חומרית, ואמנות המלחמה","מרגלים חשאיים, סיורים רגליים ותצפיות מנקודות גבוהות","הונאה יזומה, הפתעה אסטרטגית ותמרון מהיר באגפים","דיפלומטיה, לחץ כלכלי ותעמולה בקרב אוכלוסיית האויב"],"אחד מהם הוא ״טביעת העין״.","מאחר שאי אפשר לסמוך על מודיעין, קלאוזביץ מציע: (1) אינטואיציית הגאון הצבאי; (2) עוצמה חומרית; (3) אמנות המלחמה."],
["intel",2,"מהי התחבולה המועדפת על סון טסו?",["להעמיד פני חלש – כך מחזקים את מה שהאויב כבר מאמין ויוצרים תחושת ביטחון מוטעית","להעמיד פני חזק – כדי להפחיד את האויב ולגרום לו לסגת","לחשוף את התוכניות בכוונה – כדי שהאויב יחשוב שזו הונאה","לפזר שמועות על מגפה בצבא – כדי שהאויב יימנע מתקיפה"],"״כאשר אתה מסוגל – העמד פני אינך מסוגל״.","העמדת פני חלש מחזקת את מה שהאויב כבר מאמין ויוצרת אצלו ביטחון מוטעה."],
["intel",2,"מה הם ״צ׳נג״ ו״צ׳י״ אצל סון טסו?",["צ׳נג – הכוח ה״רגיל״/ישיר שמרתק או מסיח; צ׳י – הכוח ה״יוצא דופן״/עקיף שמכה במכה המכרעת – והם יכולים להחליף תפקידים","צ׳נג – ההגנה; צ׳י – ההתקפה, ולעולם אינם מחליפים תפקידים במהלך הקרב","צ׳נג – איסוף המודיעין; צ׳י – הלוגיסטיקה וההספקה של הצבא בשטח","צ׳נג – הדרג המדיני שקובע מטרות; צ׳י – הדרג הצבאי שמבצע אותן"],"שני כוחות מתואמים.","צ׳נג מרתק את האויב, צ׳י מכה באגף או בנקודה החלשה. הם יכולים להחליף תפקידים – וזה מה שהופך אותם לבלתי צפויים."],
["intel",2,"באילו רמות מפעיל סון טסו הונאה?",["דיפלומטית (טריז בין האויב לבעלי בריתו), פוליטית (חתרנות בתוך צבא האויב) וצבאית","רק ברמה הטקטית של הקרב הבודד, ולא לפני פרוץ המלחמה","רק ברמה הכלכלית, באמצעות זיוף מטבעות ושיבוש המסחר של האויב","רק כלפי הצבא שלו עצמו, כדי לשמור על סודיות התוכניות"],"תמיד, לפני ובמהלך המלחמה.","סון טסו מגדיר הונאה באופן רחב – אמצעים פעילים וסבילים – ומפעיל אותה בכל הרמות: דיפלומטית, פוליטית וצבאית."],
["intel",3,"מהי הביקורת על גישת סון טסו להונאה?",["הוא כמעט מתעלם מכך שגם האויב מונה – ההונאה אינה פתרון זול או תרופת פלא","הוא מתנגד להונאה, ולכן מפסיד בכל מלחמה","הוא רואה בהונאה דבר לא מוסרי ולכן אינו משתמש בה","אין ביקורת – ההונאה תמיד מצליחה"],"״חרב פיפיות״.","לאף צד אין מונופול על ההונאה – היא חרב פיפיות. סון טסו נוטה לראות בה פתרון ״זול״ ואף ״תרופת פלא״."],
["intel",2,"מה הלקח המודרני לגבי מודיעין והונאה?",["עצותיו של סון טסו בנושא המודיעין רלוונטיות יותר לימינו; אחרי ויטנאם ניתנה תשומת לב מוגברת למודיעין ולהונאה","עצותיו של קלאוזביץ בנושא המודיעין רלוונטיות יותר; בעידן המודרני אין צורך בהונאה","מודיעין והונאה איבדו את חשיבותם בעידן הטכנולוגי","אחרי ויטנאם הוחלט לבטל את יחידות המודיעין"],"מרכיבים לא חומריים שהוזנחו בעבר.","בנושא המודיעין, עצותיו של סון טסו רלוונטיות יותר. אחרי ויטנאם הוקדשה תשומת לב מוגברת למודיעין ולהונאה."],
["lead",1,"מהי ״טביעת העין״ (coup d׳oeil) לפי קלאוזביץ?",["האינטואיציה של הגאון הצבאי, שמאפשרת לו לקרוא את המצב ולפצות על מודיעין חסר","מכשיר אופטי לתצפית על שדה הקרב מנקודה גבוהה, שפותח בפרוסיה","היכולת לזכור בעל-פה את כל המפות והתוכניות לפני הקרב","מבט מאיים של המפקד שנועד לשמור על משמעת בקרב חייליו"],"״הפגנה מופלאה של ראיית הנולד״.","המפקד אינו יכול להתמודד עם הכאוס בלי ״טביעת העין״ – צורה נעלה של כושר ניתוח."],
["lead",2,"מהי הסכנה בהסתמכות על הגאון הצבאי?",["היא פוגעת בדחף לחפש מודיעין טוב – במקום חיפוש שיטתי נשארת האינטואיציה לבדה","היא גורמת למפקדים להיות זהירים מדי ולהימנע מכל סיכון בשדה","היא מובילה לכך שהדרג המדיני משתלט על הצבא ומנהל את הקרבות","אין סכנה כזו – לפי הקורס זו הגישה האידיאלית לניהול מלחמה"],"מה קורה כשסומכים רק על תחושת בטן?","התוצאה המזיקה ביותר: נפגע הדחף להשיג את המודיעין הטוב ביותר האפשרי."],
["lead",2,"מה ההבדל בהעדפת המפקד בין קלאוזביץ לסון טסו?",["קלאוזביץ – תעוזה על פני שיקול דעת; סון טסו – זהירות וחישוב וסיכונים מחושבים","קלאוזביץ – זהירות וחישוב; סון טסו – תעוזה על פני שיקול דעת","שניהם מעדיפים תעוזה בכל מצב","שניהם מעדיפים זהירות בכל מצב"],"״עדיף כישלון אצילי מחוסר פעולה״.","קלאוזביץ: תעוזה – עדיף כישלון אצילי מחוסר פעולה. סון טסו: זהירות וחישוב."],
["lead",2,"לפי תורת המשחקים, איזה סגנון מאפיין כל הוגה?",["קלאוזביץ – מקסי-מקס (סיכון מרבי, רווח מרבי, סגנון רומל); סון טסו – מיני-מקס (סיכון מזערי, רווח מרבי, סגנון מונטגומרי)","קלאוזביץ – מיני-מקס (סיכון מזערי, סגנון מונטגומרי); סון טסו – מקסי-מקס (סיכון מרבי, סגנון רומל)","שניהם – מקסי-מקס (סיכון מרבי ורווח מרבי), כמו סגנונו של רומל","שניהם – מיני-מקס (סיכון מזערי ורווח מרבי), כמו סגנונו של מונטגומרי"],"רומל הנועז מול מונטגומרי הזהיר.","קלאוזביץ – מקסי-מקס, סגנון רומל. סון טסו – מיני-מקס, סגנון מונטגומרי."],
["lead",2,"איך מערערים את האויב לפי כל אחד מההוגים?",["סון טסו – להכעיס ולבלבל את מצביאו ולגרום לו לפעול בלי לחשוב; קלאוזביץ – לחץ בלתי פוסק שלא משאיר זמן לפעולה מחושבת","סון טסו – לחץ בלתי פוסק שלא משאיר זמן לחשוב; קלאוזביץ – להכעיס ולבלבל את המצביא","שניהם – באמצעות משא ומתן ממושך שמתיש את האויב ושוחק את סבלנותו","שניהם – באמצעות הימנעות מכל מגע, עד שהאויב יתייאש ויסוג מעצמו"],"״הכעס את המצביא שלו ובלבל אותו״.","סון טסו: לגרום לאויב לפעול בלי לחשוב. קלאוזביץ: לחץ בלתי פוסק – כל פעולה מערכתית נועדה לבלבל את האויב."],
["lead",3,"מה אומר קלאוזביץ על אינטליגנציה אצל המצביא?",["״אינטליגנציה לבד אינה אומץ; לעיתים קרובות האנשים האינטליגנטים ביותר הם הססנים״","אינטליגנציה היא התכונה החשובה ביותר אצל מפקד, יותר מאומץ ומנחישות","מפקד צריך להיות אינטליגנטי פחות מחייליו, כדי שלא יהסס לפני קרב","אינטליגנציה ואומץ הם בעצם אותה תכונה, ולכן אי אפשר להפריד ביניהן"],"ערך המפקד – אומץ.","קלאוזביץ אינו סבור שאינטליגנציה היא התכונה הרצויה ביותר. אצל סון טסו, ערך המפקד נובע מחישוב רציונלי תחת לחץ."],
["lead",3,"מה החשש המרכזי של כל הוגה לגבי המצביא?",["קלאוזביץ – ירידת התעוזה ככל שעולים בדרגה; סון טסו – מצביא נמהר שמאבד שליטה וקל לתמרן אותו","קלאוזביץ – מצביא נמהר שקל לתמרן אותו; סון טסו – ירידת התעוזה בדרגים הגבוהים","שניהם – מצביא שאינו מכיר את השטח ואינו יודע לקרוא מפה","שניהם – מצביא שמבקר בפומבי את הדרג המדיני ופוגע בסמכותו"],"״אומץ ללא היגיון = הרס עצמי״.","קלאוזביץ חושש מירידת התעוזה בדרגים הגבוהים. סון טסו חושש ממצביא נמהר שמאבד שליטה."],
["lead",2,"במה מסכימים סון טסו וקלאוזביץ לגבי תכונות המפקד?",["יציבות, נחישות, שליטה עצמית וקור רוח חיוניים; לא כל חייל טוב יהיה מפקד טוב","מפקד טוב צריך להיות רחמן ורגיש כלפי האויב, כדי לזכות באמונו","כל חייל טוב יהיה בהכרח גם מפקד טוב, אם רק יקבל חינוך מתאים","מפקד צריך לחזור על הטקטיקה שהצליחה לו בעבר, כדי לא להסתכן"],"סון טסו גם מזהיר שרחמנות עלולה לפגום.","שניהם: יציבות, נחישות, שליטה עצמית וקור רוח. חינוך וניסיון אינם מספיקים, וצריך גם יצירתיות – לא לחזור על טקטיקות."],
["lead",3,"מהי ״אירוניית הניסיון״ בדוגמת נפוליאון?",["התכונות שהביאו לו ניצחונות בקרב (ארקולה, ינה) גרמו לנפילתו ברמה האסטרטגית, שם חישוב זהיר עדיף","נפוליאון הפסיד כמעט בכל הקרבות, ובכל זאת ניצח במלחמות עצמן","נפוליאון לא צבר כל ניסיון קרבי לפני שהוכתר לקיסר, ולכן נכשל","הניסיון הרב של נפוליאון גרם לו להיות זהיר מדי ברמה הטקטית"],"טקטיקיזציה של האסטרטגיה.","אותן תכונות שאפשרו לו לנצח בארקולה וינה הכשילו אותו כשהופעלו באסטרטגיה. מאחר שקלאוזביץ עוסק ברמה המערכתית, סביר שהיה ממליץ על זהירות רבה יותר ברמה האסטרטגית."],
["lead",2,"מה מקומו של המנהיג הצבאי בתיאוריה של כל הוגה?",["אצל קלאוזביץ – מרכזי; אצל סון טסו – פחות מרכזי (אף ש״אמן המלחמה״ דומה מאוד ל״גאון הצבאי״)","אצל סון טסו – מרכזי; אצל קלאוזביץ – כמעט אינו מוזכר בספר","אצל שניהם – אינו מוזכר כלל, כי שניהם עסקו רק במדיניות","אצל שניהם – המנהיג הצבאי חשוב יותר מהדרג המדיני וכפוף רק לעצמו"],"הגאון הצבאי הוא רעיון של קלאוזביץ.","קלאוזביץ מפתח את רעיון הגאון הצבאי. אצל סון טסו תפקיד המפקד פחות מרכזי – אף ש״אמן המלחמה״ ו״המפקד המיומן״ אינם שונים בהרבה."]
];
const WHO = [
["״הבסת האויב ללא לחימה היא שיא הכשרון״","S","הטיפוס האידיאלי של סון טסו – ניצחון בלי קרב."],
["המלחמה היא מעשה של כוח שמטרתו לאכוף על האויב לעשות כרצוננו","C","הגדרת המלחמה של קלאוזביץ."],
["״אנשים, לא עצמים, הם המכריעים״","M","מאו הזהיר מהסתמכות יתר על נשק וטכנולוגיה."],
["חיכוך – ״הכול במלחמה פשוט מאוד, אך גם הדבר הפשוט ביותר קשה״","C","מושג החיכוך שייך לקלאוזביץ."],
["צ׳נג וצ׳י – כוח ישיר וכוח עקיף שמחליפים תפקידים","S","צמד הכוחות של סון טסו."],
["השילוש הפרדוקסלי: העם, המצביא וצבאו, הממשלה","C","השילוש של קלאוזביץ."],
["המלחמה היא אמנות ולא מדע","B","עמדה משותפת לסון טסו ולקלאוזביץ."],
["ניסה לבנות תיאוריה מדעית של המלחמה","J","ז׳ומיני – ומעולם לא הודה במלואו שזו אמנות."],
["הקדיש פרק מיוחד לסיום המלחמה","MA","רק מקיאוולי עשה זאת."],
["הערכה נטו יכולה להפיק תמונה אובייקטיבית ומדויקת","M","מאו, בהשראת סון טסו והמטריאליזם הדיאלקטי."],
["הונאה היא ״המפלט האחרון של החלש והנואש״","C","קלאוזביץ אינו מחשיב הונאה."],
["״צבא ללא סוכנים חשאיים משול לאדם ללא עיניים ואוזניים״","S","המודיעין כמכפיל כוח אצל סון טסו."],
["נקודת שיא ההתקפה","C","ככל שההתקפה מצליחה – עוצמתה נחלשת."],
["שלושה שלבים: הגנה אסטרטגית, שיווי משקל, מתקפת נגד","M","המלחמה הממושכת של מאו."],
["אחרי פרוץ המלחמה – עדיפות לשיקולים הצבאיים","J","בפועל, עליונות הצבא על המדיניות."],
["חופש פעולה מרבי למפקד, כמו ברומא","MA","פיקוח ״בשלט רחוק״ הכשיל את ערי איטליה."],
["רפובליקות מסתגלות טוב יותר כי הן מחליפות מנהיגים","MA","מקיאוולי על דמוקרטיות ומשטרים סמכותיים."],
["סדר תקיפה: תוכניות ← בריתות ← צבא ← ערים","S","סדר העדיפויות של סון טסו."],
["סדר תקיפה: צבא ← בירה ← בעל ברית ← דעת קהל","C","סדר העדיפויות של קלאוזביץ."],
["להעמיד פני חלש כדי ליצור אצל האויב ביטחון מוטעה","S","התחבולה המועדפת של סון טסו."],
["עדיף כישלון אצילי מחוסר פעולה","C","קלאוזביץ מעדיף תעוזה."],
["מיני-מקס: סיכון מזערי, רווח מרבי","S","סגנון ״מונטגומרי״."],
["מקסי-מקס: סיכון מרבי, רווח מרבי","C","סגנון ״רומל״."],
["עקרון ההמתנה – הסיבה היחידה להפסקה היא המתנה למצב נוח יותר","C","היפוך של עקרון ההמשכיות."],
["המלחמה צריכה להיות קצרה ומכרעת","B","הסכמה בין שני ההוגים."],
["אחרי מודיעין והערכה נטו – אפשר לחזות בדייקנות את התוצאה","S","קלאוזביץ חולק – חיזוי בלתי אפשרי."],
["לא מאמין בגאונות – עבודה קשה, למידה והסתגלות","M","מאו מול הגאון הצבאי של קלאוזביץ."],
["״הכעס את המצביא שלו ובלבל אותו״","S","לגרום לאויב לפעול בלי לחשוב."],
["״אינטליגנציה לבד אינה אומץ״","C","האינטליגנטים ביותר הם לעיתים הססנים."],
["המלחמה חייבת להיות בשליטת הדרג המדיני","B","שניהם – אך אף אחד לא נתן קריטריונים להפרת פקודה."],
["״הנקודה הסופית לנסיגה״","M","מושג המפתח של מאו."],
["מודע מאוד לחשיבות החימוש והטכנולוגיה המודרנית","J","ז׳ומיני זיהה את ראשית המהפכה התעשייתית."],
["עוצמה צבאית = אמצעים חומריים × כוח רצון","C","הגורמים הנפשיים חשובים יותר מהחומריים."],
["את המלחמה יש לחקור כמכלול (גשטלט)","C","לא ניתוח ליניארי."],
["הרומאים: או להשמיד ולשעבד – או לתת תנאים נדיבים","MA","שתי אפשרויות הקיצון של רומא."],
["עדיפות יחסית בנקודת ההכרעה – לא יתרון מספרי מוחלט","B","הסכמה בין שני ההוגים."],
["״כמו שלמים אין צורה קבועה, כך אין תנאים קבועים במלחמה״","S","סון טסו על המורכבות האינסופית."],
["״חיוני לא לצעוד את הצעד הראשון בלי להביא בחשבון את האחרון״","C","לקח שאומץ אחרי ויטנאם."],
["הגישה העקיפה","S","אחד ממכפילי הכוח של סון טסו."],
["״במלחמה התוצאה לעולם אינה סופית״","C","המובס רואה בה ״רע זמני״."]
];

</script>
<script>
"use strict";
// ═════════ עזרים ═════════
const $ = s => document.querySelector(s);
const app = $("#app");
const esc = s => String(s).replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const shuffle = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.random() * (i + 1) | 0; [a[i], a[j]] = [a[j], a[i]]; } return a; };
const LETTERS = ["א","ב","ג","ד"];
const fmtTime = s => `${Math.floor(s/60)}:${String(Math.floor(s%60)).padStart(2,"0")}`;
const money = n => n.toLocaleString("he-IL") + " ₪";
QUESTIONS.forEach((q, i) => q.id = i);
const Q = i => ({ id: i, topic: QUESTIONS[i][0], diff: QUESTIONS[i][1], text: QUESTIONS[i][2], opts: QUESTIONS[i][3], hint: QUESTIONS[i][4], expl: QUESTIONS[i][5] });
const ALLQ = QUESTIONS.map((_, i) => Q(i));
const THINKERS = {
  S:  { name: "סון טסו", e: "🐉" },
  C:  { name: "קלאוזביץ", e: "⚔️" },
  B:  { name: "שניהם", e: "🤝" },
  M:  { name: "מאו", e: "⭐" },
  J:  { name: "ז׳ומיני", e: "📐" },
  MA: { name: "מקיאוולי", e: "🏛️" }
};
const RANKS = [
  [0,"טוראי"],[60,"רב״ט"],[150,"סמל"],[280,"סמ״ר"],[450,"סג״ם"],[650,"סגן"],[900,"סרן"],
  [1200,"רס״ן"],[1600,"סא״ל"],[2100,"אל״מ"],[2700,"תא״ל"],[3400,"אלוף"],[4300,"רא״ל"]
];

// ═════════ שמירה מקומית (בטוחה) ═════════
const KEY = "mil-thought-game-v1";
let save = { name: "", xp: 0, stats: {}, best: { mil: 0, blitz: 0, exam: 0 }, sound: true };
try { const raw = localStorage.getItem(KEY); if (raw) save = Object.assign(save, JSON.parse(raw)); } catch (e) {}
function persist() { try { localStorage.setItem(KEY, JSON.stringify(save)); } catch (e) {} }
// stats[id] = {c: נכון, w: שגוי, last: 1/0}
function record(id, ok) {
  const s = save.stats[id] || (save.stats[id] = { c: 0, w: 0, last: 0 });
  ok ? s.c++ : s.w++; s.last = ok ? 1 : 0;
  if (ok) addXP(5 + 5 * QUESTIONS[id][1]);
  persist();
}
function rankOf(xp) { let r = 0; RANKS.forEach((x, i) => { if (xp >= x[0]) r = i; }); return r; }
function addXP(n) {
  const before = rankOf(save.xp); save.xp += n; persist();
  const after = rankOf(save.xp);
  if (after > before) setTimeout(() => toast(`🎖️ קידום! הדרגה החדשה שלך: ${RANKS[after][1]}`), 400);
  renderChips();
}
function topicMastery(t) {
  const qs = ALLQ.filter(q => q.topic === t);
  const seen = qs.filter(q => save.stats[q.id]);
  const good = qs.filter(q => save.stats[q.id] && save.stats[q.id].last === 1).length;
  return { total: qs.length, seen: seen.length, pct: Math.round(100 * good / qs.length) };
}
const mistakes = () => ALLQ.filter(q => save.stats[q.id] && save.stats[q.id].last === 0);

// ═════════ צלילים ואפקטים ═════════
let actx = null;
function beep(type) {
  if (!save.sound) return;
  try {
    actx = actx || new (window.AudioContext || window.webkitAudioContext)();
    const seq = { ok: [[660,.08],[880,.12]], bad: [[220,.18],[160,.22]], tick: [[1200,.03]], win: [[523,.1],[659,.1],[784,.1],[1046,.25]] }[type];
    let t = actx.currentTime;
    seq.forEach(([f, d]) => {
      const o = actx.createOscillator(), g = actx.createGain();
      o.type = type === "bad" ? "sawtooth" : "triangle"; o.frequency.value = f;
      g.gain.setValueAtTime(.12, t); g.gain.exponentialRampToValueAtTime(.001, t + d);
      o.connect(g).connect(actx.destination); o.start(t); o.stop(t + d); t += d * .9;
    });
  } catch (e) {}
}
const fx = $("#fx"), fctx = fx.getContext("2d"); let parts = [], fxOn = false;
function confetti(n = 120) {
  fx.width = innerWidth; fx.height = innerHeight;
  const cols = ["#e0b04a","#f5d27a","#3fbf7f","#4f8de0","#ffffff","#e0703c"];
  for (let i = 0; i < n; i++) parts.push({ x: innerWidth / 2 + (Math.random() - .5) * 200, y: innerHeight * .35, vx: (Math.random() - .5) * 14, vy: -Math.random() * 13 - 4,
    s: 5 + Math.random() * 6, r: Math.random() * 6, vr: (Math.random() - .5) * .3, c: cols[i % cols.length], life: 120 + Math.random() * 60 });
  if (!fxOn) { fxOn = true; requestAnimationFrame(loopFx); }
}
function loopFx() {
  fctx.clearRect(0, 0, fx.width, fx.height);
  parts = parts.filter(p => p.life-- > 0 && p.y < fx.height + 20);
  parts.forEach(p => { p.vy += .35; p.vx *= .99; p.x += p.vx; p.y += p.vy; p.r += p.vr;
    fctx.save(); fctx.translate(p.x, p.y); fctx.rotate(p.r); fctx.fillStyle = p.c; fctx.fillRect(-p.s / 2, -p.s / 4, p.s, p.s / 2); fctx.restore(); });
  if (parts.length) requestAnimationFrame(loopFx); else { fxOn = false; fctx.clearRect(0, 0, fx.width, fx.height); }
}
function toast(msg) {
  const t = document.createElement("div"); t.className = "toast"; t.textContent = msg; document.body.appendChild(t);
  setTimeout(() => t.remove(), 2600);
}

// ═════════ טיימרים ═════════
let timer = null;
function stopTimer() { if (timer) { clearInterval(timer); timer = null; } }

// ═════════ ניווט ═════════
let S = { screen: "home" }; // מצב המסך הנוכחי
function go(screen, extra = {}) { stopTimer(); S = Object.assign({ screen }, extra); render(); scrollTo({ top: 0, behavior: "smooth" }); }
function render() {
  renderChips();
  ({ home: vHome, mil: vMil, milEnd: vMilEnd, blitz: vBlitz, blitzEnd: vBlitzEnd, train: vTrain, trainEnd: vTrainEnd,
     exam: vExam, examEnd: vExamEnd, cards: vCards, cheat: vCheat, examSetup: vExamSetup })[S.screen]();
}
function renderChips() {
  const r = rankOf(save.xp);
  $("#chips").innerHTML = `
    <span class="chip">🎖️ <b>${RANKS[r][1]}</b></span>
    <span class="chip">⚡ <b>${save.xp}</b> XP</span>
    <button class="iconbtn" data-a="sound" title="צליל" aria-label="הפעלה או השתקה של צליל">${save.sound ? "🔊" : "🔇"}</button>`;
}

// ═════════ מסך הבית ═════════
function vHome() {
  const r = rankOf(save.xp), next = RANKS[r + 1];
  const pct = next ? Math.round(100 * (save.xp - RANKS[r][0]) / (next[0] - RANKS[r][0])) : 100;
  const mis = mistakes().length;
  const totalSeen = ALLQ.filter(q => save.stats[q.id]).length;
  app.innerHTML = `
  <section class="hero">
    <div class="vs">🐉<i>מול</i>⚔️</div>
    <h1>סון טסו <span>מול</span> קלאוזביץ</h1>
    <p>משחק הכנה למבחן הסיום: ${ALLQ.length} שאלות אמריקאיות על כל 13 השיעורים, עם הסבר מלא אחרי כל תשובה. אפשר לשחק במיליונר, להתחרות בבליץ, להתאמן לפי נושא ולעשות סימולציה של המבחן.</p>
    <div class="namebox">
      <input id="pname" placeholder="איך קוראים לך? (לתעודה בסוף)" value="${esc(save.name)}" maxlength="24" aria-label="שם השחקן">
    </div>
    <div class="rankcard">
      <div class="rankbadge">הדרגה שלך<b>${RANKS[r][1]}</b></div>
      <div class="xpbar" title="התקדמות לדרגה הבאה"><i style="width:${pct}%"></i></div>
      <div class="rankbadge">${next ? `עוד ${next[0] - save.xp} XP ל<b style="display:inline;font-size:14px">${next[1]}</b>` : "הגעת לדרגה הגבוהה ביותר!"}</div>
    </div>
  </section>

  <div class="section-title">בחרו משימה</div>
  <div class="modes">
    <button class="mode feature" data-a="startMil">
      <span class="tag">הקלאסיקה</span><span class="em">💰</span>
      <h3>מי רוצה להיות מיליונר?</h3>
      <p>15 שאלות שהולכות ומתקשות, שלושה גלגלי הצלה, נקודות ביטחון ב-1,000 ₪ וב-32,000 ₪, ואפשר לפרוש עם הכסף בכל רגע.</p>
      ${save.best.mil ? `<div class="best">🏆 השיא שלך: ${money(save.best.mil)}</div>` : ""}
    </button>
    <button class="mode" data-a="startBlitz">
      <span class="tag">60 שניות</span><span class="em">⚡</span>
      <h3>מי אמר את זה?</h3>
      <p>היגד מופיע על המסך, ואתם מחליטים מהר: סון טסו, קלאוזביץ, שניהם, מאו, ז׳ומיני או מקיאוולי. רצף תשובות נכונות מכפיל את הניקוד.</p>
      ${save.best.blitz ? `<div class="best">🏆 השיא שלך: ${save.best.blitz} נק׳</div>` : ""}
    </button>
    <button class="mode" data-a="examSetup">
      <span class="tag">כמו באמת</span><span class="em">📝</span>
      <h3>סימולציית מבחן</h3>
      <p>30 או 40 שאלות, בפריסה מאוזנת בין הנושאים ועם שעון של כ-3 דקות לשאלה. הציון ופירוט לפי נושא מוצגים בסוף.</p>
      ${save.best.exam ? `<div class="best">🏆 הציון הגבוה שלך: ${save.best.exam}</div>` : ""}
    </button>
    <button class="mode" data-a="startMistakes" ${mis ? "" : "disabled style='opacity:.55'"}>
      <span class="tag">${mis} שאלות</span><span class="em">🔁</span>
      <h3>תיקון טעויות</h3>
      <p>${mis ? "כל השאלות שטעיתם בהן, בכל המצבים. שאלה יוצאת מהרשימה אחרי שעניתם עליה נכון." : "עוד אין טעויות לתקן. אחרי שתשחקו, השאלות שטעיתם בהן יחכו לכם כאן."}</p>
    </button>
    <button class="mode" data-a="cards">
      <span class="em">🃏</span>
      <h3>כרטיסיות זיכרון</h3>
      <p>שאלה בצד אחד ותשובה עם הסבר בצד השני. טוב לחזרה מהירה בדרך לקורס.</p>
    </button>
    <button class="mode" data-a="cheat">
      <span class="em">📋</span>
      <h3>דף חזרה מהיר</h3>
      <p>איזה מושג שייך לאיזה הוגה, ומספרים שכדאי לזכור, בטבלה אחת.</p>
    </button>
  </div>

  <div class="section-title">אימון לפי נושא · שליטה ${totalSeen ? `(ענית על ${totalSeen}/${ALLQ.length} שאלות)` : ""}</div>
  <div class="topics">
    ${Object.entries(TOPICS).map(([k, t]) => { const m = topicMastery(k); return `
      <button class="topic" data-a="startTrain" data-t="${k}">
        <div class="ring" style="--p:${m.pct}"><span>${m.pct}%</span></div>
        <div><div class="t">${t.icon} ${t.name}</div><div class="s">${m.total} שאלות · ${m.seen ? `נוסו ${m.seen}` : "עוד לא התחלת"}</div></div>
      </button>`; }).join("")}
  </div>`;
  $("#pname").addEventListener("input", e => { save.name = e.target.value.trim(); persist(); });
}

// ═════════ מיליונר ═════════
const LADDER = [100,200,300,500,1000,2000,4000,8000,16000,32000,64000,125000,250000,500000,1000000];
const SAFE = new Set([4, 9]);
function pickMil() {
  // 5 קלות, 5 בינוניות, 5 קשות – בלי חזרה על נושא ברצף כשאפשר
  const by = d => shuffle(ALLQ.filter(q => q.diff === d));
  return [...by(1).slice(0, 5), ...by(2).slice(0, 5), ...by(3).slice(0, 5)];
}
function prep(q) { // ערבוב תשובות
  const order = shuffle([0, 1, 2, 3]);
  return { q, order, correct: order.indexOf(0) };
}
function startMil() {
  go("mil", { list: pickMil().map(prep), i: 0, life: { f: 1, a: 1, p: 1 }, hidden: [], extra: "", answered: null, hist: [], t0: Date.now() });
}
function vMil() {
  const cur = S.list[S.i], q = cur.q, done = S.answered !== null;
  const banked = S.i ? LADDER[S.i - 1] : 0;
  app.innerHTML = `
  <div class="game">
    <div>
      <div class="qhead">
        <div class="row"><span class="pill gold">שאלה ${S.i + 1} מתוך 15</span><span class="pill">על השאלה: ${money(LADDER[S.i])}</span><span class="pill" id="clock">⏱️ 0:00</span></div>
        <button class="btn ghost" data-a="walk" ${done ? "disabled" : ""} title="פרישה עם הסכום שצברת">🚪 פרוש עם ${money(banked)}</button>
      </div>
      <div class="lifelines">
        <button class="life" data-a="l5050" ${S.life.f && !done ? "" : "disabled"}>✂️ 50:50</button>
        <button class="life" data-a="laud" ${S.life.a && !done ? "" : "disabled"}>👥 עזרת הקהל</button>
        <button class="life" data-a="lphone" ${S.life.p && !done ? "" : "disabled"}>📞 חבר טלפוני</button>
      </div>
      ${S.extra}
      ${qBlock(cur, S.answered, S.hidden)}
      ${done ? feedbackBlock(cur, S.answered, S.answered === cur.correct
          ? (S.i === 14 ? "🏆 לסיום וקבלת המיליון" : "לשאלה הבאה ←")
          : "לסיכום ולמידה ←", "milNext") : `<div class="kbd">אפשר לענות גם במקשים 1–4</div>`}
    </div>
    <aside class="ladder"><h4>סולם הזכיות</h4>
      ${LADDER.map((v, i) => ({ v, i })).reverse().map(({ v, i }) =>
        `<div class="rung ${i === S.i ? "cur" : i < S.i ? "done" : ""} ${SAFE.has(i) ? "safe" : ""}"><span>${i + 1}</span><span>${SAFE.has(i) ? "🛡️ " : ""}${money(v)}</span></div>`).join("")}
    </aside>
  </div>`;
  const tick = () => { const c = $("#clock"); if (c) c.textContent = "⏱️ " + fmtTime((Date.now() - S.t0) / 1000); };
  tick(); timer = setInterval(tick, 1000);
}
function qBlock(cur, answered, hidden = [], sel = null) {
  const q = cur.q;
  return `
  <div class="qbox"><div class="topicname">${TOPICS[q.topic].icon} ${TOPICS[q.topic].name}</div><div class="qt">${esc(q.text)}</div></div>
  <div class="opts" id="opts">
    ${cur.order.map((oi, pos) => {
      let cls = "";
      if (answered !== null) { if (pos === cur.correct) cls = "ok"; else if (pos === answered) cls = "bad"; else cls = "dim"; }
      else if (sel === pos) cls = "sel";
      if (hidden.includes(pos)) cls += " hide";
      return `<button class="opt ${cls}" data-a="ans" data-p="${pos}" ${answered !== null ? "disabled" : ""}><span class="L">${LETTERS[pos]}</span><span>${esc(q.opts[oi])}</span></button>`;
    }).join("")}
  </div>`;
}
function feedbackBlock(cur, answered, btnText, action) {
  const ok = answered === cur.correct, q = cur.q;
  return `<div class="feedback ${ok ? "ok" : "bad"}">
    <h4>${ok ? "✅ נכון!" : answered === -1 ? "⌛ נגמר הזמן" : "❌ לא נכון"}</h4>
    ${ok ? "" : `<p><b>התשובה הנכונה:</b> ${esc(q.opts[0])}</p>`}
    <p class="why">💡 <b>למה?</b> ${esc(q.expl)}</p>
    <div class="row" style="margin-top:12px"><span class="spacer"></span><button class="btn" data-a="${action}" id="nextbtn">${btnText}</button></div>
  </div>`;
}
function milAnswer(pos) {
  const cur = S.list[S.i]; S.answered = pos;
  const ok = pos === cur.correct; record(cur.q.id, ok);
  S.hist.push({ q: cur.q, ok, chosen: cur.q.opts[cur.order[pos]] });
  if (ok) { beep(S.i === 14 ? "win" : "ok"); confetti(S.i === 14 ? 300 : SAFE.has(S.i) ? 160 : 70); }
  else { beep("bad"); parts = []; }
  stopTimer(); vMil();
  if (!ok) $("#opts").classList.add("shake");
}
function milNext() {
  const cur = S.list[S.i];
  if (S.answered !== cur.correct) return endMil("lost");
  if (S.i === 14) return endMil("won");
  S.i++; S.answered = null; S.hidden = []; S.extra = ""; render();
}
function endMil(how) {
  const i = S.i; let prize;
  if (how === "won") prize = LADDER[14];
  else if (how === "walk") prize = i ? LADDER[i - 1] : 0;
  else prize = i >= 10 ? LADDER[9] : i >= 5 ? LADDER[4] : 0;
  if (prize > save.best.mil) save.best.mil = prize;
  addXP(Math.round(Math.log10(prize + 10) * 8));
  const secs = Math.round((Date.now() - S.t0) / 1000);
  go("milEnd", { how, prize, secs, hist: S.hist });
  if (how === "won") { confetti(400); beep("win"); }
}
function vMilEnd() {
  const right = S.hist.filter(h => h.ok).length;
  const title = S.how === "won" ? "🏆 מיליונר! ענית נכון על כל 15 השאלות" : S.how === "walk" ? "🚪 פרשת בזמן" : "המשחק נגמר";
  const share = `💰 מיליונר הגות צבאית: ${save.name ? save.name + " " : ""}זכיתי ב-${money(S.prize)} (${right}/15 נכונות) בזמן ${fmtTime(S.secs)}. מי עוקף אותי?`;
  app.innerHTML = `
  <div class="panel">
    <h1 class="display" style="font-size:30px">${title}</h1>
    <div class="score">
      <div class="stat"><div class="v">${money(S.prize)}</div><div class="k">סכום הזכייה</div></div>
      <div class="stat"><div class="v">${right}/15</div><div class="k">תשובות נכונות</div></div>
      <div class="stat"><div class="v">${fmtTime(S.secs)}</div><div class="k">זמן משחק</div></div>
    </div>
    <div class="row">
      <button class="btn" data-a="startMil">🔄 משחק חדש</button>
      <button class="btn ghost" data-a="copy" data-text="${esc(share)}">📋 העתקת התוצאה לקבוצה</button>
      <button class="btn ghost" data-a="home">🏠 לתפריט</button>
    </div>
    ${reviewList(S.hist, "📚 סיכום ולמידה – השאלות ששיחקת")}
  </div>`;
}
function reviewList(hist, title) {
  return `<div class="section-title">${title}</div>` + hist.map((h, i) => `
    <details class="rev" ${!h.ok ? "open" : ""}>
      <summary><span>${h.ok ? "✅" : "❌"}</span><span>${i + 1}. ${esc(h.q.text)}</span></summary>
      <div class="body">
        ${!h.ok && h.chosen ? `<p class="badc"><b>מה סימנת:</b> ${esc(h.chosen)}</p>` : ""}
        ${!h.ok && !h.chosen ? `<p class="badc"><b>לא ענית על השאלה</b></p>` : ""}
        <p class="okc"><b>התשובה הנכונה:</b> ${esc(h.q.opts[0])}</p>
        <p>💡 ${esc(h.q.expl)}</p>
      </div>
    </details>`).join("");
}
function lifeline(kind) {
  const cur = S.list[S.i];
  if (kind === "f") {
    const wrong = shuffle([0, 1, 2, 3].filter(p => p !== cur.correct)).slice(0, 2);
    S.hidden = wrong; S.life.f = 0;
  }
  if (kind === "a") {
    // הקהל צודק פחות בשאלות קשות – ולפעמים מתפצל
    const vis = [0, 1, 2, 3].filter(p => !S.hidden.includes(p));
    const base = { 1: 68, 2: 52, 3: 38 }[cur.q.diff] + Math.random() * 14;
    let rest = 100 - base; const others = vis.filter(p => p !== cur.correct);
    const pct = {}; pct[cur.correct] = base;
    others.forEach((p, k) => { const v = k === others.length - 1 ? rest : rest * (.3 + Math.random() * .5); pct[p] = v; rest -= v; });
    const vals = {}; vis.forEach(p => vals[p] = Math.round(pct[p]));
    S.extra += `<div class="hintbox">👥 <b>הקהל הצביע:</b><div class="aud">${[0,1,2,3].map(p =>
      `<div><span>${vals[p] !== undefined ? vals[p] + "%" : ""}</span><b style="height:${vals[p] || 0}%"></b><span>${LETTERS[p]}</span></div>`).join("")}</div></div>`;
    S.life.a = 0;
  }
  if (kind === "p") {
    const sure = { 1: 90, 2: 75, 3: 60 }[cur.q.diff];
    S.extra += `<div class="hintbox">📞 <b>החבר מהקורס:</b> ״אני לא בטוח לגמרי, אבל אני זוכר מהסיכום ש: ${esc(cur.q.hint)}״ <span class="mutec">(בטוח ב-${sure}%)</span></div>`;
    S.life.p = 0;
  }
  render();
}

// ═════════ בליץ – מי אמר? ═════════
const BLITZ_SEC = 60;
function startBlitz() {
  go("blitz", { deck: shuffle(WHO), k: 0, score: 0, streak: 0, bestStreak: 0, right: 0, wrong: [], left: BLITZ_SEC, fb: "", flash: "", started: false });
}
function vBlitz() {
  if (!S.started) {
    app.innerHTML = `<div class="panel" style="text-align:center">
      <div style="font-size:54px">⚡</div><h1 class="display" style="font-size:32px">מי אמר את זה?</h1>
      <p class="mutec" style="max-width:520px;margin:8px auto 18px">תוך ${BLITZ_SEC} שניות: שייכו כל היגד להוגה הנכון. כל תשובה נכונה שווה 10 נקודות × הרצף (עד ×5), ותשובה שגויה מאפסת את הרצף. ההסבר של כל היגד מופיע בסוף.</p>
      <div class="who" style="max-width:520px;margin:0 auto 18px">${Object.entries(THINKERS).map(([k, t], i) => `<div class="whob" style="cursor:default"><span class="e">${t.e}</span>${t.name}<span class="k">מקש ${i + 1}</span></div>`).join("")}</div>
      <button class="btn" data-a="blitzGo" style="font-size:18px;padding:14px 34px">🚀 התחל!</button></div>`;
    return;
  }
  const item = S.deck[S.k % S.deck.length];
  const mult = Math.min(5, 1 + Math.floor(S.streak / 3));
  app.innerHTML = `<div class="panel">
    <div class="row"><div><div class="big" id="bscore">${S.score}</div><div class="mutec" style="font-size:12px">נקודות</div></div>
      <span class="spacer"></span>
      <div style="text-align:center">${S.streak >= 3 ? `<div class="combo">🔥 רצף ${S.streak} · ×${mult}</div>` : `<div class="mutec">רצף: ${S.streak}</div>`}</div>
      <span class="spacer"></span>
      <div style="text-align:left"><div class="big" id="bleft">${Math.ceil(S.left)}</div><div class="mutec" style="font-size:12px">שניות</div></div></div>
    <div class="timerbar" style="margin-top:12px"><i id="bbar" style="width:${100 * S.left / BLITZ_SEC}%"></i></div>
    <div class="blitz-card ${S.flash}">${esc(item[0])}</div>
    <div class="who">${Object.entries(THINKERS).map(([k, t], i) => `<button class="whob" data-a="who" data-k="${k}"><span class="e">${t.e}</span>${t.name}<span class="k">${i + 1}</span></button>`).join("")}</div>
    <div class="lastfb" style="margin-top:12px">${S.fb}</div>
  </div>`;
}
function blitzGo() {
  S.started = true; S.tEnd = Date.now() + BLITZ_SEC * 1000; render();
  timer = setInterval(() => {
    S.left = Math.max(0, (S.tEnd - Date.now()) / 1000);
    const l = $("#bleft"), b = $("#bbar"); if (l) l.textContent = Math.ceil(S.left); if (b) b.style.width = (100 * S.left / BLITZ_SEC) + "%";
    if (S.left <= 0) endBlitz();
  }, 200);
}
function blitzAnswer(k) {
  const item = S.deck[S.k % S.deck.length];
  const ok = item[1] === k;
  if (ok) {
    S.streak++; S.right++; S.bestStreak = Math.max(S.bestStreak, S.streak);
    const mult = Math.min(5, 1 + Math.floor((S.streak - 1) / 3));
    S.score += 10 * mult; S.fb = `<span class="okc">✓ נכון – ${THINKERS[item[1]].name}</span>`; S.flash = "flash-ok"; beep("ok");
  } else {
    S.streak = 0; S.wrong.push({ item, k }); S.fb = `<span class="badc">✗ זה של ${THINKERS[item[1]].name}: ${esc(item[2])}</span>`; S.flash = "flash-bad"; beep("bad");
  }
  S.k++;
  if (S.k % S.deck.length === 0) S.deck = shuffle(WHO);
  vBlitz();
}
function endBlitz() {
  stopTimer();
  const rec = S.score > save.best.blitz; if (rec) save.best.blitz = S.score;
  addXP(Math.round(S.score / 5));
  if (rec && S.score > 0) { confetti(200); beep("win"); }
  go("blitzEnd", { score: S.score, right: S.right, total: S.k, bestStreak: S.bestStreak, wrong: S.wrong, rec });
}
function vBlitzEnd() {
  const share = `⚡ מי אמר את זה? ${save.name ? save.name + " – " : ""}${S.score} נקודות, ${S.right}/${S.total} נכונות, רצף שיא ${S.bestStreak}. מי עוקף?`;
  const seen = new Set(); const wr = S.wrong.filter(w => !seen.has(w.item[0]) && seen.add(w.item[0]));
  app.innerHTML = `<div class="panel">
    <h1 class="display" style="font-size:30px">${S.rec && S.score ? "🏆 שיא אישי חדש!" : "⏱️ נגמר הזמן"}</h1>
    <div class="score">
      <div class="stat"><div class="v">${S.score}</div><div class="k">נקודות</div></div>
      <div class="stat"><div class="v">${S.right}/${S.total}</div><div class="k">נכונות</div></div>
      <div class="stat"><div class="v">🔥 ${S.bestStreak}</div><div class="k">רצף שיא</div></div>
    </div>
    <div class="row"><button class="btn" data-a="startBlitz">🔄 עוד סיבוב</button><button class="btn ghost" data-a="copy" data-text="${esc(share)}">📋 העתקת התוצאה</button><button class="btn ghost" data-a="home">🏠 לתפריט</button></div>
    ${wr.length ? `<div class="section-title">שווה לחזור על אלה</div>
      <table class="cheat"><tr><th>ההיגד</th><th>סימנת</th><th>התשובה</th></tr>
      ${wr.map(w => `<tr><td style="white-space:normal">${esc(w.item[0])}<div class="mutec" style="font-weight:400;font-size:13px">${esc(w.item[2])}</div></td><td class="badc">${THINKERS[w.k].name}</td><td class="okc">${THINKERS[w.item[1]].e} ${THINKERS[w.item[1]].name}</td></tr>`).join("")}</table>`
      : `<p class="okc" style="margin-top:16px">לא טעית אף פעם בסיבוב הזה!</p>`}
  </div>`;
}

// ═════════ אימון לפי נושא / תיקון טעויות ═════════
function startTrain(topic) {
  const pool = topic === "_mis" ? shuffle(mistakes()) : shuffle(ALLQ.filter(q => q.topic === topic)).sort((a, b) => a.diff - b.diff);
  go("train", { topic, list: pool.slice(0, topic === "_mis" ? 15 : 10).map(prep), i: 0, answered: null, hist: [], showHint: false });
}
function vTrain() {
  const cur = S.list[S.i], done = S.answered !== null;
  const title = S.topic === "_mis" ? "🔁 תיקון טעויות" : `${TOPICS[S.topic].icon} ${TOPICS[S.topic].name}`;
  app.innerHTML = `
    <div class="qhead"><div class="row"><span class="pill gold">${title}</span><span class="pill">${S.i + 1} / ${S.list.length}</span>
      <span class="pill okc">✓ ${S.hist.filter(h => h.ok).length}</span></div>
      <button class="btn ghost" data-a="home">✕ יציאה</button></div>
    ${S.showHint ? `<div class="hintbox">💡 <b>רמז:</b> ${esc(cur.q.hint)}</div>` : ""}
    ${qBlock(cur, S.answered)}
    ${done ? feedbackBlock(cur, S.answered, S.i + 1 < S.list.length ? "לשאלה הבאה ←" : "לסיכום ←", "trainNext")
      : `<div class="row" style="margin-top:12px"><button class="btn ghost" data-a="hint" ${S.showHint ? "disabled" : ""}>💡 רמז</button><span class="spacer"></span><span class="kbd">מקשים 1–4</span></div>`}`;
}
function trainAnswer(pos) {
  const cur = S.list[S.i]; S.answered = pos; const ok = pos === cur.correct;
  record(cur.q.id, ok); S.hist.push({ q: cur.q, ok, chosen: cur.q.opts[cur.order[pos]] });
  beep(ok ? "ok" : "bad"); if (ok) confetti(40);
  vTrain(); if (!ok) $("#opts").classList.add("shake");
}
function trainNext() {
  if (S.i + 1 < S.list.length) { S.i++; S.answered = null; S.showHint = false; render(); }
  else go("trainEnd", { topic: S.topic, hist: S.hist });
}
function vTrainEnd() {
  const right = S.hist.filter(h => h.ok).length, pct = Math.round(100 * right / S.hist.length);
  const msg = pct === 100 ? "מושלם! אתם שולטים בנושא." : pct >= 70 ? "יפה מאוד! עברו על ההסברים של מה שפספסתם." : "שווה לעבור שוב על הנושא בסיכום ולנסות סיבוב נוסף.";
  if (pct === 100) confetti(200);
  app.innerHTML = `<div class="panel">
    <h1 class="display" style="font-size:30px">${pct}% נכונות</h1><p class="mutec">${msg}</p>
    <div class="row" style="margin-top:14px"><button class="btn" data-a="${S.topic === "_mis" ? "startMistakes" : "startTrain"}" data-t="${S.topic}">🔄 סיבוב נוסף</button><button class="btn ghost" data-a="home">🏠 לתפריט</button></div>
    ${reviewList(S.hist, "סיכום הסיבוב")}</div>`;
}

// ═════════ סימולציית מבחן ═════════
function vExamSetup() {
  app.innerHTML = `<div class="panel" style="max-width:640px;margin:0 auto">
    <h1 class="display" style="font-size:30px">📝 סימולציית מבחן</h1>
    <p class="mutec" style="margin:8px 0 14px">כמו במבחן האמיתי: השאלות מפוזרות באופן מאוזן בין הנושאים, אין משוב עד ההגשה, אפשר לדלג, לסמן שאלה לחזרה ולחזור אחורה. אין נקודות שליליות, אז כדאי לענות על הכול.</p>
    <ul class="mutec" style="margin:0 20px 18px;font-size:14px">
      <li>קראו כל שאלה וגבשו תשובה <b>לפני</b> שאתם מסתכלים על האפשרויות.</li>
      <li>שימו לב למילים כמו ״אינו״, ״למעט״ ו״מה משותף״.</li>
      <li>תשובה נחרצת מדי היא לרוב תשובה שגויה.</li>
    </ul>
    <div class="row">
      <button class="btn" data-a="startExam" data-n="30">30 שאלות · 90 דק׳</button>
      <button class="btn ghost" data-a="startExam" data-n="40">40 שאלות · 120 דק׳</button>
      <button class="btn ghost" data-a="startExam" data-n="15">גרסה מקוצרת · 15 שאלות</button>
    </div></div>`;
}
function pickExam(n) {
  const keys = Object.keys(TOPICS), pools = {}; keys.forEach(k => pools[k] = shuffle(ALLQ.filter(q => q.topic === k)));
  const out = []; let k = 0;
  while (out.length < n) { const t = keys[k++ % keys.length]; if (pools[t].length) out.push(pools[t].pop()); }
  return shuffle(out);
}
function startExam(n) {
  go("exam", { list: pickExam(n).map(prep), i: 0, ans: {}, flag: {}, tEnd: Date.now() + n * 180 * 1000, n, t0: Date.now(), confirm: false });
}
function vExam() {
  const cur = S.list[S.i], answeredN = Object.keys(S.ans).length;
  app.innerHTML = `
  <div class="qhead">
    <div class="row"><span class="pill gold">שאלה ${S.i + 1} מתוך ${S.n}</span><span class="pill">נענו ${answeredN}/${S.n}</span><span class="pill" id="eclock">⏳</span></div>
    <button class="btn" data-a="examSubmit">הגשת המבחן</button>
  </div>
  ${qBlock(cur, null, [], S.ans[S.i] ?? null)}
  <div class="row" style="margin-top:14px">
    <button class="btn ghost" data-a="eprev" ${S.i ? "" : "disabled"}>→ הקודמת</button>
    <button class="btn ghost" data-a="eflag">${S.flag[S.i] ? "🚩 מסומנת לחזרה" : "🏳️ סמן לחזרה"}</button>
    <span class="spacer"></span>
    <button class="btn ghost" data-a="enext" ${S.i < S.n - 1 ? "" : "disabled"}>הבאה ←</button>
  </div>
  <div class="qgrid">${S.list.map((_, i) => `<button class="qdot ${S.ans[i] !== undefined ? "ans" : ""} ${S.flag[i] ? "flag" : ""} ${i === S.i ? "cur" : ""}" data-a="ejump" data-i="${i}">${i + 1}</button>`).join("")}</div>
  ${S.confirm ? `<div class="modal"><div class="panel"><h3 style="margin-bottom:8px">להגיש את המבחן?</h3>
     <p class="mutec">${S.n - answeredN ? `נשארו <b class="badc">${S.n - answeredN}</b> שאלות שלא ענית עליהן, ואין נקודות שליליות.` : "ענית על כל השאלות."} ${Object.values(S.flag).filter(Boolean).length ? `יש גם ${Object.values(S.flag).filter(Boolean).length} שאלות שסימנת לחזרה.` : ""}</p>
     <div class="row" style="margin-top:14px"><button class="btn" data-a="examFinal">כן, להגיש</button><button class="btn ghost" data-a="examCancel">חזרה למבחן</button></div></div></div>` : ""}`;
  const tick = () => { const left = Math.max(0, (S.tEnd - Date.now()) / 1000); const c = $("#eclock");
    if (c) { c.textContent = "⏳ " + fmtTime(left); c.style.color = left < 300 ? "var(--bad)" : ""; }
    if (left <= 0) { toast("⏰ הזמן נגמר – המבחן הוגש"); examFinal(); } };
  tick(); timer = setInterval(tick, 1000);
}
function examFinal() {
  stopTimer();
  const hist = S.list.map((cur, i) => { const a = S.ans[i]; const ok = a === cur.correct; record(cur.q.id, ok);
    return { q: cur.q, ok, chosen: a !== undefined ? cur.q.opts[cur.order[a]] : null }; });
  const right = hist.filter(h => h.ok).length, grade = Math.round(100 * right / hist.length);
  if (grade > save.best.exam) save.best.exam = grade;
  addXP(right * 4);
  if (grade >= 85) { confetti(300); beep("win"); }
  go("examEnd", { hist, right, grade, secs: Math.round((Date.now() - S.t0) / 1000) });
}
function vExamEnd() {
  const by = {}; S.hist.forEach(h => { const t = h.q.topic; by[t] = by[t] || { r: 0, n: 0 }; by[t].n++; if (h.ok) by[t].r++; });
  const weak = Object.entries(by).filter(([, v]) => v.r / v.n < .6).map(([k]) => k);
  const g = S.grade, col = g >= 85 ? "var(--ok)" : g >= 60 ? "var(--gold)" : "var(--bad)";
  app.innerHTML = `<div class="panel">
    <div class="row"><div><div class="mutec">הציון שלך</div><div class="big" style="font-size:64px;color:${col}">${g}</div></div>
      <span class="spacer"></span>
      <div class="mutec" style="text-align:left">${save.name ? esc(save.name) + "<br>" : ""}${S.right}/${S.hist.length} נכונות<br>זמן: ${fmtTime(S.secs)}</div></div>
    <div class="section-title">פירוט לפי נושא</div>
    <div class="bars">${Object.entries(by).map(([k, v]) => { const p = Math.round(100 * v.r / v.n);
      return `<div class="b"><span>${TOPICS[k].icon} ${TOPICS[k].name}</span><span class="track"><i style="width:${p}%;background:${p >= 80 ? "var(--ok)" : p >= 60 ? "var(--gold)" : "var(--bad)"}"></i></span><span>${v.r}/${v.n}</span></div>`; }).join("")}</div>
    ${weak.length ? `<p style="margin-top:12px">🎯 <b>כדאי לחזק:</b> ${weak.map(k => `<button class="pill gold" data-a="startTrain" data-t="${k}" style="margin:2px">${TOPICS[k].name}</button>`).join(" ")}</p>` : `<p class="okc" style="margin-top:12px">אין נושא חלש במיוחד. מצב טוב לקראת המבחן!</p>`}
    <div class="row" style="margin-top:16px"><button class="btn" data-a="examSetup">🔄 מבחן נוסף</button><button class="btn ghost" data-a="startMistakes">🔁 תיקון טעויות</button><button class="btn ghost" data-a="home">🏠 לתפריט</button></div>
    ${reviewList(S.hist, "בדיקת המבחן – כל השאלות")}
  </div>`;
}

// ═════════ כרטיסיות ═════════
function startCards(topic = "all") {
  const pool = topic === "all" ? ALLQ : ALLQ.filter(q => q.topic === topic);
  go("cards", { topic, deck: shuffle(pool), i: 0, flip: false, known: 0 });
}
function vCards() {
  const q = S.deck[S.i];
  app.innerHTML = `
  <div class="qhead"><div class="row"><span class="pill gold">🃏 כרטיסיות</span><span class="pill">${S.i + 1} / ${S.deck.length}</span></div>
    <div class="row"><select id="ctopic" class="pill" style="background:var(--card);color:var(--ink);padding:8px" aria-label="בחירת נושא">
      <option value="all">כל הנושאים</option>${Object.entries(TOPICS).map(([k, t]) => `<option value="${k}" ${S.topic === k ? "selected" : ""}>${t.name}</option>`).join("")}</select>
      <button class="btn ghost" data-a="home">✕</button></div></div>
  <div class="flip ${S.flip ? "on" : ""}" data-a="flip">
    <div class="inner">
      <div class="face"><div class="mutec" style="font-size:12px">${TOPICS[q.topic].icon} ${TOPICS[q.topic].name}</div><div class="q">${esc(q.text)}</div><div class="tap">לחצו (או רווח) כדי להפוך</div></div>
      <div class="face back"><div class="a">✓ ${esc(q.opts[0])}</div><div class="x">${esc(q.expl)}</div></div>
    </div>
  </div>
  <div class="row"><button class="btn ghost" data-a="cprev" ${S.i ? "" : "disabled"}>→ הקודם</button><span class="spacer"></span>
    <button class="btn ghost" data-a="cnext">${S.i + 1 < S.deck.length ? "הבא ←" : "סיום ↺"}</button></div>`;
  $("#ctopic").addEventListener("change", e => startCards(e.target.value));
}

// ═════════ דף חזרה ═════════
function vCheat() {
  const rows = [
    ["🐉 סון טסו","ניצחון ללא קרב (״שיא הכשרון״), צ׳נג וצ׳י, גישה עקיפה, תקיפת תוכניות ובריתות, העמדת פני חלש, מיני-מקס, המודל הרציונלי הטהור, מודיעין כמכפיל כוח, הגישה ה״שלילית״ לריכוז"],
    ["⚔️ קלאוזביץ","חיכוך, השילוש הפרדוקסלי, מרכז כובד (מפורש), נקודת השיא, עקרון ההמתנה, הגאון הצבאי, טביעת העין, עקרון ההשמדה, מלחמה מוחלטת, גשטלט, מקסי-מקס, הגישה ה״חיובית״ לריכוז"],
    ["⭐ מאו","הערכה נטו ״אובייקטיבית״, שלושה שלבים (הגנה ← שיווי משקל ← מתקפת נגד), ״הנקודה הסופית לנסיגה״, עבודה קשה במקום גאונות, ״אנשים, לא עצמים, הם המכריעים״"],
    ["📐 ז׳ומיני","ניסיון לבנות תיאוריה מדעית, חשיבות הטכנולוגיה והחימוש, עדיפות לשיקולים הצבאיים אחרי פרוץ המלחמה (גם לו יש ספר בשם ״אמנות המלחמה״)"],
    ["🏛️ מקיאוולי","פרק מיוחד על סיום המלחמה, חופש פעולה למפקד (רומא), רפובליקות מסתגלות טוב יותר, הרומאים: השמדה או תנאים נדיבים"],
    ["🎓 הנטינגטון","שליטה אובייקטיבית (המדינאי לא מתערב) מול סובייקטיבית (מתערב)"],
    ["🇺🇸 ויינברגר","6 תנאים: אינטרס חיוני, כוח מספיק, יעדים ברורים, בחינה רציפה, דעת קהל, מוצא אחרון"]
  ];
  const nums = [["~500 לפנה״ס · פחות מ-40 עמ׳","סון טסו"],["1832 · ~600 עמ׳","קלאוזביץ"],["3 צלעות (+1 חומרית = לרבע)","השילוש"],["3","מטרות לפירוק האויב מנשקו"],["3","תחליפי מודיעין (קלאוזביץ)"],["3 שלבים מול 2 מצבים","מאו מול קלאוזביץ"],["5","מכפילי כוח (סון טסו)"],["6","תנאי ויינברגר"],["100 מול 200","דוגמת הדיביזיות (עליונות ההגנה)"]];
  const agree = ["מלחמה היא אמנות ולא מדע","עליונות הדרג המדיני, וחופש פעולה למפקד (אבל בלי קריטריונים להפרת פקודה)","מלחמה קצרה ומכרעת, ומהירות חיונית","תמיכת העם הכרחית","עדיפות יחסית בנקודת ההכרעה","אינטואיציה של המפקד, יציבות ונחישות","שיטת הטיפוס האידיאלי"];
  app.innerHTML = `<div class="panel">
    <div class="row"><h1 class="display" style="font-size:28px">📋 דף חזרה מהיר</h1><span class="spacer"></span><button class="btn ghost" data-a="home">✕</button></div>
    <p class="mutec" style="margin:4px 0 12px"><b>כלל אצבע:</b> סון טסו = רחב, מדיני, אידיאלי, זול, הונאה ומודיעין, חישוב זהיר. קלאוזביץ = צר, צבאי-מערכתי, מציאותי, כוח וריכוז, חיכוך ואי-ודאות, תעוזה.</p>
    <div style="overflow-x:auto"><table class="cheat"><tr><th>הוגה</th><th>מושגים ששייכים לו</th></tr>${rows.map(r => `<tr><td>${r[0]}</td><td style="white-space:normal">${r[1]}</td></tr>`).join("")}</table></div>
    <div class="section-title">🤝 הסכמות בין סון טסו לקלאוזביץ (שאלות ״מה משותף״)</div>
    <ul style="margin:0 20px;font-size:14.5px">${agree.map(a => `<li>${a}</li>`).join("")}</ul>
    <div class="section-title">🔢 מספרים שכדאי לזכור</div>
    <table class="cheat">${nums.map(n => `<tr><td class="goldc">${n[0]}</td><td>${n[1]}</td></tr>`).join("")}</table>
    <div class="section-title">⚠️ מלכודות נפוצות</div>
    <ul style="margin:0 20px;font-size:14.5px">
      <li>קלאוזביץ <b>לא מזלזל</b> בדיפלומטיה או בגורמים נפשיים. הם פשוט מחוץ למיקוד הספר, או שאי אפשר למדוד אותם.</li>
      <li><b>אף אחד</b> מהשניים לא קבע קריטריונים למקרים שבהם מפקד רשאי להפר פקודה מדינית.</li>
      <li>טכנולוגיה עדיפה וניצחון צבאי הם תנאי <b>הכרחי אך לא מספיק</b>.</li>
      <li>סדר העדיפויות בתקיפה <b>הפוך</b>: אצל סון טסו מתחילים בתוכניות ובבריתות, ואצל קלאוזביץ בצבא ובבירה.</li>
    </ul>
    <div class="row" style="margin-top:18px"><button class="btn" data-a="startBlitz">⚡ לתרגל ב״מי אמר?״</button><button class="btn ghost" data-a="cards">🃏 לכרטיסיות</button></div>
  </div>`;
}

// ═════════ אירועים ═════════
document.addEventListener("click", e => {
  const el = e.target.closest("[data-a]"); if (!el || el.disabled) return;
  const a = el.dataset.a;
  const A = {
    home: () => go("home"),
    sound: () => { save.sound = !save.sound; persist(); renderChips(); },
    startMil, walk: () => endMil("walk"), milNext,
    l5050: () => lifeline("f"), laud: () => lifeline("a"), lphone: () => lifeline("p"),
    ans: () => { const p = +el.dataset.p; S.screen === "mil" ? milAnswer(p) : S.screen === "train" ? trainAnswer(p) : examPick(p); },
    startBlitz, blitzGo, who: () => blitzAnswer(el.dataset.k),
    startTrain: () => startTrain(el.dataset.t), startMistakes: () => startTrain("_mis"),
    hint: () => { S.showHint = true; vTrain(); }, trainNext,
    examSetup: () => go("examSetup"), startExam: () => startExam(+el.dataset.n),
    eprev: () => { S.i--; vExamRe(); }, enext: () => { S.i++; vExamRe(); }, ejump: () => { S.i = +el.dataset.i; vExamRe(); },
    eflag: () => { S.flag[S.i] = !S.flag[S.i]; vExamRe(); },
    examSubmit: () => { S.confirm = true; vExamRe(); }, examCancel: () => { S.confirm = false; vExamRe(); }, examFinal,
    cards: () => startCards(), flip: () => { S.flip = !S.flip; $(".flip").classList.toggle("on", S.flip); },
    cnext: () => { if (S.i + 1 < S.deck.length) { S.i++; S.flip = false; vCards(); } else startCards(S.topic); },
    cprev: () => { S.i--; S.flip = false; vCards(); },
    cheat: () => go("cheat"),
    copy: async () => { try { await navigator.clipboard.writeText(el.dataset.text); toast("✓ הועתק! אפשר להדביק בקבוצה"); } catch (err) { toast("לא הצלחתי להעתיק – אפשר לצלם מסך"); } }
  };
  if (A[a]) A[a]();
});
function vExamRe() { stopTimer(); vExam(); }
function examPick(p) { S.ans[S.i] = p; beep("tick"); if (S.i < S.n - 1) setTimeout(() => { if (S.screen === "exam") { S.i++; vExamRe(); } }, 260); else vExamRe(); }
document.addEventListener("keydown", e => {
  if (e.target.tagName === "INPUT" || e.target.tagName === "SELECT") return;
  const n = parseInt(e.key, 10);
  if (S.screen === "blitz" && S.started && n >= 1 && n <= 6) return blitzAnswer(Object.keys(THINKERS)[n - 1]);
  if ((S.screen === "mil" || S.screen === "train") && S.answered === null && n >= 1 && n <= 4) {
    const b = document.querySelector(`.opt[data-p="${n - 1}"]`); if (b && !b.classList.contains("hide")) b.click(); return;
  }
  if (S.screen === "exam" && !S.confirm && n >= 1 && n <= 4) return examPick(n - 1);
  if (e.key === "Enter") { const nb = $("#nextbtn"); if (nb) { e.preventDefault(); nb.click(); } }
  if (S.screen === "cards" && (e.key === " " || e.key === "ArrowUp")) { e.preventDefault(); $(".flip").click(); }
  if (S.screen === "cards" && e.key === "ArrowLeft") $('[data-a="cnext"]').click();
  if (S.screen === "cards" && e.key === "ArrowRight" && S.i) $('[data-a="cprev"]').click();
});
addEventListener("resize", () => { fx.width = innerWidth; fx.height = innerHeight; });
render();
</script>
</body>
</html>
'''

show_game()
