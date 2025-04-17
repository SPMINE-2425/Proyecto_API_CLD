
# UNIVERSIDAD EXTERNADO DE COLOMBIA
# MINE VIII
# SEMINARIO DE PROGRAMACIÓN


# PROYECTO FINAL API

Estudiantes
1. Cindy Dayana Rozo Romero 
2. Diana Katherine Jimenez Contreras
3. Leyde Lorena Chaparro Cortes

# 🎓 Predicción de Deserción Estudiantil

Este proyecto permite predecir si un estudiante se va a graduar, abandonar o continuar en la universidad. Usa un modelo de machine learning, expuesto a través de una API creada con FastAPI y una interfaz de usuario con Streamlit.

---

## 📄 Documentación

### 🎯 Objetivo
Desarrollar una solución que permita predecir la deserción estudiantil mediante una interfaz sencilla y conectada a un modelo entrenado.

## 📌 Objetivos

- Predecir el resultado académico de un estudiante (Graduate, Dropout, Enrolled).
- Facilitar la interacción mediante una interfaz web.
- Integrar un modelo entrenado con datos reales (UCI Student Dataset).


## ⚙️ Tecnologías Usadas

- Python
- FastAPI
- Streamlit
- Pandas
- Joblib
- Uvicorn

---

## 📁 Estructura del Proyecto

```
Proyecto_API/
├── app/
│   └── app_streamlit.py           # Interfaz con Streamlit
├── Cuaderno/
│   └── pipeline_final.gz          # Modelo entrenado
├── main.py                        # API FastAPI
├── 1. Modelo de Predicción_student.ipynb  # Notebook de entrenamiento
```

### ⚙️ Componentes del Proyecto

- `main.py`: Contiene la API construida con FastAPI.
- `app/app_streamlit.py`: Interfaz de usuario hecha en Streamlit.
- `Cuaderno/pipeline_final.gz`: Modelo entrenado serializado.
- `1. Modelo de Predicción_student.ipynb`: Notebook donde se procesaron los datos y se entrenó el modelo.

### 🧠 Decisiones Tomadas

- Se seleccionaron variables relevantes del dataset de UCI para predecir el rendimiento del estudiante.
- Se creó un pipeline de preprocesamiento + modelo y se guardó con `joblib`.
- Se implementó la API con FastAPI para manejar las peticiones de predicción.
- Se diseñó una app sencilla en Streamlit para que cualquier usuario pueda usar el modelo.

### 📊 Resultados Obtenidos

- Predicciones en tiempo real que indican si un estudiante: **se gradúa, abandona o continúa**.
- Interfaz funcional conectada a la API.
- Proyecto replicable de forma local desde cualquier equipo.

---

## 🧪 Instrucciones para Ejecutar el Proyecto Localmente

### ✅ 1. Clonar el Repositorio

```bash
git clone https://github.com/SPMINE-2425/Proyecto_API_CLD.git
cd tu_repositorio
```

### ✅ 2. Crear y Activar un Entorno Virtual (opcional pero recomendado)

```bash
python -m venv env
```

- En **Windows**:
  ```bash
  .\env\Scripts\activate
  ```

- En **Mac/Linux**:
  ```bash
  source env/bin/activate
  ```

### ✅ 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### ✅ 4. Iniciar la API

En una terminal:

```bash
uvicorn main:app --reload
```

Esto levanta la API en: `http://127.0.0.1:8000`

### ✅ 5. Iniciar la App de Streamlit

En otra terminal:

```bash
streamlit run app/app_streamlit.py
```

Esto abrirá la app en el navegador en: `http://localhost:8501`

### ✅ 6. Usar la App

1. Completa el formulario con los datos del estudiante.
2. Haz clic en **Predecir**.
3. La predicción se mostrará en pantalla (Graduate, Dropout o Enrolled).

---