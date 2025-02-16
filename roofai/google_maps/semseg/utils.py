import math


# https://chatgpt.com/c/67b173a0-26cc-8005-9bb4-46bfbc1d53ee
def meters_to_degrees(
    lat: float,
    delta_in_m: float,
    direction: str,
) -> float:
    earth_radius = 6378137.0

    # Conversion factor from degrees to radians
    degrees_to_radians = math.pi / 180.0

    # Calculate the number of degrees latitude per meter
    meters_per_degree_latitude = earth_radius * degrees_to_radians

    # Calculate the number of degrees longitude per meter
    # The radius of a circle of latitude decreases with the cosine of the latitude
    meters_per_degree_longitude = meters_per_degree_latitude * math.cos(
        lat * degrees_to_radians
    )

    if direction == "lat":
        return delta_in_m / meters_per_degree_latitude

    if direction == "lon":
        return delta_in_m / meters_per_degree_longitude

    raise ValueError(f"'lat' or 'lon' expected, received '{direction}'!")
