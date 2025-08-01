from fpdf import FPDF
import plotly.express as px
import tempfile
import os
from dash import dcc
from dash.dcc import send_file

def exportar_dashboard_pdf(df):
    # === FIGURAS DEL DASHBOARD ===
    fig1 = px.scatter(df, x="MTS/MIN", y="MTS-HSD", color="SES", hover_name="JUGADOR",
                      title="Relación Ritmo vs Alta Intensidad")
    
    vars_carrera = ["TOT-DIST", "MTS/MIN", "MTS-HSD", "MTS-SPD"]
    df_carrera = df.groupby("POS")[vars_carrera].mean().reset_index().melt(id_vars="POS")
    fig2 = px.bar(df_carrera, x="POS", y="value", color="variable", barmode="group",
                  title="Promedio de Variables de Carrera por Posición")

    df_neuro = df.groupby("POS")[["ACEL", "DES"]].mean().reset_index().melt(id_vars="POS")
    fig3 = px.bar(df_neuro, x="POS", y="value", color="variable", barmode="group",
                  title="Promedio ACEL y DES por Posición")

    fig4 = px.histogram(df, x="SES", y="TOT-DIST", color="POS", barmode="group",
                        title="Carga Total por Sesión y Posición")

    for fig in [fig1, fig2, fig3, fig4]:
        fig.update_layout(template="plotly_dark")

    # === CREAR PDF ===
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    
    # --- PORTADA ---
    pdf.add_page()
    pdf.image("assets/logo.png", x=100, w=90)  # Ajustá ruta si es necesario

    pdf.set_font("Arial", "B", 20)
    pdf.ln(10)
    pdf.cell(0, 10, "Resumen Físico - Dashboard", ln=True, align="C")

    pdf.set_font("Arial", "", 12)
    pdf.ln(10)
    intro = (
        "Este informe resume las métricas físicas más relevantes obtenidas a partir del monitoreo GPS. "
        "Incluye análisis de carga total, ritmo de juego y esfuerzos de alta intensidad, desglosados por tipo de sesión y posición. "
        "Su objetivo es brindar una visión clara para apoyar el proceso de toma de decisiones."
    )
    pdf.multi_cell(0, 10, intro, align="C")

    # --- PÁGINAS CON GRÁFICOS ---
    for fig in [fig1, fig2, fig3, fig4]:
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmpfile:
            fig.write_image(tmpfile.name)
            tmpfile.flush()
            tmpfile.close()

            pdf.add_page()
            pdf.image(tmpfile.name, w=250)
            os.remove(tmpfile.name)

    # === EXPORTAR ===
    tmp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(tmp_pdf.name)
    return dcc.send_file(tmp_pdf.name)
