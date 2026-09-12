from fastapi import FastAPI
from engine.sizing import calculate_system


app = FastAPI(
    title="OFF THE GRID",
    description="Rural sustainable energy planning system",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "OFF THE GRID API is running"
    }


@app.post("/calculate")
def calculate_energy(data: dict):

    devices = data["devices"]

    solar_irradiance = data["solar_irradiance"]

    wind_speed = data["wind_speed"]

    autonomy_days = data.get(
        "autonomy_days",
        2
    )

    result = calculate_system(
        devices,
        solar_irradiance,
        wind_speed,
        autonomy_days
    )

    return result