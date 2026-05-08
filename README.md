# 🤖 Simulador de entrevistas con IA

Un simulador de entrevistas conversacionales creado con **Streamlit** y **OpenAI GPT-4o-mini** que permite a los usuarios practicar entrevistas de trabajo y recibir comentarios personalizados de IA

---

## 📋 Descripción

Esta aplicación simula una entrevista de trabajo real realizada por un ejecutivo de recursos humanos con inteligencia artificial. El usuario proporciona su información personal, selecciona una empresa y un puesto, y luego mantiene una conversación de 5 preguntas con la IA. Al finalizar, la aplicación genera comentarios detallados con una puntuación del 1 al 10.

---

## ✨ Características

- **Configuración personalizada**: introduce tu nombre, experiencia y habilidades antes de empezar.
- **Múltiples roles y empresas**: elige entre puestos como Científico de Datos, Ingeniero de Datos, Analista de BI y Analista Financiero en empresas como Amazon, Meta, Spotify y muchas más.
- **Entrevista realista**: la IA adapta sus preguntas al puesto, nivel y empresa seleccionados.
- **Retroalimentación automática**: tras 5 intercambios, recibe una evaluación detallada con puntuación y sugerencias constructivas.
- **Interfaz sencilla e intuitiva**: desarrollada íntegramente con Streamlit.

---

## 🛠️ Tecnologías

- [Python 3.10+](https://www.python.org/)
- [Streamlit](https://streamlit.io/) — Interface Web
- [OpenAI API](https://platform.openai.com/) — GPT-4o-mini model
- [streamlit-js-eval](https://pypi.org/project/streamlit-js-eval/) — Funcionalidad de reinicio de página

---

## 🚀 Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/mauroacampani/interview-tool.git
cd git clone https://github.com/mauroacampani/interview-tool.git

```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la clave API de OpenAI

Crear un archivo `.streamlit/secrets.toml` en la raíz del proyecto:

```toml
OPENAI_API_KEY = "tu-clave-api"
```


### 5. Ejecutar la aplicación

```bash
streamlit run app.py
```

---

## 📁 Estructura del proyecto

```
interview-tool/
├── app.py                  # Aplicación principal
├── requirements.txt        # Dependencias del proyecto
├── .gitignore
└── .streamlit/
    └── secrets.toml        # Clave API (no incluida en el repositorio)
```

---

## 📦 requirements.txt

```
streamlit
openai
streamlit-js-eval
```

---

## 🎮 Cómo usar

1. Ingresa tu **nombre**, **experiencia** y **habilidades**.
2. Selecciona tu **nivel** (Junior / Intermedio / Senior), **puesto** y **empresa**.
3. Haz clic en **"Comienza la entrevista"** para empezar.
4. Preséntate y responde las preguntas del entrevistador (5 intercambios en total).
5. Haz clic en **"Obtener retroalimentación"** para recibir tu puntuación y comentarios personalizados.

---

## 🔒 Notas de seguridad

- Las claves API se gestionan mediante `st.secrets` y nunca se incluyen directamente en el código fuente.
- El archivo `.streamlit/secrets.toml` siempre debe excluirse del control de versiones.

---

## 🙋 Author


[LinkedIn](https://linkedin.com/in/maurocampani) · [GitHub](https://github.com/mauroacampani)

---
