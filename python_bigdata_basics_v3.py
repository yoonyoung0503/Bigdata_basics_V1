import streamlit as st

# ════════════════════════════════════════════════════════════════
# 탭 정의
# ════════════════════════════════════════════════════════════════
TABS = [
    ("1", "개요"),
    ("2", "라이브러리"),
    ("3", "DB 연결"),
    ("4", "쿼리 작성"),
    ("5", "파일 저장"),
]
N = len(TABS)

GREEN  = "#10B981"
ORANGE = "#F59E0B"
TEAL   = "#0D9488"

# ════════════════════════════════════════════════════════════════
# 페이지 설정 & 전역 CSS
# ════════════════════════════════════════════════════════════════
st.set_page_config(page_title="HF Python 기초 교육",
                   layout="wide", initial_sidebar_state="collapsed")

st.markdown(f"""
<style>
:root {{
  --c-green:  {GREEN};
  --c-orange: {ORANGE};
  --c-teal:   {TEAL};
}}

[data-testid="stSidebar"],[data-testid="collapsedControl"]{{display:none!important}}
[data-testid="stToolbar"]{{display:none!important}}
[data-testid="stDecoration"]{{display:none!important}}
header[data-testid="stHeader"]{{display:none!important}}

.block-container{{
  padding: 0 1.2rem 2rem !important;
  padding-top: 0 !important;
  margin-top: 0 !important;
  max-width: 100% !important;
}}
.stApp > div:first-child {{
  padding-top: 0 !important;
}}

/* ── 헤더 ── */
.hdr-wrap {{
  position: relative;
  background: linear-gradient(135deg, #064E3B 0%, #065F46 60%, #047857 100%);
  border-radius: 0 0 14px 14px;
  box-shadow: 0 4px 16px rgba(0,0,0,.28);
  padding: .9rem 1.4rem .75rem;
  margin: 0 0 .7rem 0;
  display: flex;
  align-items: center;
  gap: .8rem;
}}
.hdr-text {{ flex: 1; min-width: 0; }}
.hdr-title {{
  color: #ECFDF5;
  font-size: 1.15rem;
  font-weight: 800;
  margin: 0;
  line-height: 1.35;
  letter-spacing: -.02em;
  white-space: normal;
  word-break: keep-all;
}}
.hdr-sub {{
  color: rgba(167,243,208,.85);
  font-size: .78rem;
  margin: .15rem 0 0;
  white-space: normal;
  word-break: keep-all;
}}
.hdr-badges {{ display: flex; gap: .4rem; flex-shrink: 0; align-items: center; }}
.badge {{
  font-size: .65rem;
  font-weight: 700;
  padding: .2rem .55rem;
  border-radius: 20px;
  white-space: nowrap;
  letter-spacing: .02em;
}}
.badge-tag {{ background: rgba(255,255,255,.15); color: #D1FAE5; border: 1px solid rgba(255,255,255,.25); }}
.badge-main {{ background: {ORANGE}; color: #1C1917; border: none; }}

/* ── 탭 구분선 ── */
div[data-testid="stHorizontalBlock"] {{
  border-bottom: 2px solid {GREEN};
  padding-bottom: 2px;
  margin-bottom: 1rem;
}}

/* ── primary 버튼 ── */
[data-testid="stBaseButton-primary"] {{
  background: linear-gradient(135deg, #047857, #065F46) !important;
  border-color: #065F46 !important;
  font-weight: 700 !important;
}}
[data-testid="stBaseButton-primary"]:hover {{
  background: linear-gradient(135deg, #065F46, #064E3B) !important;
  border-color: #064E3B !important;
}}

/* ── 콘텐츠 박스 ── */
.tip {{
  border-left: 4px solid {GREEN};
  background: rgba(16,185,129,.11);
  color: inherit;
  padding: .75rem 1rem;
  border-radius: 0 8px 8px 0;
  margin: .5rem 0;
  font-size: .9rem;
  line-height: 1.65;
}}
.wrn {{
  border-left: 4px solid {ORANGE};
  background: rgba(245,158,11,.11);
  color: inherit;
  padding: .75rem 1rem;
  border-radius: 0 8px 8px 0;
  margin: .5rem 0;
  font-size: .9rem;
  line-height: 1.65;
}}
.err {{
  border-left: 4px solid #F87171;
  background: rgba(239,68,68,.11);
  color: inherit;
  padding: .75rem 1rem;
  border-radius: 0 8px 8px 0;
  margin: .5rem 0;
  font-size: .9rem;
  line-height: 1.65;
}}
.syn {{
  border-left: 4px solid {TEAL};
  background: rgba(13,148,136,.09);
  color: inherit;
  padding: .75rem 1rem;
  border-radius: 0 8px 8px 0;
  margin: .5rem 0;
  font-family: 'Courier New', monospace;
  font-size: .9rem;
  line-height: 2;
}}
.okbox {{
  border-left: 4px solid {GREEN};
  background: rgba(16,185,129,.11);
  color: inherit;
  padding: .55rem 1rem;
  border-radius: 0 8px 8px 0;
  margin: .4rem 0;
  font-size: .9rem;
}}
.sec {{
  font-size: 1.28rem;
  font-weight: 800;
  border-bottom: 3px solid {GREEN};
  padding-bottom: .38rem;
  margin-bottom: 1rem;
  color: {GREEN} !important;
  letter-spacing: -.02em;
}}
.cls {{
  border-radius: 12px;
  padding: 1rem 1.15rem;
  border: 1.5px solid rgba(128,128,128,.25);
  background: transparent;
  color: inherit;
  height: 100%;
}}
.step-card {{
  border-radius: 12px;
  padding: 1rem 1.15rem;
  border: 1.5px solid rgba(128,128,128,.2);
  background: transparent;
  color: inherit;
  position: relative;
}}
.step-num {{
  display: inline-block;
  background: {GREEN};
  color: #fff;
  font-weight: 800;
  font-size: .75rem;
  border-radius: 50%;
  width: 1.5rem;
  height: 1.5rem;
  line-height: 1.5rem;
  text-align: center;
  margin-right: .5rem;
}}
</style>
""", unsafe_allow_html=True)

