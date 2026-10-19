from fastapi import FastAPI
from pydantic import BaseModel  
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
#initialize the app 
app = FastAPI()

# Define our data structures 
#bedrooms	bathrooms	toilets	parking_space	title	town	state	price
class HouseData(BaseModel):
    bedrooms: int
    bathrooms: int
    toilets: int
    parking_space: int
    title: str
    town: str
    state: str
    price: float







# load the pretrained model 
with open('rf_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.get("/home")
def home():
    return {"message": "Welcome to the House Price Prediction API!"}

@app.post("/predict")
def predict_price(data: HouseData):
    # convert data to a DataFrame
    input_data = pd.DataFrame([data.dict()])
    # scale the input data
    scaler = StandardScaler()
    input_data_scaled = scaler.fit_transform(input_data[['bedrooms', 'bathrooms', 'toilets', 'parking_space']])

    # make prediction
    prediction = model.predict(input_data_scaled)

    return {"predicted_price": prediction[0]}




