from engine.sizing import calculate_system


devices = [

    {
        "name": "LED Light",
        "power_w": 10,
        "hours_per_day": 6,
        "quantity": 10
    },

    {
        "name": "Router",
        "power_w": 20,
        "hours_per_day": 24,
        "quantity": 2
    },

    {
        "name": "Water Pump",
        "power_w": 500,
        "hours_per_day": 2,
        "quantity": 1
    }

]


solar_irradiance = [
    0,
    0,
    0,
    0,
    0,
    0.1,
    0.3,
    0.5,
    0.7,
    0.9,
    1.0,
    1.0,
    0.9,
    0.8,
    0.7,
    0.5,
    0.3,
    0.1,
    0,
    0,
    0,
    0,
    0,
    0
]


wind_speed = [
    5,
    5,
    6,
    6,
    7,
    7,
    8,
    8,
    7,
    6,
    5,
    5,
    6,
    7,
    8,
    8,
    7,
    6,
    6,
    5,
    5,
    5,
    5,
    5
]


result = calculate_system(
    devices,
    solar_irradiance,
    wind_speed,
    autonomy_days=2
)


print("\n==============================")
print("OFF THE GRID SYSTEM RESULT")
print("==============================")

print(
    "Daily Load:",
    round(result["daily_load_kwh"], 2),
    "kWh/day"
)

print(
    "Solar Capacity:",
    round(result["solar_capacity_kw"], 2),
    "kW"
)

print(
    "Wind Capacity:",
    round(result["wind_capacity_kw"], 2),
    "kW"
)

print(
    "Battery Capacity:",
    round(result["battery_capacity_kwh"], 2),
    "kWh"
)

print(
    "Average Solar:",
    round(result["average_solar"], 2)
)

print(
    "Average Wind:",
    round(result["average_wind"], 2),
    "m/s"
)

print(
    "Uptime:",
    round(
        result["simulation"]["uptime"],
        2
    ),
    "%"
)

print(
    "Blackout Hours:",
    result["simulation"]["blackout_hours"]
)

print("\n----- BILL OF MATERIALS -----")

print(
    "Solar:",
    result["bom"]["solar"]
)

print(
    "Wind:",
    result["bom"]["wind"]
)

print(
    "Battery:",
    result["bom"]["battery"]
)

print(
    "Estimated Total Cost:",
    result["bom"]["total_cost"],
    "INR"
)