# ── 탭 인덱스 ──────────────────────────────────────────────────
if "t" not in st.session_state:
    try:
        st.session_state.t = int(st.query_params.get("t", 0))
    except Exception:
        st.session_state.t = 0
idx = max(0, min(st.session_state.t, N - 1))

# ── 헤더 ──────────────────────────────────────────────────────
st.markdown(f"""
<div class="hdr-wrap">
  <div class="hdr-text">
    <p class="hdr-title">빅데이터 플랫폼 사용을 위한 Python 기초</p>
    <p class="hdr-sub">라이브러리 소개 · Trino DB 연결 · with 문 구조 · CSV / Excel 파일 저장</p>
  </div>
  <div class="hdr-badges">
    <span class="badge badge-tag">데이터분석도구 ①</span>
    <span class="badge badge-main">기초 개념</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── 탭 바 ─────────────────────────────────────────────────────
tab_cols = st.columns(N)
for i, (col, (ico, lbl)) in enumerate(zip(tab_cols, TABS)):
    with col:
        active = (i == idx)
        if st.button(f"{ico} {lbl}", key=f"tb{i}",
                     type="primary" if active else "secondary",
                     use_container_width=True):
            st.session_state.t = i
            st.rerun()


def nav_footer(i):
    st.divider()
    lc, _, rc = st.columns([2, 6, 2])
    with lc:
        if i > 0:
            if st.button(f"← {TABS[i-1][1]}", key=f"pv{i}", use_container_width=True):
                st.session_state.t = i - 1
                st.rerun()
    with rc:
        if i < N - 1:
            if st.button(f"{TABS[i+1][1]} →", key=f"nx{i}",
                         use_container_width=True, type="primary"):
                st.session_state.t = i + 1
                st.rerun()


# ════════════════════════════════════════════════════════════════
# 0. 개요
# ════════════════════════════════════════════════════════════════
if idx == 0:
    st.markdown('<div class="sec">교육 개요</div>', unsafe_allow_html=True)

    st.markdown("""
이 교육은 빅데이터 플랫폼(Trino)에서 데이터를 조회하고,
Python으로 가공하여 CSV / Excel 파일로 저장하는 기본 방법을 다룹니다.

    """)

    st.markdown("### 실무 흐름")
    st.markdown(f"""
<div class="syn">
① 라이브러리 import &nbsp;→&nbsp; ② Trino DB 연결 &nbsp;→&nbsp; ③ SQL 쿼리 작성·실행<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓<br>
④ DataFrame 으로 결과 받기 &nbsp;→&nbsp; ⑤ CSV / Excel 파일 저장
</div>
""", unsafe_allow_html=True)

    st.markdown("### 커리큘럼")
    curriculum = [
        ("📦", "라이브러리", "SQLAlchemy · Trino · Pandas · JSON 역할 소개"),
        ("🔌", "DB 연결",    "Trino 엔진 생성 및 연결 방법"),
        ("📋", "쿼리 작성",  "SQL 쿼리 기본 개념과 Python에서 호출하는 방법"),
        ("💾", "파일 저장",  "CSV, Excel 파일 만드는 방법"),
    ]
    c1, c2 = st.columns(2)
    for j, (ico, title, desc) in enumerate(curriculum):
        col = c1 if j % 2 == 0 else c2
        col.markdown(
            f'<div class="step-card" style="margin-bottom:.6rem">'
            f'<span class="step-num">{ico}</span><b>{title}</b><br>'
            f'<small style="opacity:.75">{desc}</small></div>',
            unsafe_allow_html=True)

    st.divider()
    st.markdown("### 기본 코드 전체 구조")
    st.markdown("아래가 실무에서 사용하는 표준 코드 전체입니다. 각 부분의 의미를 이 교육에서 차례로 설명합니다.")
    st.code("""from sqlalchemy import create_engine, text
import trino
import pandas as pd
import json

# ── Pandas 출력 옵션 ────────────────────────────────────────
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.options.display.float_format = '{:,.0f}'.format

# ── DB 연결 ─────────────────────────────────────────────────
engine = create_engine("trino://사용자ID@호스트:포트/카탈로그/스키마")

# ── 쿼리 실행 ────────────────────────────────────────────────
with engine.connect() as conn:
    query = \"\"\"
        SELECT *
        FROM   테이블명
        WHERE  조건컬럼 = '값'
        LIMIT  100
    \"\"\"
    df = pd.read_sql(text(query), conn)

# ── JSON 컬럼이 있는 경우 ────────────────────────────────────
if 'clean_payload' in df.columns:
    parsed_data = df['clean_payload'].apply(
        lambda x: json.loads(x) if pd.notnull(x) else {}
    )
    df = pd.json_normalize(parsed_data)

display(df)

# ── 파일 저장 ────────────────────────────────────────────────
csv_file_name = "결과파일.csv"
df.to_csv(csv_file_name, index=False, encoding="utf-8-sig")
""", language="python")

    nav_footer(0)


# ════════════════════════════════════════════════════════════════
# 1. 라이브러리
# ════════════════════════════════════════════════════════════════
elif idx == 1:
    st.markdown('<div class="sec">라이브러리 소개</div>', unsafe_allow_html=True)

    st.markdown("""
라이브러리란 다른 사람이 미리 만들어 놓은 유용한 코드 묶음입니다.
우리가 직접 DB 연결 코드나 엑셀 저장 코드를 만들 필요 없이, 라이브러리를 가져다 쓰면 됩니다.
    """)

    st.markdown("### import — 라이브러리 불러오기")
    st.markdown("코드 맨 위에 아래 블록을 항상 작성합니다.")
    st.code("""from sqlalchemy import create_engine, text   # DB 연결 도구
import trino                                  # Trino 전용 드라이버
import pandas as pd                           # 데이터 표(DataFrame) 도구
import json                                   # JSON 파싱 도구
""", language="python")

    st.markdown('''<div class="tip"><b>import vs from ~ import</b><br>
• <code>import pandas as pd</code> → pandas 전체를 가져오고, <code>pd</code>라는 별명으로 사용<br>
• <code>from sqlalchemy import create_engine</code> → sqlalchemy에서 <code>create_engine</code> 함수만 꺼내오기
</div>''', unsafe_allow_html=True)

    st.divider()
    st.markdown("### 각 라이브러리가 하는 일")

    libs = [
        ("sqlalchemy", GREEN,  "Python과 데이터베이스를 연결해주는 표준 도구입니다. Trino에 접속할 때 <code>create_engine()</code>과 <code>text()</code> 함수를 사용합니다."),
        ("trino",      TEAL,   "Trino(분산 SQL 엔진) 전용 드라이버입니다. <code>import trino</code> 한 줄만 써주면 SQLAlchemy가 Trino에 연결할 때 자동으로 활용합니다. 직접 호출하는 경우는 거의 없습니다."),
        ("pandas (pd)",ORANGE, "데이터를 표(DataFrame) 형태로 다루는 핵심 라이브러리입니다. 쿼리 결과 받기, 데이터 가공, CSV/Excel 저장까지 대부분의 작업을 pandas로 처리합니다."),
        ("json",       GREEN,  "JSON 형식의 문자열을 Python에서 사용할 수 있는 딕셔너리로 변환해줍니다. DB의 <code>clean_payload</code> 같은 JSON 컬럼을 파싱할 때 사용합니다."),
    ]
    for lib, bc, desc in libs:
        st.markdown(
            f'<div class="step-card" style="margin-bottom:.7rem;border-left:4px solid {bc}">'
            f'<code style="font-size:1rem;font-weight:700">{lib}</code><br>'
            f'<span style="font-size:.9rem;line-height:1.7">{desc}</span></div>',
            unsafe_allow_html=True)

    st.divider()
    st.markdown("### Pandas 출력 옵션")
    st.markdown("DataFrame을 화면에 출력할 때 보기 좋게 설정하는 옵션입니다. 코드 상단에 한 번만 작성하면 됩니다.")
    st.code("""pd.set_option('display.max_columns', None)   # 모든 컬럼 표시 (기본값은 일부만 표시)
pd.set_option('display.max_colwidth', None)  # 컬럼 내용 잘림 방지
pd.options.display.float_format = '{:,.0f}'.format  # 숫자에 천 단위 쉼표 표시
""", language="python")

    st.markdown('''<div class="wrn"><b>주의 — 오타</b><br>
원본 코드에 <code>display.max_cloumns</code> 라는 오타가 있을 수 있습니다.<br>
올바른 옵션명은 <code>display.max_<b>col</b>umns</code> 입니다. (u·l 순서 주의)
</div>''', unsafe_allow_html=True)

    nav_footer(1)


# ════════════════════════════════════════════════════════════════
# 2. DB 연결
# ════════════════════════════════════════════════════════════════
elif idx == 2:
    st.markdown('<div class="sec">DB 연결 — Trino란 무엇인가</div>', unsafe_allow_html=True)

    st.markdown("### Trino란?")
    st.markdown(f"""
<div class="step-card" style="margin-bottom:.8rem">
<b>Trino</b>는 수십억 건의 대용량 데이터를 빠르게 처리하는 <b>분산 SQL 엔진</b>입니다.<br><br>
일반 사내 DB가 한 대의 서버에서 처리하는 방식이라면,
Trino는 여러 서버가 동시에 데이터를 나눠 처리하기 때문에 대용량 쿼리를 훨씬 빠르게 실행할 수 있습니다.<br><br>
우리가 쓰는 빅데이터 플랫폼의 핵심 데이터베이스 엔진이 바로 Trino입니다.
</div>
""", unsafe_allow_html=True)

    st.markdown(f"""
<div class="syn">
[사내 PC] → Python 코드 → SQLAlchemy → Trino 드라이버 → Trino 서버 → 데이터 반환
</div>
""", unsafe_allow_html=True)

    st.divider()
    st.markdown("### 연결 주소(Connection String) 구조")
    st.markdown('''<div class="syn">
trino://<b>사용자ID</b>@<b>호스트주소</b>:<b>포트번호</b>/<b>카탈로그</b>/<b>스키마</b>
</div>''', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
<div class="step-card">
<b>각 항목 설명</b><br><br>
<span class="step-num">ID</span> <b>사용자ID</b> — 본인 사번 또는 계정<br><br>
<span class="step-num">2</span> <b>호스트주소</b> — Trino 서버 주소<br><br>
<span class="step-num">3</span> <b>포트번호</b> — 보통 8080 또는 8443<br><br>
<span class="step-num">4</span> <b>카탈로그</b> — 최상위 데이터 구분 (예: iceberg)<br><br>
<span class="step-num">5</span> <b>스키마</b> — 카탈로그 안의 레이어 (예: bronze, silver, gold)
</div>
""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
<div class="step-card">
<b>레이어 구조</b><br><br>
<div style="line-height:2.2">
<b>iceberg</b> (카탈로그)<br>
&nbsp;&nbsp;&nbsp;&nbsp;├─ <b>bronze</b> — 원본 적재 데이터<br>
&nbsp;&nbsp;&nbsp;&nbsp;├─ <b>silver</b> — 정제된 데이터<br>
&nbsp;&nbsp;&nbsp;&nbsp;└─ <b>gold</b> &nbsp;&nbsp;— 집계·분석용 데이터
</div>
<br>
<small style="opacity:.7">어떤 레이어를 써야 하는지는 담당자 또는 데이터 카탈로그에서 확인하세요.</small>
</div>
""", unsafe_allow_html=True)

    st.divider()
    st.markdown("### 엔진 생성 코드")
    st.code("""from sqlalchemy import create_engine

# 기본형
engine = create_engine("trino://사용자ID@호스트:포트/카탈로그/스키마")

# 실제 작성 예시
engine = create_engine(
    "trino://hong123@trino.bigdata.co.kr:8080/iceberg/bronze"
)
""", language="python")

    st.markdown('''<div class="tip"><b>엔진은 한 번만 만들면 됩니다</b><br>
<code>create_engine()</code>은 스크립트당 한 번만 실행하면 됩니다.<br>
이후 쿼리를 여러 번 실행하더라도 엔진을 다시 만들 필요가 없습니다.
</div>''', unsafe_allow_html=True)

    st.divider()
    st.markdown("### 연결 테스트")
    st.markdown("엔진이 제대로 연결되는지 확인하는 가장 간단한 방법입니다.")
    st.code("""from sqlalchemy import create_engine, text
import pandas as pd

engine = create_engine("trino://사용자ID@호스트:포트/카탈로그/스키마")

# 연결 테스트: 간단한 쿼리 1건만 조회
with engine.connect() as conn:
    df = pd.read_sql(text("SELECT 1 AS test"), conn)
    display(df)

# 정상이면 test 컬럼에 1이 담긴 DataFrame이 출력됩니다.
""", language="python")

    nav_footer(2)


