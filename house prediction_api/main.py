import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

model = joblib.load("house_model.joblib")
features = joblib.load("house_features.joblib")

# input schema
class HouseFeatures(BaseModel):
    MedInc: float = Field(gt=0,description="Media Income of"  \
                          "Neighbourhood")
    HouseAge : float=Field(gt=0, description="Average age of house in the block")
    AveRooms: float=Field(gtgt=0, description="Average number of house in the block")
    AveBedrms: float=Field(gtgt=0, description="Average number of house in the rooms")
    Population: float=Field(gtgt=0, description="Total Population")
    AveOccup: float=Field(gtgt=0, description="Average age of house Occupied")
    Latitude: float=Field(gtgt=0, description="Latitude")
    Longitude: float=Field(gtgt=0, description="Longitude")

# home
@app.get("/")
def home():
    return {
        "message":"California house prediction api",
        "status":"running",
        "endpoint":"send POST request to /predict"
    }               

@app.get("/health")
def health():
    return {
        "status":"running",
        "model":"RandomForestRegressor",
        "features":features,
        "avg_error":"$39,000"
    }

# prediction
@app.post("/predict")
def predict(house: HouseFeatures):
    try:
        input_data = pd.DataFrame([{
            "MedInc": house.MedInc,
            "HouseAge":house.HouseAge,
            "AveRooms":house.AveRooms,
            "AveBedrms":house.AveBedrms,
            "Population":house.Population,
            "AveOccup":house.AveOccup,
            "Latitude":house.Latitude,
            "Longitude":house.Longitude
        }])

        predicted = model.predict(input)[0]
        price_usd = predicted * 100000

        return {
            "predicted_price": f"${price_usd:,.0f}",
            "predicted_price_short": f"${predicted:.2f} house thousands",
            "findence_range":f"${price_usd - 39000:,.0f} to ${price_usd + 39000:,.0f}"
        }
    
    except Exception as e:
        raise HTTPException(
            status_code = 500,
            detail=f"prediction failed: {str(e)}"
        )
