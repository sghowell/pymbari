import numpy as np


def vapprs(salinity: np.ndarray, temp: np.ndarray) -> np.ndarray:
    """
    Calculate vapor pressure of seawater

    :param salinity:
    :param temp:
    :return:
    """
    # Convert degree C to degree K
    tk = temp + 273.15

    return np.exp(24.4543 - (6745.09 / tk) - 4.8489 * np.log(tk / 100.) - 0.000544 * salinity)
