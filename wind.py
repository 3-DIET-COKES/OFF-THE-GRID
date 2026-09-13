def calculate_wind_power(
    wind_speed,
    wind_capacity_kw,
    cut_in_speed,
    rated_speed,
    cut_out_speed
):

    if wind_speed < cut_in_speed:
        return 0

    if wind_speed >= cut_out_speed:
        return 0

    if wind_speed >= rated_speed:
        return wind_capacity_kw

    power = (
        wind_capacity_kw
        * (
            wind_speed - cut_in_speed
        )
        / (
            rated_speed - cut_in_speed
        )
    )

    return power


def calculate_hourly_wind(
    wind_speed,
    wind_capacity_kw,
    cut_in_speed,
    rated_speed,
    cut_out_speed
):

    hourly_wind = []

    for speed in wind_speed:

        power = calculate_wind_power(
            speed,
            wind_capacity_kw,
            cut_in_speed,
            rated_speed,
            cut_out_speed
        )

        hourly_wind.append(power)

    return hourly_wind


def calculate_required_wind(
    daily_load,
    average_wind_speed,
    wind_fraction,
    cut_in_speed,
    rated_speed,
    cut_out_speed
):

    if average_wind_speed < cut_in_speed:
        return 0

    if average_wind_speed >= cut_out_speed:
        return 0

    if average_wind_speed >= rated_speed:
        power_factor = 1
    else:
        power_factor = (
            average_wind_speed - cut_in_speed
        ) / (
            rated_speed - cut_in_speed
        )

    if power_factor <= 0:
        return 0

    wind_capacity = (
        daily_load
        * wind_fraction
        / (
            24
            * power_factor
        )
    )

    return wind_capacity