# ════════════════════════════════════════════════════════════════
# 3. 쿼리 작성
# ════════════════════════════════════════════════════════════════
elif idx == 3:
    st.markdown('<div class="sec">쿼리 작성 및 호출</div>', unsafe_allow_html=True)

    st.markdown(f"""
<div class="wrn">
SQL 쿼리 작성법(SELECT / WHERE / JOIN 등)은 <b>별도 SQL 교육자료</b>에서 다룹니다.<br>
이 챕터에서는 Python 코드 구조(<code>with</code> 문, <code>pd.read_sql</code>)와 JSON 컬럼 처리에 집중합니다.
</div>
""", unsafe_allow_html=True)

    t2, t3 = st.tabs(["with 문 & 쿼리 호출", "JSON 컬럼 처리"])

    # ── 탭 1: Python에서 쿼리 호출 ──
    with t2:
        st.markdown("#### with 문이란?")
        st.markdown("쿼리 실행 코드에서 자주 보이는 `with` 문의 의미를 먼저 이해하고 넘어갑니다.")
        st.code("""with engine.connect() as conn:
    # 이 블록 안에서 conn을 사용해 쿼리 실행
    df = pd.read_sql(text(query), conn)

# 블록이 끝나면 conn 연결이 자동으로 닫힘
""", language="python")
        st.markdown(f"""
<div class="tip">
<b>with 문 구조 설명</b><br><br>
• <code>with engine.connect()</code> — DB 연결을 엽니다<br>
• <code>as conn</code> — 열린 연결 객체를 <code>conn</code>이라는 이름으로 사용합니다<br>
• 블록(들여쓰기 안쪽) 안에서만 <code>conn</code>을 사용할 수 있습니다<br>
• 블록이 끝나면 <code>conn.close()</code>를 직접 호출하지 않아도 <b>연결이 자동으로 닫힙니다</b><br><br>
즉, 연결 열기·닫기를 자동으로 처리해주기 때문에 안전하고 코드가 깔끔해집니다.
</div>""", unsafe_allow_html=True)
        st.markdown(f"""
<div class="wrn">연결을 열어놓고 닫지 않으면 서버 자원이 낭비됩니다.
<code>with</code> 문을 쓰면 예외(오류)가 발생해도 연결이 반드시 닫히므로 항상 <code>with</code> 문을 사용하세요.
</div>""", unsafe_allow_html=True)

        st.divider()
        st.markdown("#### 쿼리 실행 기본 패턴")
        st.markdown("Python에서 Trino에 쿼리를 보내고 결과를 DataFrame으로 받는 표준 코드입니다.")
        st.code("""from sqlalchemy import create_engine, text
import pandas as pd

engine = create_engine("trino://사용자ID@호스트:포트/카탈로그/스키마")

with engine.connect() as conn:
    query = \"\"\"
        -- SQL 쿼리 작성법은 별도 SQL 교육자료에서 다룹니다.
        -- 아래는 구조 이해를 위한 예시입니다.
        SELECT
            basis_ym        AS 기준연월,
            region_cd       AS 지역코드,
            SUM(grnt_cnt)   AS 공급건수
        FROM   iceberg.bronze.TB_테이블명
        WHERE  basis_ym = '202306'
        GROUP BY 1, 2
        ORDER BY 공급건수 DESC
        LIMIT  1000
    \"\"\"
    df = pd.read_sql(text(query), conn)

display(df)
""", language="python")

        st.markdown(f"""
<div class="tip">
<b>with 문 안의 SQL 쿼리</b><br>
<code>query = \"\"\"...\"\"\"</code> 부분에 작성하는 SQL 문법(SELECT, WHERE, GROUP BY 등)은
<b>별도 SQL 교육자료(데이터분석도구 ②)</b>에서 자세히 다룹니다.<br>
여기서는 <code>with engine.connect() as conn</code> → <code>pd.read_sql()</code>로 이어지는
<b>Python 호출 구조</b>를 이해하는 데 집중하세요.
</div>
""", unsafe_allow_html=True)

        st.markdown(f"""
<div class="tip"><b>코드 구조 설명</b><br>
• <code>with engine.connect() as conn</code> — DB 연결을 열고, 블록이 끝나면 자동으로 연결을 닫습니다<br>
• <code>\"\"\" ... \"\"\"</code> — 삼중 따옴표로 여러 줄 SQL 문자열 작성<br>
• <code>text(query)</code> — SQL 문자열을 SQLAlchemy가 인식하는 형태로 변환<br>
• <code>pd.read_sql(..., conn)</code> — 쿼리 실행 후 결과를 DataFrame으로 반환
</div>""", unsafe_allow_html=True)

        st.divider()
        st.markdown("#### 조건값을 변수로 넣는 방법 (f-string)")
        st.markdown("기준연월 등 조건값을 변수로 관리하면 코드 재사용이 쉬워집니다.")
        st.code("""basis_ym  = "202306"   # ← 이 값만 바꾸면 됩니다
region_cd = "11"

with engine.connect() as conn:
    # query 변수에 작성하는 SQL 문법은 SQL 교육자료에서 다룹니다.
    query = f\"\"\"
        SELECT *
        FROM   iceberg.bronze.TB_테이블명
        WHERE  basis_ym   = '{basis_ym}'
          AND  region_cd  = '{region_cd}'
        LIMIT  500
    \"\"\"
    df = pd.read_sql(text(query), conn)

display(df)
""", language="python")

        st.markdown('''<div class="tip"><b>f-string이란?</b><br>
문자열 앞에 <code>f</code>를 붙이면, 문자열 안의 <code>{변수명}</code>이 실제 변수 값으로 바뀝니다.<br>
<code>f"WHERE basis_ym = '{basis_ym}'"</code> → <code>WHERE basis_ym = '202306'</code>
</div>''', unsafe_allow_html=True)

    # ── 탭 3: JSON 컬럼 처리 ──
    with t3:
        st.markdown("#### JSON 컬럼이란?")
        st.markdown("""
일부 테이블의 컬럼에는 데이터가 JSON 형식의 **문자열**로 저장되어 있습니다.
예를 들어 `clean_payload` 컬럼의 값이 아래처럼 생겼습니다.
        """)
        st.code('''{"region":"서울","amount":185050,"cnt":320}''', language="json")

        st.markdown("이 문자열을 그냥 두면 분석에 사용하기 어렵습니다. **파싱(parsing)** 과정을 거쳐 각 키를 컬럼으로 펼쳐야 합니다.")

        st.divider()
        st.markdown("#### JSON 파싱 코드")
        st.code("""import json

# clean_payload 컬럼이 있는 경우에만 파싱
if 'clean_payload' in df.columns:
    parsed_data = df['clean_payload'].apply(
        lambda x: json.loads(x) if pd.notnull(x) else {}
    )
    df = pd.json_normalize(parsed_data)

display(df)
""", language="python")

        st.markdown(f"""
<div class="tip"><b>코드 설명</b><br>
• <code>json.loads(x)</code> — JSON 문자열 → Python 딕셔너리로 변환<br>
• <code>pd.notnull(x)</code> — 값이 비어있지 않은지 확인 (비어있으면 빈 딕셔너리 반환)<br>
• <code>lambda x: ...</code> — 각 행에 적용할 짧은 함수<br>
• <code>pd.json_normalize()</code> — 딕셔너리 리스트를 펼쳐서 각 키를 컬럼으로 변환
</div>""", unsafe_allow_html=True)

        st.markdown("#### 파싱 전/후 비교")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**파싱 전 — 한 컬럼에 문자열로**")
            st.code("""clean_payload
──────────────────────────────────────
{"region":"서울","amount":185050}
{"region":"경기","amount":312000}
{"region":"인천","amount":98000}
""", language="text")
        with c2:
            st.markdown("**파싱 후 — 컬럼으로 펼쳐짐**")
            st.code("""region    amount
──────────────────
서울      185050
경기      312000
인천       98000
""", language="text")

    nav_footer(3)


