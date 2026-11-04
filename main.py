import os
from pathlib import Path
import joblib
from fastapi import FastAPI,HTTPException,Request
from pydantic import BaseModel, Field
import mlflow
import mlflow.sklearn
import numpy as np
from contextlib import asynccontextmanager
from typing import Callable


#Mlflow configuration
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "http://127.0.0.1:7001")

MODEL_URI = "models:/iris-classifier@champion"
MODEL_PATH = Path("models/iris_random_forest_model.joblib")

# Global variables
model = None
client = None
model_version = None

try:
    #Load the champion model at the application startup
    import socket
    socket.setdefaulttimeout(3)  # 3 second timeout
    
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    model = mlflow.sklearn.load_model(MODEL_URI)
    client = mlflow.MlflowClient()
    champion_version = client.get_model_version_by_alias(name="iris-classifier", alias="champion")
    model_version = champion_version.version
    print(f"Loaded champion model version: {model_version} from MLflow Model Registry")
    
    socket.setdefaulttimeout(None)  # Reset timeout
except Exception as e:
    print(f"Error loading champion model from MLflow: {e}")
    print(f"Loading local model from {MODEL_PATH}")
    model = joblib.load(MODEL_PATH)
    model_version = "local"
    print(f"Loaded local model successfully")

app = FastAPI(title="Iris Classifier API", description="API for predicting iris species using a trained Random Forest model.")

class IrisInput(BaseModel):
    sepal_length: float = Field(gt=0)
    sepal_width: float = Field(gt=0)
    petal_length: float = Field(gt=0)
    petal_width: float = Field(gt=0)





@app.get("/")
def health_check():
    return {"status": "Ready to serve"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict")
def predict(data: IrisInput):
    features = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]
    prediction = int(model.predict(features)[0])
    return {
        "prediction": prediction,
        "class_name": ["setosa", "versicolor", "virginica"][prediction]
    }
@app.get("/model_info")
def get_model_info():
    # Fetch model information from MLflow Model Registry
    try:
        model_version = client.get_model_version_by_alias(name="Iris_Classifier", alias="champion")
        return {
            "model_name": "Iris_Classifier",
            "version": model_version.version,
            "stage": model_version.current_stage,
            "run_id": model_version.run_id
        }
    except Exception as e:
        return {"error": f"Failed to fetch model info: {str(e)}"}
