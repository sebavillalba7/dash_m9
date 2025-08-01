
from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from flask import Flask
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import os
from utils.pdf_generator import exportar_dashboard_pdf

# === Cargar datos ===
df = pd.read_excel("data/DB_UNT_2.xlsx")

# === Inicializar servidor Flask + Login ===
server = Flask(__name__)
server.secret_key = 'clave_secreta_segura'
login_manager = LoginManager()
login_manager.init_app(server)

# === Usuarios ficticios ===
users = {"admin": {"password": "admin"}}

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# === Inicializar Dash ===
app = Dash(
    __name__,
    server=server,
    external_stylesheets=[dbc.themes.DARKLY],
    suppress_callback_exceptions=True
)
app.title = "Monitoreo y Control de Cargas"


# === Layout de login ===
login_layout = dbc.Container([
    html.Div([
        html.Img(src='/assets/logo.png', style={'height': '300px', 'marginTop': '20px'}),
        html.H2("Iniciar sesión", className='text-center mt-4 mb-2'),
        html.Hr(),
        dcc.Input(id="username", type="text", placeholder="Usuario", className='form-control mb-2'),
        dcc.Input(id="password", type="password", placeholder="Contraseña", className='form-control mb-2'),
        html.Button("Ingresar", id="login-btn", className='btn btn-primary'),
        html.Div(id="login-output", className='mt-2 text-danger')
    ], className='text-center text-white mt-5')
])

# === Layout inicial para ruteo dinámico ===
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# === Página principal ===
home_layout = dbc.Container([
    html.Div([
        html.Img(src='/assets/logo.png', style={'height': '300px', 'marginTop': '20px'}),
        html.H1("Análisis de Rendimiento Físico", className='text-center mt-4 mb-2'),
        html.Hr(),
        html.P("Explorá las métricas físicas y neuromusculares por sesión", className='text-center'),
        dbc.Button("Ir al Dashboard", href="/dashboard", color="primary", className='d-block mx-auto'),
        dbc.Button("Cerrar sesión", href="/logout", color="danger", className='d-block mx-auto mt-2')
    ], className='text-center text-white mt-5')
])

# === Página Dashboard ===
dashboard_layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Img(src='/assets/logo.png', style={'height': '60px'}), width=2),
        dbc.Col(html.H2("Dashboard de Performance", className='text-white text-center mt-3'), width=8),
        dbc.Col([
            dbc.Button("Home", href="/home", color="secondary", className="mt-3 mb-1"),
            dbc.Button("Exportar PDF", id="btn-pdf", color="info", className="mt-2")
        ], width=2)
    ]),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id="filtro-pos",
                options=[{"label": pos, "value": pos} for pos in sorted(df["POS"].dropna().unique())],
                placeholder="Seleccionar posición/es",
                multi=True
            )
        ], width=6),
        dbc.Col([
            dcc.Dropdown(
                id="filtro-ses",
                options=[{"label": ses, "value": ses} for ses in sorted(df["SES"].dropna().unique())],
                placeholder="Seleccionar tipo de sesión",
                multi=True
            )
        ], width=6)
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col(dcc.Graph(id="grafico_carga")),
        dbc.Col(dcc.Graph(id="grafico_carrera")),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id="grafico_neuromuscular")),
        dbc.Col(dcc.Graph(id="grafico_totales")),
    ]),
    dcc.Download(id="descargar-pdf")
], fluid=True)

# === Control de navegación ===
@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def mostrar_pagina(pathname):
    if pathname in ["/", "/login"]:
        return login_layout
    elif pathname == "/dashboard" and current_user.is_authenticated:
        return dashboard_layout
    elif pathname == "/home" and current_user.is_authenticated:
        return home_layout
    elif pathname == "/logout":
        logout_user()
        return login_layout
    else:
        return login_layout


# === Callback de login ===
@app.callback(
    Output("login-output", "children"),
    Input("login-btn", "n_clicks"),
    State("username", "value"),
    State("password", "value")
)
def login(n_clicks, username, password):
    if n_clicks and username in users and users[username]["password"] == password:
        login_user(User(username))
        return dcc.Location(href="/home", id="redir")
    elif n_clicks:
        return "Usuario o contraseña incorrectos."

# === Callback de gráficos ===
@app.callback(
    Output("grafico_carga", "figure"),
    Output("grafico_carrera", "figure"),
    Output("grafico_neuromuscular", "figure"),
    Output("grafico_totales", "figure"),
    Input("filtro-pos", "value"),
    Input("filtro-ses", "value")
)
def actualizar_graficos(pos, ses):
    dff = df.copy()
    if pos: dff = dff[dff["POS"].isin(pos)]
    if ses: dff = dff[dff["SES"].isin(ses)]

    fig1 = px.scatter(dff, x="MTS/MIN", y="MTS-HSD", color="SES", hover_name="JUGADOR",
                      title="Relación Ritmo vs Alta Intensidad")

    vars_carrera = ["TOT-DIST", "MTS/MIN", "MTS-HSD", "MTS-SPD"]
    df_carrera = dff.groupby("POS")[vars_carrera].mean().reset_index().melt(id_vars="POS")
    fig2 = px.bar(df_carrera, x="POS", y="value", color="variable", barmode="group",
                  title="Promedio de Variables de Carrera por Posición")

    df_neuro = dff.groupby("POS")[["ACEL", "DES"]].mean().reset_index().melt(id_vars="POS")
    fig3 = px.bar(df_neuro, x="POS", y="value", color="variable", barmode="group",
                  title="Promedio ACEL y DES por Posición")

    fig4 = px.histogram(dff, x="SES", y="TOT-DIST", color="POS", barmode="group",
                        title="Carga Total por Sesión y Posición")

    for fig in [fig1, fig2, fig3, fig4]:
        fig.update_layout(template="plotly_dark")

    return fig1, fig2, fig3, fig4

# === Exportar PDF ===
@app.callback(
    Output("descargar-pdf", "data"),
    Input("btn-pdf", "n_clicks"),
    prevent_initial_call=True
)
def generar_pdf(n):
    return exportar_dashboard_pdf(df)

# === Layout raíz con enrutamiento ===
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

if __name__ == '__main__':
    app.run(debug=True)
