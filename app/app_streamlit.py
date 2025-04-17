import streamlit as st
import requests

st.set_page_config(page_title="Predicción de Deserción Estudiantil", layout="centered")

# Título
st.title("🎓 Predicción de Deserción Estudiantil")

# Diccionarios para campos categóricos (puedes ajustar más)
GENERO = {"Masculino": 0, "Femenino": 1}
SI_NO = {"No": 0, "Sí": 1}

# Formulario
with st.form("student_form"):
    st.subheader("📋 Ingrese los datos del estudiante")

    marital_status = st.selectbox("Estado civil", [1, 2, 3])
    application_mode = st.selectbox("Modo de aplicación", [1, 2, 5, 10, 15, 51, 57, 90, 99])
    application_order = st.selectbox("Orden de aplicación", list(range(1, 20)))
    course = st.selectbox("Curso", [33, 171, 8014, 9003])
    attendance = st.radio("Jornada", ["Día", "Noche"])
    prev_qualification = st.selectbox("Titulación previa", [1, 2, 3, 4, 5, 6, 9])
    prev_grade = st.number_input("Nota titulación previa", min_value=0.0, max_value=200.0)
    nationality = st.selectbox("Nacionalidad", [1, 2])
    admission_grade = st.number_input("Nota de admisión", min_value=0.0, max_value=200.0)
    gender = st.radio("Género", list(GENERO.keys()))
    age = st.number_input("Edad de ingreso", min_value=15, max_value=100)
    debtor = st.selectbox("¿Es deudor?", list(SI_NO.keys()))
    tuition_up_to_date = st.selectbox("¿Pagos al día?", list(SI_NO.keys()))
    displaced = st.selectbox("¿Desplazado?", list(SI_NO.keys()))
    special_needs = st.selectbox("¿Necesidades especiales?", list(SI_NO.keys()))
    scholarship = st.selectbox("¿Becado?", list(SI_NO.keys()))
    international = st.selectbox("¿Extranjero?", list(SI_NO.keys()))

    st.markdown("### Rendimiento Académico")
    curr_1_enrolled = st.number_input("Materias 1er sem inscritas", 0)
    curr_1_approved = st.number_input("Materias 1er sem aprobadas", 0)

    st.markdown("### Contexto Económico")
    unemployment_rate = st.slider("Tasa de desempleo", 0.0, 20.0, 10.0)
    inflation_rate = st.slider("Tasa de inflación", 0.0, 15.0, 5.0)
    gdp = st.slider("PIB (GDP)", 0.0, 50000.0, 15000.0)

    submit = st.form_submit_button("📊 Predecir")

# Llamado a la API
if submit:
    data = {
        "Marital Status": marital_status,
        "Application mode": application_mode,
        "Application order": application_order,
        "Course": course,
        "Daytime/evening attendance": 0 if attendance == "Noche" else 1,
        "Previous qualification": prev_qualification,
        "Previous qualification (grade)": prev_grade,
        "Nacionality": nationality,
        "Mother's qualification": 1,
        "Father's qualification": 1,
        "Mother's occupation": 1,
        "Father's occupation": 1,
        "Admission grade": admission_grade,
        "Displaced": SI_NO[displaced],
        "Educational special needs": SI_NO[special_needs],
        "Debtor": SI_NO[debtor],
        "Tuition fees up to date": SI_NO[tuition_up_to_date],
        "Gender": GENERO[gender],
        "Scholarship holder": SI_NO[scholarship],
        "Age at enrollment": age,
        "International": SI_NO[international],
        "Curricular units 1st sem (credited)": 0,
        "Curricular units 1st sem (enrolled)": curr_1_enrolled,
        "Curricular units 1st sem (evaluations)": 0,
        "Curricular units 1st sem (approved)": curr_1_approved,
        "Curricular units 1st sem (grade)": 10.0,
        "Curricular units 1st sem (without evaluations)": 0,
        "Curricular units 2nd sem (credited)": 0,
        "Curricular units 2nd sem (enrolled)": 0,
        "Curricular units 2nd sem (evaluations)": 0,
        "Curricular units 2nd sem (approved)": 0,
        "Curricular units 2nd sem (grade)": 10.0,
        "Curricular units 2nd sem (without evaluations)": 0,
        "Unemployment rate": unemployment_rate,
        "Inflation rate": inflation_rate,
        "GDP": gdp
    }

    try:
        url = "http://127.0.0.1:8000/predict"
        res = requests.post(url, json=data)
        result = res.json()
        st.success(f"🎯 Resultado de la predicción: **{result['prediction']}**")
    except Exception as e:
        st.error(f"❌ Error al conectarse con la API: {e}")