# 🏃‍♂️ Dashboard Deportivo con Dash – Módulo 9

Aplicación web interactiva desarrollada como parte del **Máster en Python Avanzado Aplicado al Deporte (Módulo 9)**. 
Esta app permite visualizar, filtrar, analizar y exportar métricas físicas deportivas (como distancia total, ritmo e intensidad) a partir de una base de datos de GPS.

## 🧠 ¿Qué incluye esta app?

- Autenticación de usuarios (login / logout)
- Navegación multipágina: Home, Dashboard de Performance, Dashboard GPS
- Visualizaciones interactivas con filtros por posición y sesión
- Exportación automática del informe a PDF con tu logo y estilo
- Diseño responsivo con Bootstrap y estilos personalizados

---

## ⚙️ Requisitos previos

### 🔧 En Windows
1. Instalar [Anaconda](https://www.anaconda.com/products/distribution) (o Python 3.10+ si no usas Anaconda)
2. Crear entorno virtual (recomendado):
   ```bash
   conda create -n tarea_m9 python=3.10
   conda activate tarea_m9
   
📦 Instalación de dependencias
Una vez dentro del entorno virtual, ejecutar:
pip install -r requirements.txt

🚀 Cómo ejecutar la aplicación
Desde la raíz del proyecto (donde está app_dash.py):
python app_dash.py

Luego, abre tu navegador y accede a:
http://127.0.0.1:8050/

🔐 Acceso a la aplicación
Usuario: admin
Contraseña: admin

El sistema cuenta con control de sesiones mediante Flask-Login.

🗂️ Estructura del Proyecto

📁 TAREA_M9/
│
├── app_dash.py             # Archivo principal de la app Dash
├── requirements.txt        # Dependencias del proyecto
├── Procfile                # Archivo para despliegue en Heroku (opcional)
│
├── assets/                 # Recursos visuales y CSS
│   ├── custom.css          # Estilos personalizados
│   └── logo.png            # Logo usado en Home y en PDF
│
├── data/                   # Fuentes de datos externas
│   └── DB_UNT_2.xlsx       # Base de datos con métricas GPS
│
└── utils/
    └── pdf_generator.py    # Script para exportar los gráficos a PDF

📊 Funcionalidades del Dashboard
Página: Home
Presentación e introducción

Logo institucional

Botón de ingreso al sistema

Página: Dashboard Performance
Gráficos interactivos:

Dispersión: Ritmo vs Alta Intensidad

Barras: Variables por posición

Histograma: Carga total por sesión

Filtros por posición y tipo de sesión

Botón: 📤 Exportar PDF

Crea informe con logo, título y gráficos

Generado con fpdf y kaleido

Página: Dashboard GPS (No competitiva)
Tabla interactiva filtrable (DataTable)

Visualizaciones secundarias

Área física como ejemplo de sección no competitiva

🧪 Librerías principales utilizadas
Dash

Dash Bootstrap Components

Flask-Login

Pandas

Plotly

FPDF

Kaleido (exportación a imágenes)

🧾 Exportación a PDF
Genera un informe automático con:

Logo, título, párrafo introductorio

Gráficos de rendimiento

Se guarda como archivo temporal y se descarga automáticamente

🖥️ Diseño responsivo
La aplicación está diseñada para funcionar correctamente en:

🖥️ PC / Laptops

📱 Tablets y celulares

Gracias al uso de Dash Bootstrap Components y CSS personalizado (assets/custom.css).

🧠 Créditos
Proyecto desarrollado por Sebastián Villalba
Máster en Python Avanzado Aplicado al Deporte
Año: 2025

🪪 Licencia
Este proyecto tiene fines exclusivamente académicos y demostrativos.
© 2025 Sebastián Villalba - Todos los derechos reservados.
sebastiangvillalba@gmail.com

---

