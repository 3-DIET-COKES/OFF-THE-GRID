from engine.load import calculate_daily_load
from engine.load import calculate_hourly_load

from engine.solar import calculate_required_solar
from engine.solar import calculate_hourly_solar

from engine.wind import calculate_required_wind
from engine.wind import calculate_hourly_wind

from engine.battery import calculate_battery_capacity

from engine.simulation import simulate_24_hours

from engine.hardware import select_solar_panel
from engine.hardware import select_wind_turbine
from engine.hardware import select_battery
from engine.hardware import calculate_total_hardware_cost


def calculate_system(
    devices,
    solar_irradiance,
    wind_speed,
    autonomy_days,
    solar_fraction,
    wind_fraction,
    solar_efficiency,
    battery_efficiency,
    depth_of_discharge,

    panel_capacity_w,
    panel_price,

    turbine_capacity_kw,
    turbine_price,
    cut_in_speed,
    rated_speed,
    cut_out_speed,

    battery_capacity_kwh,
    battery_price
):

    daily_load = calculate_daily_load(
        devices
    )

    hourly_load = calculate_hourly_load(
        devices
    )

    average_wind_speed = (
        sum(wind_speed)
        / len(wind_speed)
    )

    solar_capacity = calculate_required_solar(
        daily_load * solar_fraction,
        solar_irradiance,
        solar_efficiency
    )

    wind_capacity = calculate_required_wind(
        daily_load,
        average_wind_speed,
        wind_fraction,
        cut_in_speed,
        rated_speed,
        cut_out_speed
    )

    battery_capacity = calculate_battery_capacity(
        daily_load,
        autonomy_days,
        depth_of_discharge,
        battery_efficiency
    )

    hourly_solar = calculate_hourly_solar(
        solar_capacity,
        solar_irradiance,
        solar_efficiency
    )

    hourly_wind = calculate_hourly_wind(
        wind_speed,
        wind_capacity,
        cut_in_speed,
        rated_speed,
        cut_out_speed
    )

    simulation = simulate_24_hours(
        hourly_load,
        hourly_solar,
        hourly_wind,
        battery_capacity,
        None,
        depth_of_discharge,
        battery_efficiency
    )

    solar_hardware = select_solar_panel(
        solar_capacity,
        panel_capacity_w,
        panel_price
    )

    wind_hardware = select_wind_turbine(
        wind_capacity,
        turbine_capacity_kw,
        turbine_price,
        cut_in_speed,
        rated_speed,
        cut_out_speed
    )

    battery_hardware = select_battery(
        battery_capacity,
        battery_capacity_kwh,
        battery_price
    )

    total_cost = calculate_total_hardware_cost(
        solar_hardware,
        wind_hardware,
        battery_hardware
    )

    return {
        "daily_load_kwh": daily_load,

        "solar_capacity_kw": solar_capacity,

        "wind_capacity_kw": wind_capacity,

        "battery_capacity_kwh": battery_capacity,

        "average_wind_speed": average_wind_speed,

        "simulation": simulation,

        "hardware": {
            "solar": solar_hardware,
            "wind": wind_hardware,
            "battery": battery_hardware
        },

        "total_cost": total_cost
    }