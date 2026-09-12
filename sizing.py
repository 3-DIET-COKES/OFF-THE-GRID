from load import calculate_daily_load
from solar import calculate_required_solar
from wind import calculate_required_wind
from battery import calculate_battery_capacity
from solar import calculate_hourly_solar
from wind import calculate_hourly_wind
from simulation import simulate_24_hours
from hardware import create_bom


def create_hourly_load(daily_load):

    hourly_load = []

    for hour in range(24):

        hourly_load.append(
            daily_load / 24
        )

    return hourly_load


def calculate_system(
    devices,
    solar_irradiance,
    wind_speed,
    autonomy_days=2,
    solar_fraction=0.7,
    wind_fraction=0.3
):

    # --------------------------------
    # 1. Calculate daily load
    # --------------------------------

    daily_load = calculate_daily_load(
        devices
    )


    # --------------------------------
    # 2. Calculate average resources
    # --------------------------------

    average_solar = (
        sum(solar_irradiance)
        / len(solar_irradiance)
    )

    average_wind = (
        sum(wind_speed)
        / len(wind_speed)
    )


    # --------------------------------
    # 3. Calculate solar requirement
    # --------------------------------

   solar_capacity = calculate_required_solar(
    daily_load * solar_fraction,
    solar_irradiance
)

    # --------------------------------
    # 4. Calculate wind requirement
    # --------------------------------

    wind_capacity = calculate_required_wind(
        daily_load,
        wind_fraction,
        average_wind
    )


    # --------------------------------
    # 5. Calculate battery
    # --------------------------------

    battery_capacity = calculate_battery_capacity(
        daily_load,
        autonomy_days
    )


    # --------------------------------
    # 6. Generate hourly values
    # --------------------------------

    hourly_solar = calculate_hourly_solar(
        solar_capacity,
        solar_irradiance
    )

    hourly_wind = calculate_hourly_wind(
        wind_capacity,
        wind_speed
    )

    hourly_load = create_hourly_load(
        daily_load
    )


    # --------------------------------
    # 7. Run 24-hour simulation
    # --------------------------------

    simulation = simulate_24_hours(
        hourly_load,
        hourly_solar,
        hourly_wind,
        battery_capacity
    )


    # --------------------------------
    # 8. Select hardware
    # --------------------------------

    bom = create_bom(
        solar_capacity,
        wind_capacity,
        battery_capacity
    )


    # --------------------------------
    # 9. Return final result
    # --------------------------------

    return {

        "daily_load_kwh":
            daily_load,

        "solar_capacity_kw":
            solar_capacity,

        "wind_capacity_kw":
            wind_capacity,

        "battery_capacity_kwh":
            battery_capacity,

        "average_solar":
            average_solar,

        "average_wind":
            average_wind,

        "simulation":
            simulation,

        "bom":
            bom
    }