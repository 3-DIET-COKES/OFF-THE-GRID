def calculate_battery_capacity(
    daily_load,
    autonomy_days,
    depth_of_discharge,
    efficiency
):

    battery_capacity = (
        daily_load
        * autonomy_days
        /
        (
            depth_of_discharge
            * efficiency
        )
    )

    return battery_capacity


def calculate_minimum_soc(
    battery_capacity,
    depth_of_discharge
):

    minimum_soc = (
        battery_capacity
        * (1 - depth_of_discharge)
    )

    return minimum_soc


def charge_battery(
    current_soc,
    generation,
    load,
    battery_capacity,
    efficiency
):

    net_energy = generation - load

    if net_energy > 0:

        stored_energy = (
            net_energy
            * efficiency
        )

        new_soc = (
            current_soc
            + stored_energy
        )

        if new_soc > battery_capacity:
            new_soc = battery_capacity

    else:

        new_soc = (
            current_soc
            + net_energy
        )

    return new_soc