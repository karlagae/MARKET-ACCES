import streamlit as st
import textwrap

st.set_page_config(
    page_title="Seguimiento Market Access",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# DATOS MOCK
# =========================
kpis = [
    ("CONTACTOS\nREALIZADOS", "21", "↑ +5 últimos 7 días", "orange"),
    ("INTERÉS\nCAPTURADO", "13", "↑ +5 últimos 7 días", "blue"),
    ("PRESENTACIONES\nPROGRAMADAS", "8", "", "white"),
    ("NECESIDADES\nGENERADAS", "7", "", "white"),
    ("CASOS ENVIADOS\nA SUPERIOR", "5", "", "white"),
    ("AUTORIZACIONES\nOBTENIDAS", "3", "", "white_orange"),
]

instituciones = [
    ("IMSS", 65, "blue"),
    ("ISSSTE", 35, "orange"),
    ("SEDENA", 50, "blue_dark"),
]

eventos = [
    ("11", "JUN", "Presentación IMSS", "Dr. Miguel Ángel Sosa", "blue"),
    ("17", "JUN", "Seguimiento ISSSTE", "Lic. Reyna Basilio", "light"),
    ("21", "JUN", "Revisión SEDENA", "Dra. Mesa Correa", "soft"),
]

procesos = [
    ("Dr. Miguel Ángel Sosa", "IMSS", "ACDx", [1.0, 0.8, 1.0, 0.0, 0.0]),
    ("Lic. Reyna Basilio", "ISSSTE", "Coagulación", [1.0, 1.0, 0.5, 0.0, 0.0]),
    ("Dra. Rosa Guadalupe", "SEDENA", "Gases", [1.0, 1.0, 0.8, 0.0, 0.0]),
]

# =========================
# CSS
# =========================
st.markdown(textwrap.dedent("""
<style>
    .stApp {
        background-color: #f3f2f7;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 1.2rem;
        padding-bottom: 1rem;
    }

    :root {
        --blue: #06038D;
        --orange: #E87722;
        --dark: #222657;
        --border: #dfdde8;
        --text: #131a46;
        --soft: #f7f7fb;
    }

    .title-bar {
        background: linear-gradient(90deg, #232654 0%, #34306e 100%);
        color: white;
        padding: 16px 20px;
        border-radius: 4px;
        text-align: center;
        font-size: 26px;
        font-weight: 800;
        margin-bottom: 12px;
    }

    .top-icon-box {
        background: #23008f;
        color: white;
        border-radius: 4px;
        height: 42px;
        display: flex;
        align-items: center;
        padding: 0 16px;
        font-size: 18px;
        font-weight: 600;
    }

    .fake-filter {
        background: white;
        border: 1px solid var(--border);
        border-radius: 4px;
        height: 42px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 14px;
        color: var(--text);
        font-size: 16px;
    }

    .filter-btn {
        background: #23008f;
        color: white;
        border-radius: 4px;
        height: 42px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
        font-weight: 700;
    }

    .kpi-card {
        border-radius: 4px;
        border: 1px solid var(--border);
        min-height: 150px;
        padding: 14px 10px 10px 10px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        text-align: center;
    }

    .kpi-orange {
        background: var(--orange);
        color: white;
    }

    .kpi-blue {
        background: linear-gradient(135deg, #2f5fd0 0%, #4372e6 100%);
        color: white;
    }

    .kpi-white {
        background: white;
        color: var(--text);
    }

    .kpi-white-orange {
        background: white;
        color: var(--orange);
    }

    .kpi-title {
        white-space: pre-line;
        font-size: 17px;
        font-weight: 800;
        line-height: 1.15;
    }

    .kpi-value {
        font-size: 56px;
        font-weight: 900;
        line-height: 1;
        margin: 8px 0 6px 0;
    }

    .kpi-sub {
        font-size: 14px;
        opacity: 0.95;
    }

    .panel {
        background: white;
        border: 1px solid var(--border);
        border-radius: 4px;
        padding: 14px 18px;
        height: 100%;
    }

    .panel-title {
        font-size: 21px;
        font-weight: 800;
        color: var(--text);
        margin-bottom: 18px;
    }

    .inst-row {
        display: grid;
        grid-template-columns: 90px 1fr 80px;
        gap: 12px;
        align-items: center;
        margin-bottom: 18px;
    }

    .inst-name {
        font-size: 24px;
        font-weight: 800;
        color: var(--text);
    }

    .inst-name.orange {
        color: var(--orange);
    }

    .bar-bg {
        width: 100%;
        height: 22px;
        background: #eceaf4;
        border-radius: 2px;
        overflow: hidden;
    }

    .bar-fill-blue {
        height: 100%;
        background: linear-gradient(90deg, #4f79df 0%, #6187ea 100%);
    }

    .bar-fill-orange {
        height: 100%;
        background: linear-gradient(90deg, #f39a19 0%, #ff9e00 100%);
    }

    .bar-fill-blue-dark {
        height: 100%;
        background: linear-gradient(90deg, #324d9c 0%, #4d67c0 100%);
    }

    .pct {
        font-size: 22px;
        font-weight: 800;
        color: var(--text);
    }

    .calendar-head {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 14px;
    }

    .calendar-title {
        font-size: 22px;
        font-weight: 800;
        color: var(--text);
    }

    .nav-wrap {
        display: flex;
        gap: 8px;
    }

    .nav-btn {
        width: 38px;
        height: 32px;
        border: 1px solid var(--border);
        border-radius: 4px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--text);
        background: white;
        font-size: 20px;
    }

    .calendar-placeholder {
        height: 95px;
        background: #faf9fd;
        border: 1px solid #efedf4;
        border-radius: 4px;
        margin-bottom: 14px;
    }

    .event-card {
        display: flex;
        gap: 14px;
        padding: 12px;
        border-radius: 6px;
        margin-bottom: 10px;
        align-items: center;
    }

    .event-blue {
        background: linear-gradient(90deg, #2c56c7 0%, #395fd4 100%);
        color: white;
    }

    .event-light {
        background: #edf3ff;
        color: var(--text);
    }

    .event-soft {
        background: #f1eff8;
        color: var(--text);
    }

    .event-date {
        width: 60px;
        min-width: 60px;
        background: rgba(255,255,255,0.92);
        border-radius: 6px;
        text-align: center;
        padding: 6px;
        font-weight: 700;
    }

    .event-day {
        font-size: 22px;
        font-weight: 800;
        line-height: 1;
        color: #131a46;
    }

    .event-month {
        font-size: 11px;
        opacity: 0.75;
        margin-top: 3px;
        color: #131a46;
        letter-spacing: 0.5px;
    }

    .event-info {
        display: flex;
        flex-direction: column;
    }

    .event-main {
        font-size: 18px;
        font-weight: 800;
        line-height: 1.1;
    }

    .event-sub {
        font-size: 14px;
        line-height: 1.1;
        margin-top: 4px;
        opacity: 0.95;
    }

    .stage-header {
        display: grid;
        grid-template-columns: 2.4fr 1.1fr 1.4fr repeat(5, 1fr);
        margin-bottom: 10px;
        column-gap: 8px;
        align-items: center;
    }

    .process-row {
        display: grid;
        grid-template-columns: 2.4fr 1.1fr 1.4fr repeat(5, 1fr);
        align-items: center;
        margin-bottom: 12px;
        column-gap: 8px;
    }

    .stage-name {
        text-align: center;
        color: var(--text);
        font-size: 16px;
        font-weight: 700;
    }

    .text-cell {
        color: var(--text);
        font-size: 16px;
        display: flex;
        align-items: center;
        min-height: 18px;
    }

    .text-cell-left {
        color: var(--text);
        font-size: 16px;
        display: flex;
        align-items: center;
        min-height: 18px;
        text-align: left;
    }

    .inst-badge {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 700;
        width: fit-content;
    }

    .inst-imss {
        background: #eaf0ff;
        color: #315fd3;
    }

    .inst-issste {
        background: #fff1e7;
        color: #e87722;
    }

    .inst-sedena {
        background: #eef1f4;
        color: #364152;
    }

    .sol-cell {
        color: var(--text);
        font-size: 15px;
        font-weight: 600;
        display: flex;
        align-items: center;
    }

    .proc-track {
        height: 18px;
        background: #eceaf4;
        border-radius: 2px;
        overflow: hidden;
    }

    .fill-blue {
        height: 100%;
        background: linear-gradient(90deg, #3e62c9 0%, #5572e2 100%);
    }

    .fill-orange {
        height: 100%;
        background: linear-gradient(90deg, #f08d1d 0%, #ff9800 100%);
    }

    .fill-gray {
        height: 100%;
        background: linear-gradient(90deg, #7f8aa3 0%, #98a3bb 100%);
    }
</style>
"""), unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown(
    textwrap.dedent("""
    <div class="title-bar">SEGUIMIENTO MARKET ACCESS – PROGRESO HACIA BASES</div>
    """),
    unsafe_allow_html=True
)

c1, c2, c3, c4, c5, c6 = st.columns([1.4, 1.1, 1.1, 1.2, 1.2, 0.65])

with c1:
    st.markdown(
        textwrap.dedent("""
        <div class="top-icon-box">👤 📁 • • • • • • •</div>
        """),
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        textwrap.dedent("""
        <div class="fake-filter"><span>Institución Pública</span><span>˅</span></div>
        """),
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        textwrap.dedent("""
        <div class="fake-filter"><span><b>Área</b></span><span>˅</span></div>
        """),
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        textwrap.dedent("""
        <div class="fake-filter"><span>Responsable Werfen</span><span>˅</span></div>
        """),
        unsafe_allow_html=True
    )

with c5:
    st.markdown(
        textwrap.dedent("""
        <div class="fake-filter"><span>Decisor Técnico</span><span>˅</span></div>
        """),
        unsafe_allow_html=True
    )

with c6:
    st.markdown(
        textwrap.dedent("""
        <div class="filter-btn">Filtrar</div>
        """),
        unsafe_allow_html=True
    )

st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

# =========================
# KPIS
# =========================
kpi_cols = st.columns(6)

for col, (title, value, sub, kind) in zip(kpi_cols, kpis):
    cls = {
        "orange": "kpi-orange",
        "blue": "kpi-blue",
        "white": "kpi-white",
        "white_orange": "kpi-white-orange",
    }[kind]

    html = textwrap.dedent(f"""
    <div class="kpi-card {cls}">
        <div class="kpi-title">{title}</div>
        <div class="kpi-value">{value}</div>
        <div class="kpi-sub">{sub}</div>
    </div>
    """)
    col.markdown(html, unsafe_allow_html=True)

st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

# =========================
# AVANCE + CALENDARIO
# =========================
left, right = st.columns([2.1, 1.2])

with left:
    html = textwrap.dedent("""
    <div class="panel">
        <div class="panel-title">Avance hacia modificación de bases por institución</div>
    """)

    for nombre, pct, kind in instituciones:
        bar_class = {
            "blue": "bar-fill-blue",
            "orange": "bar-fill-orange",
            "blue_dark": "bar-fill-blue-dark"
        }[kind]

        name_class = "inst-name orange" if nombre == "ISSSTE" else "inst-name"

        html += textwrap.dedent(f"""
        <div class="inst-row">
            <div class="{name_class}">{nombre}</div>
            <div class="bar-bg">
                <div class="{bar_class}" style="width:{pct}%"></div>
            </div>
            <div class="pct">{pct}%</div>
        </div>
        """)

    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

with right:
    html = textwrap.dedent("""
    <div class="panel">
        <div class="calendar-head">
            <div class="calendar-title">Junio 2024 ˅</div>
            <div class="nav-wrap">
                <div class="nav-btn">‹</div>
                <div class="nav-btn">›</div>
            </div>
        </div>
        <div class="calendar-placeholder"></div>
    """)

    for dia, mes, titulo, sub, kind in eventos:
        event_class = {
            "blue": "event-blue",
            "light": "event-light",
            "soft": "event-soft"
        }[kind]

        html += textwrap.dedent(f"""
        <div class="event-card {event_class}">
            <div class="event-date">
                <div class="event-day">{dia}</div>
                <div class="event-month">{mes}</div>
            </div>

            <div class="event-info">
                <div class="event-main">{titulo}</div>
                <div class="event-sub">{sub}</div>
            </div>
        </div>
        """)

    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

# =========================
# CRONOGRAMA
# =========================
html = textwrap.dedent("""
<div class="panel">
    <div class="panel-title">Cronograma de Procesos</div>
    <div class="stage-header">
        <div class="stage-name" style="text-align:left;">Decisor</div>
        <div class="stage-name">Institución</div>
        <div class="stage-name">Solución</div>
        <div class="stage-name">Contactos</div>
        <div class="stage-name">Interés</div>
        <div class="stage-name">Presentación</div>
        <div class="stage-name">Necesidad</div>
        <div class="stage-name">Bases</div>
    </div>
""")

for nombre, institucion, solucion, vals in procesos:
    if institucion.upper() == "IMSS":
        badge_class = "inst-badge inst-imss"
        fill_class = "fill-blue"
    elif institucion.upper() == "ISSSTE":
        badge_class = "inst-badge inst-issste"
        fill_class = "fill-orange"
    else:
        badge_class = "inst-badge inst-sedena"
        fill_class = "fill-gray"

    html += textwrap.dedent(f"""
    <div class="process-row">
        <div class="text-cell-left">{nombre}</div>
        <div class="text-cell" style="justify-content:center;">
            <span class="{badge_class}">{institucion}</span>
        </div>
        <div class="sol-cell">{solucion}</div>
    """)

    for v in vals:
        html += textwrap.dedent(f"""
        <div class="proc-track">
            <div class="{fill_class}" style="width:{int(v * 100)}%"></div>
        </div>
        """)

    html += "</div>"

html += "</div>"

st.markdown(html, unsafe_allow_html=True)
