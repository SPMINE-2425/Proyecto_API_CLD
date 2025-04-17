from fastapi import FastAPI
from pydantic import BaseModel, Field
import pandas as pd
import joblib
import os

# Clase con nombres de columnas originales
class StudentInput(BaseModel):
    Marital_Status: int = Field(alias="Marital Status")
    Application_mode: int = Field(alias="Application mode")
    Application_order: int = Field(alias="Application order")
    Course: int = Field(alias="Course")
    Daytime_evening_attendance: int = Field(alias="Daytime/evening attendance")
    Previous_qualification: int = Field(alias="Previous qualification")
    Previous_qualification_grade: float = Field(alias="Previous qualification (grade)")
    Nacionality: int = Field(alias="Nacionality")
    Mothers_qualification: int = Field(alias="Mother's qualification")
    Fathers_qualification: int = Field(alias="Father's qualification")
    Mothers_occupation: int = Field(alias="Mother's occupation")
    Fathers_occupation: int = Field(alias="Father's occupation")
    Admission_grade: float = Field(alias="Admission grade")
    Displaced: int = Field(alias="Displaced")
    Educational_special_needs: int = Field(alias="Educational special needs")
    Debtor: int = Field(alias="Debtor")
    Tuition_fees_up_to_date: int = Field(alias="Tuition fees up to date")
    Gender: int = Field(alias="Gender")
    Scholarship_holder: int = Field(alias="Scholarship holder")
    Age_at_enrollment: int = Field(alias="Age at enrollment")
    International: int = Field(alias="International")
    Curricular_1st_credited: int = Field(alias="Curricular units 1st sem (credited)")
    Curricular_1st_enrolled: int = Field(alias="Curricular units 1st sem (enrolled)")
    Curricular_1st_evaluations: int = Field(alias="Curricular units 1st sem (evaluations)")
    Curricular_1st_approved: int = Field(alias="Curricular units 1st sem (approved)")
    Curricular_1st_grade: float = Field(alias="Curricular units 1st sem (grade)")
    Curricular_1st_without_eval: int = Field(alias="Curricular units 1st sem (without evaluations)")
    Curricular_2nd_credited: int = Field(alias="Curricular units 2nd sem (credited)")
    Curricular_2nd_enrolled: int = Field(alias="Curricular units 2nd sem (enrolled)")
    Curricular_2nd_evaluations: int = Field(alias="Curricular units 2nd sem (evaluations)")
    Curricular_2nd_approved: int = Field(alias="Curricular units 2nd sem (approved)")
    Curricular_2nd_grade: float = Field(alias="Curricular units 2nd sem (grade)")
    Curricular_2nd_without_eval: int = Field(alias="Curricular units 2nd sem (without evaluations)")
    Unemployment_rate: float = Field(alias="Unemployment rate")
    Inflation_rate: float = Field(alias="Inflation rate")
    GDP: float = Field(alias="GDP")

# Cargar pipeline
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
pipeline_path = os.path.join(project_root, "Cuaderno/pipeline_final.gz")
pipeline = joblib.load(pipeline_path)

# Crear app
app = FastAPI(
    title="API de Predicción de Rendimiento Estudiantil",
    description="Esta API predice si un estudiante se gradúa, abandona o continúa, usando un modelo entrenado.",
    version="1.0"
)

# Ruta raíz
@app.get("/")
def read_root():
    return {"message": "La API está funcionando correctamente."}

# Endpoint de predicción
@app.post("/predict")
def predict(student: StudentInput):
    df = pd.DataFrame([student.dict(by_alias=True)])
    prediction = pipeline.predict(df)
    return {"prediction": prediction[0]}  # Retorna 'Graduate', 'Dropout', etc.
