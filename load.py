def calculate_device_energy(power_watts, hours_per_day, quantity=1):
    energy_wh = power_watts * hours_per_day * quantity
    return energy_wh / 1000


def calculate_daily_load(devices):
    total_energy = 0

    for device in devices:
        energy = calculate_device_energy(
            device["power_w"],
            device["hours_per_day"],
            device.get("quantity", 1)
        )

        total_energy += energy

    return total_energy