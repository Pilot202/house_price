from fastapi import FastAPI
from pydantic import BaseModel  
import pickle
import pandas as pd
import numpy as np
# import request 

#initialize the app 
app = FastAPI()

# Define our data structures 
# Define the prediction request fields. Price is the value being predicted.
class HouseData(BaseModel):
    bedrooms: int
    bathrooms: int
    toilets: int
    parking_space: int
    title: str
    town: str
    state: str

# load the pretrained model 
with open('rf_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.get("/home")
def home():
    return {"message": "Welcome to the House Price Prediction API!"}








@app.post("/predict")
def predict_price(data: HouseData):
    input_data = pd.DataFrame([data.dict()])
    encoded_input = pd.get_dummies(
        input_data,
        columns=["title", "town", "state"],
    )

    training_features = getattr(model, "feature_names_in_", None)
    if training_features is None:
        raise ValueError(
            "The saved model has no training feature names. Retrain and save it "
            "with the encoded training DataFrame."
        )

    encoded_input = encoded_input.reindex(columns=training_features, fill_value=0)
    log_price_pred = model.predict(encoded_input)[0]
    return {"predicted_price": float(np.exp(log_price_pred))}


    




