from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def read_root():
    return {"message": "ML API is running!"}

@app.get("/predict/")
def predict(x: float, y: float):
    data = np.array([[x, y]])
    prediction = model.predict(data)
    return {"prediction": prediction.tolist()}
