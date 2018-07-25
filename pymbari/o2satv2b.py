import numpy as np


def o2satv2b(salinity: np.ndarray, temp: np.ndarray) -> np.ndarray:
    """
    Calculate oxygen concentration at saturation

    :param salinity:
    :param temp:
    :return:
    """
    # Define constants, etc. for saturation calculation
    # The constants used are for units of umol O2/kg
    a0 = 5.80818
    a1 = 3.20684
    a2 = 4.11890
    a3 = 4.93845
    a4 = 1.01567
    a5 = 1.41575

    b0 = -7.01211e-03
    b1 = -7.25958e-03
    b2 = -7.93334e-03
    b3 = -5.54491e-03

    c0 = -1.32412e-07

    # Calculate Ts from T (deg C)

    ts = np.log((298.15 - temp) / (273.15 + temp))

    # Calculate O2 saturation in umol O2 / kg

    a = ((((a5 * ts + a4) * ts + a3) * ts + a2) * ts + a1) * ts + a0

    b = ((b3 * ts + b2) * ts + b1) * ts + b0

    return np.exp(a + salinity * (b + salinity * c0))
