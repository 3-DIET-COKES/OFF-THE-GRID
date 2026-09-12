def simulate_24_hours(
    hourly_load,
    hourly_solar,
    hourly_wind,
    battery_capacity,
    initial_soc=None,
    depth_of_discharge=0.9,
    battery_efficiency=0.95
):

    if initial_soc is None:
        initial_soc = battery_capacity

    minimum_soc = (
        battery_capacity
        * (1 - depth_of_discharge)
    )

    current_soc = initial_soc

    results = []

    blackout_hours = 0

    total_load = 0
    total_solar = 0
    total_wind = 0

    for hour in range(24):

        load = hourly_load[hour]

        solar = hourly_solar[hour]

        wind = hourly_wind[hour]

        generation = solar + wind

        net_energy = generation - load

        if net_energy >= 0:

            stored_energy = (
                net_energy
                * battery_efficiency
            )

            current_soc += stored_energy

            if current_soc > battery_capacity:
                current_soc = battery_capacity

            blackout = False

        else:

            energy_needed = abs(net_energy)

            available_energy = (
                current_soc
                - minimum_soc
            )

            if available_energy >= energy_needed:

                current_soc -= energy_needed

                blackout = False

            else:

                current_soc = minimum_soc

                blackout = True

                blackout_hours += 1

        total_load += load
        total_solar += solar
        total_wind += wind

        results.append({
            "hour": hour,
            "load": load,
            "solar": solar,
            "wind": wind,
            "generation": generation,
            "battery_soc": current_soc,
            "blackout": blackout
        })

    uptime = (
        (24 - blackout_hours)
        / 24
        * 100
    )

    return {
        "hourly_results": results,
        "total_load": total_load,
        "total_solar": total_solar,
        "total_wind": total_wind,
        "blackout_hours": blackout_hours,
        "uptime": uptime
    }