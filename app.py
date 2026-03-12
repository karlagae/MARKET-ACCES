import streamlit as st

st.set_page_config(page_title="Seguimiento Market Access", layout="wide")

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
    ("11", "Presentación IMSS", "Dr. Miguel 2", "blue"),
    ("17", "Seguimiento ISSSTE", "Pora Basilio", "light"),
    ("21", "Revisión SEDENA", "Dra. Mesa Correa", "soft"),
]

procesos = [
    ("🩺", "Dr. Miguel Ángel Sosa ACDx", [1.0, 0.8, 1.0, 0.0, 0.0]),
    ("👩‍💼", "Lic. Reyna Basilio ISSSTE", [1.0, 1.0, 0.5, 0.0, 0.0]),
    ("🧪", "Dra. Rosa de Guadalupe BMP", [1.0, 1.0, 0.8, 0.0, 0.0]),
    ("🧬", "Dra. Deta. BMP IMSS", [1.0, 1.0, 1.0, 0.0, 0.0]),
]

# =========================
# CSS
# =========================
st.markdown("""
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
    border-radius: 4px;
    padding: 10px 12px;
    margin-bottom: 10px;
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

.event-main {
    font-size: 18px;
    font-weight: 800;
    line-height: 1.1;
}

.event-sub {
    font-size: 14px;
    line-height: 1.1;
    margin-top: 2px;
}

.stage-header {
    display: grid;
    grid-template-columns: 300px repeat(5, 1fr);
    margin-bottom: 8px;
}

.stage-name {
    text-align: center;
    color: var(--text);
    font-size: 17px;
    font-weight: 700;
}

.process-row {
    display: grid;
    grid-template-columns: 300px repeat(5, 1fr);
    align-items: center;
    margin-bottom: 12px;
}

.process-name {
    display: flex;
    align-items: center;
    gap: 10px;
    color: var(--text);
    font-size: 17px;
}

.proc-icon {
    width: 28px;
    height: 28px;
    border-radius: 4px;
    background: #eef2fb;
    display: flex;
    align-items: center;
    justify-content: center;
}

.proc-track {
    height: 18px;
    background: #eceaf4;
    border-right: 1px solid #f8f7fb;
}

.fill-blue {
    height: 100%;
    background: linear-gradient(90deg, #3e62c9 0%, #5572e2 100%);
}

.fill-orange {
    height: 100%;
    background: linear-gradient(90deg, #f08d1d 0%, #ff9800 100%);
}

.legend {
    display: flex;
    gap: 24px;
    margin-top: 10px;
    font-size: 16px;
    color: var(--text);
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

.legend-imss {
    background: linear-gradient(90deg, #5d84e5 0%, #87a6f5 100%);
}

.legend-issste {
    background: linear-gradient(90deg, #f08d1d 0%, #ff9800 100%);
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown('<div class="title-bar">SEGUIMIENTO MARKET ACCESS – PROGRESO HACIA BASES</div>', unsafe_allow_html=True)

c1, c2, c3, c4, c5, c6 = st.columns([1.4, 1.1, 1.1, 1.2, 1.2, 0.65])

with c1:
    st.markdown('<div class="top-icon-box">👤 📁 • • • • • • •</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="fake-filter"><span>Institución Pública</span><span>˅</span></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="fake-filter"><span><b>Área</b></span><span>˅</span></div>', unsafe_allow_html=True)
with c4:
    st.markdown('<div class="fake-filter"><span>Responsable Werfen</span><span>˅</span></div>', unsafe_allow_html=True)
with c5:
    st.markdown('<div class="fake-filter"><span>Decisor Técnico</span><span>˅</span></div>', unsafe_allow_html=True)
with c6:
    st.markdown('<div class="filter-btn">Filtrar</div>', unsafe_allow_html=True)

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

    html = f"""
    <div class="kpi-card {cls}">
        <div class="kpi-title">{title}</div>
        <div class="kpi-value">{value}</div>
        <div class="kpi-sub">{sub}</div>
    </div>
    """
    col.markdown(html, unsafe_allow_html=True)

st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

# =========================
# AVANCE + CALENDARIO
# =========================
left, right = st.columns([2.1, 1.2])

with left:
    html = '<div class="panel"><div class="panel-title">Avance hacia modificación de bases por institución</div>'
    for nombre, pct, kind in instituciones:
        bar_class = {
            "blue": "bar-fill-blue",
            "orange": "bar-fill-orange",
            "blue_dark": "bar-fill-blue-dark"
        }[kind]
        name_class = "inst-name orange" if nombre == "ISSSTE" else "inst-name"

        html += f"""
        <div class="inst-row">
            <div class="{name_class}">{nombre}</div>
            <div class="bar-bg"><div class="{bar_class}" style="width:{pct}%"></div></div>
            <div class="pct">{pct}%</div>
        </div>
        """
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

with right:
    html = """
    <div class="panel">
        <div class="calendar-head">
            <div class="calendar-title">Junio 2024 ⌄</div>
            <div class="nav-wrap">
                <div class="nav-btn">‹</div>
                <div class="nav-btn">›</div>
            </div>
        </div>
        <div class="calendar-placeholder"></div>
    """
    for dia, titulo, sub, kind in eventos:
        event_class = {
            "blue": "event-blue",
            "light": "event-light",
            "soft": "event-soft"
        }[kind]
        html += f"""
        <div class="event-card {event_class}">
            <div class="event-main">{dia} {titulo}</div>
            <div class="event-sub">{sub}</div>
        </div>
        """
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

# =========================
# CRONOGRAMA
# =========================
html = """
<div class="panel">
    <div class="panel-title">Cronograma de Procesos</div>
    <div class="stage-header">
        <div></div>
        <div class="stage-name">Contactos</div>
        <div class="stage-name">Interés</div>
        <div class="stage-name">Presentación</div>
        <div class="stage-name">Necesidad</div>
        <div class="stage-name">Bases</div>
    </div>
"""

for idx, (icono, nombre, vals) in enumerate(procesos):
    html += f"""
    <div class="process-row">
        <div class="process-name">
            <div class="proc-icon">{icono}</div>
            <div>{nombre}</div>
        </div>
    """
    for j, v in enumerate(vals):
        fill_class = "fill-orange" if (idx == 0 and j == 0) else "fill-blue"
        html += f"""
        <div class="proc-track">
            <div class="{fill_class}" style="width:{int(v*100)}%"></div>
        </div>
        """
    html += "</div>"

html += """
    <div class="legend">
        <div class="legend-item"><div class="legend-box legend-imss"></div> IMSS</div>
        <div class="legend-item"><div class="legend-box legend-issste"></div> ISSSTE</div>
    </div>
</div>
"""

st.markdown(html, unsafe_allow_html=True)
