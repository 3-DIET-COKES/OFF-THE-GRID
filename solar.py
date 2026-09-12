def calculate_solar_energy(
    solar_capacity_kw,
    solar_irradiance,
    efficiency=0.8
):
    energy = (
        solar_capacity_kw
        * solar_irradiance
        * efficiency
    )

    return energy


def calculate_hourly_solar(
    solar_capacity_kw,
    hourly_irradiance,
    efficiency=0.8
):
    solar_energy = []

    for irradiance in hourly_irradiance:

        energy = calculate_solar_energy(
            solar_capacity_kw,
            irradiance,
            efficiency
        )

        solar_energy.append(energy)

    return solar_energy


def calculate_required_solar(
    daily_load,
    hourly_irradiance,
    efficiency=0.8
):
    daily_sun_hours = sum(hourly_irradiance)

    solar_capacity = (
        daily_load
        / (daily_sun_hours * efficiency)
    )

    return solar_capacity