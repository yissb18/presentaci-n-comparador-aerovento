# ⚡ AeroVento — Página web del facturador

Página de un solo archivo (HTML, CSS y JavaScript) donde la persona dibuja su consumo de un día y ve:
qué plan le conviene (franjas o plano), el consumo y valor del mes, el subsidio o contribución por
estrato, sugerencias de ahorro y una **factura en PDF** con NIT, ciudad, mes y códigos de pago.

## Archivos

```
aerovento-web/
├── index.html           # La página (para GitHub Pages)
├── aerovento.html       # La misma página (la lee Streamlit)
├── streamlit_app.py     # La incrusta en Streamlit
├── requirements.txt
└── .streamlit/config.toml
```

## Opción A (recomendada): GitHub Pages

1. Crea un repositorio en https://github.com/new (por ejemplo `aerovento`).
2. **Add file → Upload files**, arrastra el contenido de la carpeta y **Commit changes**.
3. **Settings → Pages → Deploy from a branch**, rama `main`, carpeta `/ (root)`, **Save**.
4. En uno o dos minutos: `https://TU_USUARIO.github.io/aerovento/`

La descarga del PDF funciona con normalidad en esta opción.

## Opción B: Streamlit Community Cloud

1. Sube los archivos a GitHub (pasos 1 y 2 de arriba).
2. En https://share.streamlit.io: **Create app → Deploy a public app from GitHub**.
3. Elige el repositorio, la rama `main` y `streamlit_app.py` como archivo principal. **Deploy**.

La página queda dentro de un marco de Streamlit. Algunos navegadores bloquean la descarga del PDF
desde ese marco. Si pasa, usa el botón **Imprimir** (guardar como PDF) o la opción A.

## Cosas que debes saber

- Las letras vienen de Google Fonts y el generador de PDF (jsPDF) viene de cdnjs: se necesita internet.
- La factura es un documento informativo. El número y la referencia de pago los genera el programa y no
  tienen validez tributaria ni son un convenio de recaudo real.
- Los porcentajes de subsidio (60, 50, 15 y 20 %) y los topes (173 y 130 kWh) son valores máximos de referencia.
  Verifícalos antes de usarla con clientes.
- Para tener la lógica en Python (con `logica.py` y descarga de PDF nativa en Streamlit) usa el paquete `aerovento-streamlit`.
- Si cambias el contenido, edita `index.html` y copia el mismo cambio a `aerovento.html`.
