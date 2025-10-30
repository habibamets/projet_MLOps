from fastapi import FastAPI, HTTPException
import numpy as np
import pickle
from pydantic import BaseModel
import json
from pathlib import Path

class Iris(BaseModel):
    sepal_length:float
    sepal_width:float
    petal_length:float
    petal_width:float

app = FastAPI(title = "Iris Classifier API", description="Predict Iris species from 4 features")


model_path = Path(__file__).parent / 'iris_classifier.pkl'
metadata_path = Path(__file__).parent / 'model_metadata.json'

try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    model = None

try:
    if metadata_path.exists():
        with open(metadata_path, 'r') as f:
            metadata = json.load(f)
    else:
        metadata={}
except Exception:
    metadata = {}

@app.get("/")
def health_check():
    return {"message": "API is running"}

@app.post("/predict")
def predict(input_data: Iris):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not found")
    data = np.array([[input_data.sepal_length, input_data.sepal_width, input_data.petal_length, input_data.petal_width]])
    prediction = model.predict(data)
    return {"predicted_class": int(prediction[0]),
            "predicted_class_name": metadata.get("class_names")[int(prediction[0])],
            "metadata": metadata}