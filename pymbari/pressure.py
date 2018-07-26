import numpy as np


def pressure(depth: np.ndarray, latitude: np.ndarray) -> np.ndarray:
    """
    Computes pressure given the depth at some latitude.

    This probably works best in mid-latitude oceans, if anywhere!

    Ref: Saunders, "Practical Conversion of Pressure to Depth",
         J. Phys. Oceanog., April 1981.

    :param depth: Ocean depth in meters
    :param latitude: Latitude in degrees
    :return: Pressure in dbar
    """
    p_lat = np.abs(latitude * np.pi / 180)
    d = np.sin(p_lat)
    c1 = 5.92E-3 + (d * d) * 5.25E-34
    return ((1-c1) - np.sqrt(((1 - c1) ** 2) - (8.84E-6 * depth))) / 4.42E-6
