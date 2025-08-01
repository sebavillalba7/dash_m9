# 🏋️‍♂️ Dashboard de Performance Física con Dash

Este proyecto forma parte del Módulo 9 del Máster en Python Avanzado Aplicado al Deporte. Consiste en una aplicación web desarrollada con **Dash** que permite visualizar y exportar datos de rendimiento físico en deportistas a partir de métricas GPS.

## 🔐 Acceso a la aplicación

- **Usuario**: `admin`
- **Contraseña**: `admin`

El sistema implementa **control de sesiones con Flask-Login**, navegación por pestañas, visualizaciones interactivas y generación de reportes en PDF con estilo personalizado.

---

## 🧰 Tecnologías y Librerías Usadas

- Python 3.9+
- Plotly Dash
- Flask-Login
- Dash Bootstrap Components
- FPDF
- Kaleido
- Pandas

---

## 🖥️ Instalación y Ejecución

### 🪟 Windows

```bash
# 1. Clonar el repositorio
git clone https://github.com/sebavillalba7/dash_m9.git
cd dash_m9

# 2. Crear entorno virtual (recomendado)
python -m venv venv
venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar la app
python app_dash.py
```

### 🍎 MacOS / Linux

```bash
# 1. Clonar el repositorio
git clone https://github.com/sebavillalba7/dash_m9.git
cd dash_m9

# 2. Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar la app
python3 app_dash.py
```

---

## 📂 Estructura del Proyecto

```text
TAREA_M9/
├── app_dash.py            # app Dash
├── requirements.txt       # Dependencias del proyecto
├── Procfile               # Despliegue en Heroku
│
├── assets/                # Recursos visuales y CSS
│   ├── custom.css         # Estilos personalizados (modo oscuro, selectboxes, etc.)
│   └── logo.png           # Logo usado en página Home y PDF
│
├── data/                  # Fuentes de datos externas
│   └── DB_UNT_2.xlsx      # Base de datos con métricas GPS
│
├── utils/                 
│   └── pdf_generator.py   # Script para exportar los gráficos a PDF
```

---

## 📊 Funcionalidades Implementadas

### Página: `Home`
- Logo institucional
- Bienvenida e introducción al dashboard
- Botón de ingreso con autenticación

### Página: `Dashboard Performance`
- **Gráfico de dispersión**: Ritmo (MTS/MIN) vs Alta Intensidad (MTS-HSD)
- **Gráfico de barras**: Variables de carrera promedio por posición
- **Histograma**: Carga total (TOT-DIST) por sesión y posición
- Filtros por `posición` y `tipo de sesión`
- **Botón Exportar PDF**: Genera informe visual con logo, título e interpretación

---

## ✅ Tareas del Enunciado Cumplidas

- [x] Login/logout protegido con Flask-Login
- [x] Layout con navegación entre páginas
- [x] Dashboards con múltiples gráficos y filtros
- [x] Exportación a PDF personalizada
- [x] Código comentado y organizado
- [x] Diseño responsivo usando Bootstrap
- [x] Archivo `requirements.txt`
- [x] README detallado

---

## 🧠 Reflexión Final

Este proyecto me permitió consolidar conocimientos sobre desarrollo de aplicaciones interactivas con Dash y su integración con librerías complementarias como Flask-Login, FPDF y Plotly. Implementar un sistema de login, navegación multipágina, gráficos dinámicos con filtros, y exportación a PDF, ha sido un gran ejercicio de integración de habilidades.

Aprendí a manejar la estructura de carpetas de una app web profesional, los detalles de compatibilidad entre sistemas, y cómo organizar la documentación para facilitar la reutilización y el despliegue.

---

## 📧 Contacto

Sebastián Villalba  
📍 Santa Fe, Argentina  
📧 sebastiangvillalba@gmail.com
🔗 [LinkedIn](https://www.linkedin.com/in/sebastianvillalba/)

