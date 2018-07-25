import numpy as np


def o2satv2a(salinity: np.ndarray, temp: np.ndarray) -> np.ndarray:
    """
    Calculate O2 concentration at saturation

    :param salinity:
    :param temp:
    :return:
    """
    # Define constants, etc. for saturation calculation
    # The constants used are for units of mL O2 / L.
    a0 = 2.00856
    a1 = 3.22400
    a2 = 3.99063
    a3 = 4.80299
    a4 = 9.78188e-01
    a5 = 1.71069

    b0 = -6.24097e-03
    b1 = -6.93498e-03
    b2 = -6.90358e-03
    b3 = -4.29155e-03

    c0 = -3.11680e-07

    # Calculate Ts from T (deg C)
    ts = np.log((298.15 - temp) / (273.15 + temp))

    # Calculate O2 saturation in mL O2/L.
    a = ((((a5 * ts + a4) * ts + a3) * ts + a2) * ts + a1) * ts + a0

    b = ((b3 * ts + b2) * ts + b1) * ts + b0

    return np.exp(a + salinity * (b + salinity * c0))