# ════════════════════════════════════════════════════════════════
# 4. 파일 저장
# ════════════════════════════════════════════════════════════════
elif idx == 4:
    st.markdown('<div class="sec">파일 저장 — CSV · Excel</div>', unsafe_allow_html=True)

    t1, t2, t3 = st.tabs(["CSV 저장", "Excel 저장", "파일명 자동 생성"])

    # ── 탭 1: CSV ──
    with t1:
        st.markdown("#### CSV 파일 저장")
        st.markdown("쿼리로 받은 DataFrame을 CSV 파일로 저장하는 기본 방법입니다.")
        st.code("""# 기본 저장
csv_file_name = "결과파일.csv"
df.to_csv(csv_file_name, index=False, encoding="utf-8-sig")
""", language="python")

        st.markdown("#### 각 옵션 설명")
        options = [
            ("index=False",         GREEN,  "행 번호(인덱스)를 CSV에 포함하지 않음. <b>생략하면 불필요한 숫자 컬럼이 생깁니다.</b>"),
            ('encoding="utf-8-sig"', TEAL,  "한글이 깨지지 않도록 인코딩 설정. <b>반드시 써야 합니다.</b> utf-8만 쓰면 엑셀에서 한글이 깨질 수 있습니다."),
        ]
        for opt, bc, desc in options:
            st.markdown(
                f'<div class="step-card" style="margin-bottom:.6rem;border-left:4px solid {bc}">'
                f'<code style="font-weight:700">{opt}</code><br>'
                f'<span style="font-size:.9rem">{desc}</span></div>',
                unsafe_allow_html=True)

        st.markdown('''<div class="wrn"><b>자주 하는 실수</b><br>
• <code>encoding="utf-8-sig"</code> 대신 <code>encoding="utf-8"</code> → 엑셀에서 한글 깨짐<br>
• <code>index=False</code> 생략 → 0, 1, 2, 3... 숫자 컬럼이 첫 번째 컬럼으로 추가됨
</div>''', unsafe_allow_html=True)

    # ── 탭 2: Excel ──
    with t2:
        st.markdown("#### Excel 파일 저장")
        st.markdown("CSV 대신 `.xlsx` 형식으로 저장할 수 있습니다. 시트 이름도 지정할 수 있습니다.")
        st.code("""# openpyxl 라이브러리가 필요합니다 (설치: pip install openpyxl)
excel_file_name = "결과파일.xlsx"

with pd.ExcelWriter(excel_file_name, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="데이터", index=False)
""", language="python")

        st.markdown('''<div class="tip"><b>ExcelWriter란?</b><br>
<code>pd.ExcelWriter</code>는 Excel 파일 작성 도구입니다.<br>
<code>with</code> 블록 안에 <code>to_excel()</code>을 쓰면, 블록이 끝날 때 파일이 자동으로 저장됩니다.
</div>''', unsafe_allow_html=True)

        st.divider()
        st.markdown("#### 시트를 여러 개 만들기")
        st.markdown("하나의 Excel 파일 안에 여러 시트로 나눠 저장할 수 있습니다.")
        st.code("""with pd.ExcelWriter("결과파일.xlsx", engine="openpyxl") as writer:
    df_all.to_excel(writer, sheet_name="전체",  index=False)
    df_seoul.to_excel(writer, sheet_name="서울", index=False)
    df_gyeonggi.to_excel(writer, sheet_name="경기", index=False)
""", language="python")

    # ── 탭 3: 파일명 자동 생성 ──
    with t3:
        st.markdown("#### 오늘 날짜를 파일명에 자동으로 넣기")
        st.markdown("매번 파일명을 직접 수정하지 않고, 날짜를 자동으로 파일명에 포함시킬 수 있습니다.")
        st.code("""import datetime

today = datetime.date.today().strftime("%Y%m%d")  # 예: "20250120"
print(today)   # 20250120
""", language="python")

        st.markdown("#### 파일명 자동 생성 예시")
        st.code("""import datetime

today    = datetime.date.today().strftime("%Y%m%d")
basis_ym = "202306"

# CSV 파일명
csv_file_name = f"보증현황_{basis_ym}_{today}.csv"
# → "보증현황_202306_20250120.csv"

# Excel 파일명
excel_file_name = f"보증현황_{basis_ym}_{today}.xlsx"
# → "보증현황_202306_20250120.xlsx"

# 저장
df.to_csv(csv_file_name, index=False, encoding="utf-8-sig")
""", language="python")

        st.markdown('''<div class="tip"><b>strftime 형식 코드</b><br>
• <code>%Y</code> → 연도 4자리 (예: 2025)<br>
• <code>%m</code> → 월 2자리 (예: 01)<br>
• <code>%d</code> → 일 2자리 (예: 20)<br>
• <code>%Y%m%d</code> → 20250120 형식으로 출력
</div>''', unsafe_allow_html=True)

        st.divider()
        st.markdown("### 전체 저장 코드 — 완성본")
        st.markdown("쿼리 실행부터 파일 저장까지 이어지는 완성 코드입니다.")
        st.code("""from sqlalchemy import create_engine, text
import pandas as pd
import json
import datetime

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.options.display.float_format = '{:,.0f}'.format

engine = create_engine("trino://사용자ID@호스트:포트/카탈로그/스키마")

basis_ym = "202306"

with engine.connect() as conn:
    query = f\"\"\"
        SELECT *
        FROM   iceberg.bronze.TB_테이블명
        WHERE  basis_ym = '{basis_ym}'
        LIMIT  1000
    \"\"\"
    df = pd.read_sql(text(query), conn)

# JSON 컬럼 파싱 (해당하는 경우)
if 'clean_payload' in df.columns:
    parsed_data = df['clean_payload'].apply(
        lambda x: json.loads(x) if pd.notnull(x) else {}
    )
    df = pd.json_normalize(parsed_data)

display(df)

# 파일 저장
today = datetime.date.today().strftime("%Y%m%d")
csv_file_name = f"결과_{basis_ym}_{today}.csv"
df.to_csv(csv_file_name, index=False, encoding="utf-8-sig")
print(f"저장 완료: {csv_file_name}")
""", language="python")

    nav_footer(4)
