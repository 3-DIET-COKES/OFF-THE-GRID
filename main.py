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

    result = calculate_system(

        # Site and load data
        data["devices"],
        data["solar_irradiance"],
        data["wind_speed"],

        # System configuration
        data["autonomy_days"],
        data["solar_fraction"],
        data["wind_fraction"],
        data["solar_efficiency"],
        data["battery_efficiency"],
        data["depth_of_discharge"],

        # Solar hardware
        data["panel_capacity_w"],
        data["panel_price"],

        # Wind hardware
        data["turbine_capacity_kw"],
        data["turbine_price"],
        data["cut_in_speed"],
        data["rated_speed"],
        data["cut_out_speed"],

        # Battery hardware
        data["battery_capacity_kwh"],
        data["battery_price"]
    )

    return result