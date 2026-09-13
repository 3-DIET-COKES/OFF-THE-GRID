def select_solar_panel(
    required_capacity_kw,
    panel_capacity_w,
    panel_price
):

    number_of_panels = (
        required_capacity_kw * 1000
        / panel_capacity_w
    )

    number_of_panels = int(
        number_of_panels + 0.999
    )

    total_capacity_kw = (
        number_of_panels
        * panel_capacity_w
        / 1000
    )

    total_cost = (
        number_of_panels
        * panel_price
    )

    return {
        "type": "Solar Panel",
        "capacity_per_unit_w": panel_capacity_w,
        "quantity": number_of_panels,
        "total_capacity_kw": total_capacity_kw,
        "cost": total_cost
    }


def select_wind_turbine(
    required_capacity_kw,
    turbine_capacity_kw,
    turbine_price,
    cut_in_speed,
    rated_speed,
    cut_out_speed
):

    number_of_turbines = (
        required_capacity_kw
        / turbine_capacity_kw
    )

    number_of_turbines = int(
        number_of_turbines + 0.999
    )

    total_capacity_kw = (
        number_of_turbines
        * turbine_capacity_kw
    )

    total_cost = (
        number_of_turbines
        * turbine_price
    )

    return {
        "type": "Wind Turbine",
        "capacity_per_unit_kw": turbine_capacity_kw,
        "quantity": number_of_turbines,
        "total_capacity_kw": total_capacity_kw,
        "cut_in_speed": cut_in_speed,
        "rated_speed": rated_speed,
        "cut_out_speed": cut_out_speed,
        "cost": total_cost
    }


def select_battery(
    required_capacity_kwh,
    battery_capacity_kwh,
    battery_price
):

    number_of_batteries = (
        required_capacity_kwh
        / battery_capacity_kwh
    )

    number_of_batteries = int(
        number_of_batteries + 0.999
    )

    total_capacity_kwh = (
        number_of_batteries
        * battery_capacity_kwh
    )

    total_cost = (
        number_of_batteries
        * battery_price
    )

    return {
        "type": "Battery",
        "capacity_per_unit_kwh": battery_capacity_kwh,
        "quantity": number_of_batteries,
        "total_capacity_kwh": total_capacity_kwh,
        "cost": total_cost
    }


def calculate_total_hardware_cost(
    solar,
    wind,
    battery
):

    total_cost = (
        solar["cost"]
        + wind["cost"]
        + battery["cost"]
    )

    return total_cost