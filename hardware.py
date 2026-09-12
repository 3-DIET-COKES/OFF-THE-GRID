solar_panels = [
    {
        "name": "500W Solar Panel",
        "capacity_kw": 0.5,
        "price": 18000
    },

    {
        "name": "550W Solar Panel",
        "capacity_kw": 0.55,
        "price": 20000
    }
]


wind_turbines = [
    {
        "name": "1kW Wind Turbine",
        "capacity_kw": 1,
        "price": 120000
    },

    {
        "name": "2kW Wind Turbine",
        "capacity_kw": 2,
        "price": 220000
    },

    {
        "name": "3kW Wind Turbine",
        "capacity_kw": 3,
        "price": 320000
    }
]


batteries = [
    {
        "name": "5kWh LiFePO4 Battery",
        "capacity_kwh": 5,
        "price": 90000
    },

    {
        "name": "10kWh LiFePO4 Battery",
        "capacity_kwh": 10,
        "price": 170000
    },

    {
        "name": "15kWh LiFePO4 Battery",
        "capacity_kwh": 15,
        "price": 245000
    }
]


def select_solar_panel(required_capacity):

    panel = solar_panels[0]

    quantity = int(
        required_capacity
        / panel["capacity_kw"]
    )

    if (
        quantity * panel["capacity_kw"]
        < required_capacity
    ):
        quantity += 1

    total_capacity = (
        quantity
        * panel["capacity_kw"]
    )

    total_cost = (
        quantity
        * panel["price"]
    )

    return {
        "name": panel["name"],
        "quantity": quantity,
        "capacity_kw": total_capacity,
        "cost": total_cost
    }


def select_wind_turbine(required_capacity):

    if required_capacity <= 0:

        return {
            "name": None,
            "quantity": 0,
            "capacity_kw": 0,
            "cost": 0
        }

    for turbine in wind_turbines:

        if (
            turbine["capacity_kw"]
            >= required_capacity
        ):

            return {
                "name": turbine["name"],
                "quantity": 1,
                "capacity_kw":
                    turbine["capacity_kw"],
                "cost":
                    turbine["price"]
            }

    turbine = wind_turbines[-1]

    quantity = int(
        required_capacity
        / turbine["capacity_kw"]
    )

    if (
        quantity
        * turbine["capacity_kw"]
        < required_capacity
    ):
        quantity += 1

    return {
        "name": turbine["name"],
        "quantity": quantity,
        "capacity_kw":
            quantity * turbine["capacity_kw"],
        "cost":
            quantity * turbine["price"]
    }


def select_battery(required_capacity):

    battery = batteries[0]

    quantity = int(
        required_capacity
        / battery["capacity_kwh"]
    )

    if (
        quantity
        * battery["capacity_kwh"]
        < required_capacity
    ):
        quantity += 1

    total_capacity = (
        quantity
        * battery["capacity_kwh"]
    )

    total_cost = (
        quantity
        * battery["price"]
    )

    return {
        "name": battery["name"],
        "quantity": quantity,
        "capacity_kwh": total_capacity,
        "cost": total_cost
    }


def create_bom(
    solar_capacity,
    wind_capacity,
    battery_capacity
):

    solar = select_solar_panel(
        solar_capacity
    )

    wind = select_wind_turbine(
        wind_capacity
    )

    battery = select_battery(
        battery_capacity
    )

    total_cost = (
        solar["cost"]
        + wind["cost"]
        + battery["cost"]
    )

    return {
        "solar": solar,
        "wind": wind,
        "battery": battery,
        "total_cost": total_cost
    }