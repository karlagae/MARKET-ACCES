
import streamlit as st

st.set_page_config(
    page_title="Seguimiento Market Access",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# DATOS MOCKUP
# =========================
kpis = [
    {"title": "CONTACTOS\nREALIZADOS", "value": "21", "color": "orange", "sub": "↑ +5 últimos 7 días"},
    {"title": "INTERÉS\nCAPTURADO", "value": "13", "color": "blue", "sub": "↑ +5 últimos 7 días"},
    {"title": "PRESENTACIONES\nPROGRAMADAS", "value": "8", "color": "white", "sub": ""},
    {"title": "NECESIDADES\nGENERADAS", "value": "7", "color": "white", "sub": ""},
    {"title": "CASOS ENVIADOS\nA SUPERIOR", "value": "5", "color": "white", "sub": ""},
    {"title": "AUTORIZACIONES\nOBTENIDAS", "value": "3", "color": "white_orange", "sub": ""},
]

instituciones = [
    ("IMSS", 65, "blue"),
    ("ISSSTE", 35, "orange"),
    ("SEDENA", 50, "blue_dark"),
]

cronograma = [
    {
        "nombre": "Dr. Miguel Ángel Sosa ACDx",
        "inst": "",
        "vals": [1.0, 0.8, 1.0, 0.0, 0.0],
        "icon": "🩺"
    },
    {
        "nombre": "Lic. Reyna Basilio",
        "inst": "ISSSTE",
        "vals": [1.0, 1.0, 0.5, 0.0, 0.0],
        "icon": "🧑‍💼"
    },
    {
        "nombre": "Dra. Rosa de Guadalupe BMP",
        "inst": "",
        "vals": [1.0, 1.0, 0.8, 0.0, 0.0],
        "icon": "🧪"
    },
    {
        "nombre": "Dra. Deta. BMP",
        "inst": "IMSS",
        "vals": [1.0, 1.0, 1.0, 0.0, 0.0],
        "icon": "🧬"
    },
]

eventos = [
    {"dia": "11", "titulo": "Presentación IMSS", "sub": "Dr. Miguel 2", "tipo": "blue"},
    {"dia": "17", "titulo": "Seguimiento ISSSTE", "sub": "Pora Basilio", "tipo": "light"},
    {"dia": "21", "titulo": "Rovsión SEDENA", "sub": "Dra. Mesa Correa", "tipo": "soft"},
]


# =========================
# ESTILOS
# =========================
st.markdown("""
<style>
    .stApp {
        background: #f4f3f8;
    }

    .block-container {
        padding-top: 1.3rem;
        padding-bottom: 1rem;
        max-width: 1450px;
    }

    :root {
        --blue: #06038D;
        --blue-2: #2E5FD0;
        --orange: #E87722;
        --black: #000000;
        --white: #FFFFFF;
        --soft-bg: #f4f3f8;
        --card-border: #e3e1ea;
        --muted: #707070;
    }

    .top-title {
        background: linear-gradient(90deg, #1e2148 0%, #2d2f66 100%);
        color: white;
        border-radius: 4px;
        padding: 16px 24px;
        text-align: center;
        font-size: 28px;
        font-weight: 700;
        letter-spacing: 0.3px;
        margin-bottom: 12px;
    }

    .filters-wrap {
        display: grid;
        grid-template-columns: 270px 1fr 1fr 1fr 1fr 120px;
        gap: 10px;
        margin-bottom: 14px;
        align-items: stretch;
    }

    .filter-left {
        background: var(--blue);
        color: white;
        border-radius: 4px;
        height: 42px;
        display: flex;
        align-items: center;
        padding: 0 16px;
        font-size: 19px;
        gap: 12px;
        justify-content: flex-start;
    }

    .fake-select {
        background: white;
        border: 1px solid var(--card-border);
        border-radius: 4px;
        height: 42px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 14px;
        color: #1e2148;
        font-size: 16px;
    }

    .fake-button {
        background: var(--blue);
        color: white;
        border-radius: 4px;
        height: 42px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
        font-weight: 700;
    }

    .kpi-grid {
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        gap: 12px;
        margin-bottom: 14px;
    }

    .kpi-card {
        border: 1px solid var(--card-border);
        border-radius: 4px;
        min-height: 150px;
        padding: 16px 14px 12px 14px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .kpi-orange {
        background: var(--orange);
        color: white;
    }

    .kpi-blue {
        background: linear-gradient(135deg, #2e5fd0 0%, #3f6de5 100%);
        color: white;
    }

    .kpi-white {
        background: white;
        color: #111b4d;
    }

    .kpi-white-orange {
        background: white;
        color: #111b4d;
    }

    .kpi-title {
        font-size: 18px;
        font-weight: 700;
        text-align: center;
        line-height: 1.18;
        white-space: pre-line;
    }

    .kpi-value {
        font-size: 56px;
        font-weight: 800;
        text-align: center;
        line-height: 1;
        margin-top: 6px;
        margin-bottom: 4px;
    }

    .kpi-sub {
        font-size: 14px;
        text-align: center;
        opacity: 0.95;
    }

    .kpi-white-orange .kpi-title,
    .kpi-white-orange .kpi-value {
        color: var(--orange);
    }

    .main-grid {
        display: grid;
        grid-template-columns: 65% 35%;
        gap: 14px;
        margin-bottom: 14px;
    }

    .panel {
        background: white;
        border: 1px solid var(--card-border);
        border-radius: 4px;
        padding: 14px 18px;
    }

    .panel-title {
        font-size: 22px;
        font-weight: 700;
        color: #1a214f;
        margin-bottom: 18px;
    }

    .inst-row {
        display: grid;
        grid-template-columns: 80px 1fr 80px;
        align-items: center;
        gap: 10px;
        margin-bottom: 16px;
    }

    .inst-name {
        font-size: 24px;
        font-weight: 700;
        color: #1a214f;
    }

    .inst-name.orange {
        color: var(--orange);
    }

    .bar-bg {
        height: 22px;
        background: #e8e7f0;
        border-radius: 2px;
        overflow: hidden;
        position: relative;
    }

    .bar-fill-blue {
        height: 100%;
        background: linear-gradient(90deg, #4a78df 0%, #507bf2 100%);
    }

    .bar-fill-orange {
        height: 100%;
        background: linear-gradient(90deg, #f39a19 0%, #ff9900 100%);
    }

    .bar-fill-blue-dark {
        height: 100%;
        background: linear-gradient(90deg, #324d9c 0%, #4663bc 100%);
    }

    .pct {
        font-size: 24px;
        font-weight: 700;
        color: #1a214f;
    }

    .calendar-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 14px;
    }

    .calendar-title {
        font-size: 22px;
        font-weight: 700;
        color: #1a214f;
    }

    .calendar-nav {
        display: flex;
        gap: 8px;
    }

    .nav-btn {
        width: 38px;
        height: 32px;
        border: 1px solid var(--card-border);
        border-radius: 4px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #1a214f;
        background: white;
        font-size: 22px;
    }

    .calendar-placeholder {
        background: #faf9fd;
        border: 1px solid #efedf4;
        border-radius: 4px;
        height: 98px;
        margin-bottom: 14px;
    }

    .event-card {
        border-radius: 4px;
        padding: 12px 14px;
        margin-bottom: 10px;
        line-height: 1.08;
    }

    .event-blue {
        background: linear-gradient(90deg, #2c56c7 0%, #385fd2 100%);
        color: white;
    }

    .event-light {
        background: #edf4ff;
        color: #1a214f;
    }

    .event-soft {
        background: #f2f0fa;
        color: #1a214f;
    }

    .event-main {
        font-size: 19px;
        font-weight: 700;
        margin-bottom: 3px;
    }

    .event-sub {
        font-size: 14px;
        opacity: 0.95;
    }

    .cronograma-panel {
        background: white;
        border: 1px solid var(--card-border);
        border-radius: 4px;
        padding: 14px 18px 18px 18px;
    }

    .stages-head {
        display: grid;
        grid-template-columns: 290px repeat(5, 1fr);
        gap: 0;
        margin-top: 6px;
        margin-bottom: 8px;
    }

    .stage-cell {
        font-size: 18px;
        color: #1a214f;
        text-align: center;
    }

    .process-row {
        display: grid;
        grid-template-columns: 290px repeat(5, 1fr);
        gap: 0;
        align-items: center;
        margin-bottom: 12px;
    }

    .name-cell {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 17px;
        color: #1a214f;
    }

    .icon {
        width: 28px;
        height: 28px;
        border-radius: 4px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #eef2fb;
        font-size: 16px;
    }

    .mini-track {
        height: 18px;
        background: #ecebf3;
        border-right: 1px solid #f6f4fa;
        position: relative;
    }

    .mini-fill-blue {
        height: 100%;
        background: linear-gradient(90deg, #3c61c7 0%, #506fe3 100%);
    }

    .mini-fill-orange {
        height: 100%;
        background: linear-gradient(90deg, #f08d1d 0%, #ff9700 100%);
    }

    .legend {
        display: flex;
        gap: 24px;
        margin-top: 12px;
        color: #1a214f;
        font-size: 16px;
        align-items: center;
    }

    .legend-item {
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .legend-box {
        width: 18px;
        height: 18px;
        border-radius: 3px;
    }

    .blue-box { background: linear-gradient(90deg, #5d84e5 0%, #87a6f5 100%); }
    .orange-box { background: linear-gradient(90deg, #f08d1d 0%, #ff9800 100%); }

    @media (max-width: 1200px) {
        .kpi-grid {
            grid-template-columns: repeat(3, 1fr);
        }
        .main-grid {
            grid-template-columns: 1fr;
        }
        .filters-wrap {
            grid-template-columns: 1fr 1fr;
        }
        .stages-head, .process-row {
            grid-template-columns: 1fr;
        }
    }
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown(
    '<div class="top-title">SEGUIMIENTO MARKET ACCESS – PROGRESO HACIA BASES</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="filters-wrap">
    <div class="filter-left">👤 🗂️ • • • • • • •</div>
    <div class="fake-select"><span>Institución Pública</span><span>⌄</span></div>
    <div class="fake-select"><span><b>Área</b></span><span>⌄</span></div>
    <div class="fake-select"><span>Responsable Werfen</span><span>⌄</span></div>
    <div class="fake-select"><span>Decisor Técnico</span><span>⌄</span></div>
    <div class="fake-button">Filtrar</div>
</div>
""", unsafe_allow_html=True)

# =========================
# KPIS
# =========================
kpi_html = '<div class="kpi-grid">'
for k in kpis:
    cls = {
        "orange": "kpi-orange",
        "blue": "kpi-blue",
        "white": "kpi-white",
        "white_orange": "kpi-white-orange",
    }[k["color"]]

    kpi_html += f"""
    <div class="kpi-card {cls}">
        <div class="kpi-title">{k["title"]}</div>
        <div class="kpi-value">{k["value"]}</div>
        <div class="kpi-sub">{k["sub"]}</div>
    </div>
    """
kpi_html += "</div>"

st.markdown(kpi_html, unsafe_allow_html=True)

# =========================
# AVANCE + AGENDA
# =========================
left_html = """
<div class="panel">
    <div class="panel-title">Avance hacia modificación de bases por institución</div>
"""

for nombre, pct, tipo in instituciones:
    fill_class = {
        "blue": "bar-fill-blue",
        "orange": "bar-fill-orange",
        "blue_dark": "bar-fill-blue-dark"
    }[tipo]
    name_class = "inst-name orange" if nombre == "ISSSTE" else "inst-name"

    left_html += f"""
    <div class="inst-row">
        <div class="{name_class}">{nombre}</div>
        <div class="bar-bg">
            <div class="{fill_class}" style="width:{pct}%;"></div>
        </div>
        <div class="pct">{pct}%</div>
    </div>
    """

left_html += "</div>"

right_html = """
<div class="panel">
    <div class="calendar-header">
        <div class="calendar-title">Junio 2024 ⌄</div>
        <div class="calendar-nav">
            <div class="nav-btn">‹</div>
            <div class="nav-btn">›</div>
        </div>
    </div>
    <div class="calendar-placeholder"></div>
"""

for e in eventos:
    tipo_class = {
        "blue": "event-blue",
        "light": "event-light",
        "soft": "event-soft"
    }[e["tipo"]]
    right_html += f"""
    <div class="event-card {tipo_class}">
        <div class="event-main">{e['dia']} {e['titulo']}</div>
        <div class="event-sub">{e['sub']}</div>
    </div>
    """

right_html += "</div>"

st.markdown(
    f"""
    <div class="main-grid">
        {left_html}
        {right_html}
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# CRONOGRAMA
# =========================
cron_html = """
<div class="cronograma-panel">
    <div class="panel-title">Cronograma de Procesos</div>

    <div class="stages-head">
        <div></div>
        <div class="stage-cell">Contactos</div>
        <div class="stage-cell">Interés</div>
        <div class="stage-cell">Presentación</div>
        <div class="stage-cell">Necesidad</div>
        <div class="stage-cell">Bases</div>
    </div>
"""

for i, row in enumerate(cronograma):
    cron_html += f"""
    <div class="process-row">
        <div class="name-cell">
            <div class="icon">{row['icon']}</div>
            <div>{row['nombre']}{"&nbsp;&nbsp;" + row['inst'] if row['inst'] else ""}</div>
        </div>
    """

    for j, v in enumerate(row["vals"]):
        fill_class = "mini-fill-orange" if (i == 0 and j == 0) else "mini-fill-blue"
        cron_html += f"""
        <div class="mini-track">
            <div class="{fill_class}" style="width:{int(v*100)}%;"></div>
        </div>
        """

    cron_html += "</div>"

cron_html += """
    <div class="legend">
        <div class="legend-item"><div class="legend-box blue-box"></div> IMSS</div>
        <div class="legend-item"><div class="legend-box orange-box"></div> ISSSTE</div>
    </div>
</div>
"""

st.markdown(cron_html, unsafe_allow_html=True)
