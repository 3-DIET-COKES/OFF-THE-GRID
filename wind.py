def calculate_wind_power(
    wind_speed,
    rated_speed=12,
    cut_in_speed=3,
    cut_out_speed=25
):
    if wind_speed < cut_in_speed:
        return 0

    if wind_speed >= cut_out_speed:
        return 0

    if wind_speed >= rated_speed:
        return 1

    power_factor = (
        (wind_speed ** 3 - cut_in_speed ** 3)
        / (rated_speed ** 3 - cut_in_speed ** 3)
    )

    return power_factor


def calculate_wind_energy(
    wind_capacity_kw,
    wind_speed
):
    power_factor = calculate_wind_power(
        wind_speed
    )

    energy = (
        wind_capacity_kw
        * power_factor
    )

    return energy


def calculate_hourly_wind(
    wind_capacity_kw,
    hourly_wind_speed
):
    wind_energy = []

    for wind_speed in hourly_wind_speed:

        energy = calculate_wind_energy(
            wind_capacity_kw,
            wind_speed
        )

        wind_energy.append(energy)

    return wind_energy


def calculate_required_wind(
    daily_load,
    wind_fraction,
    average_wind_speed
):
    if average_wind_speed < 3:
        return 0

    capacity_factor = (
        average_wind_speed / 12
    ) ** 3

    if capacity_factor < 0.05:
        capacity_factor = 0.05

    wind_energy_required = (
        daily_load * wind_fraction
    )

    wind_capacity = (
        wind_energy_required
        / (24 * capacity_factor)
    )

    return wind_capacity