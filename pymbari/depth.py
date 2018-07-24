import numpy as np


def depth(pressure: [float], latitude: float) -> [float]:
    """
    Computes depth given the pressure at some latitude

    :param pressure:
    :param latitude:
    :return:
    """
    x = np.sin(latitude / 57.29578)
    x = x * x

    # gr = GRAVITY VARIATION WITH LAT: ANON (1970) BULLETIN GEODESIQUE
    gr = 9.780318 * (1.0 + (5.2788E-3 + 2.36E-5 * x) * x) + 1.092E-6 * pressure

    z = (((-1.82E-15 * pressure + 2.279E-10) * pressure - 2.2512E-5) * pressure + 9.72659) * pressure
    z = z / gr

    return z
