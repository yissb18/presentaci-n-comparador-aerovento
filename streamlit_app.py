"""
streamlit_app.py — Muestra la página de AeroVento (aerovento.html) dentro de Streamlit.

La página es un solo archivo HTML con CSS y JavaScript. Streamlit solo la incrusta.
"""

from pathlib import Path

import streamlit as st

st.set_page_config(page_title="AeroVento · ¿Cuánto pagas de luz?", page_icon="⚡",
                   layout="wide", initial_sidebar_state="collapsed")

st.html("""
<style>
header, [data-testid="stHeader"], footer { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
iframe { height: 100vh !important; border: 0; }
</style>
""")

HTML = (Path(__file__).parent / "aerovento.html").read_text(encoding="utf-8")


def mostrar(html: str, alto: int = 900):
    """Usa st.iframe (versiones nuevas) o components.html (versiones viejas)."""
    if hasattr(st, "iframe"):
        st.iframe(html, height=alto)
    else:
        import streamlit.components.v1 as components
        components.html(html, height=alto, scrolling=True)


mostrar(HTML)
