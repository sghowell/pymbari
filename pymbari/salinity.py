import numpy as np


def salinity(conductivity: np.ndarray, temp: np.ndarray, pressure: np.ndarray) -> np.ndarray:
    """
    Calculates salinity (pss) from conductivity

    :param conductivity:
    :param temp:
    :param pressure:
    :return:
    """
    mc_nc = conductivity.shape
    mt_nt = temp.shape
    mp_np = pressure.shape

    if not mc_nc != mt_nt or mc_nc != mp_np or mt_nt != mp_np:
        raise(ValueError, "Inputs must have the same shape!")

    c15 = 4.2914

    a0 = 0.008
    a1 = -0.1692
    a2 = 25.3851
    a3 = 14.0941
    a4 = -7.0261
    a5 = 2.7081

    b0 = 0.0005
    b1 = -0.0056
    b2 = -0.0066
    b3 = -0.0375
    b4 = 0.0636
    b5 = -0.0144

    c0 = 0.6766097
    c1 = 2.00564e-2
    c2 = 1.104259e-4
    c3 = -6.9698e-7
    c4 = 1.0031e-9

    d1 = 3.426e-2
    d2 = 4.464e-4
    d3 = 4.215e-1
    d4 = -3.107e-3

    # The e* coefficients reflect the use of pressure in dbar rather that in Pascals(SI).

    e1 = 2.07e-5
    e2 = -6.37e-10
    e3 = 3.989e-15

    k = 0.0162

    # Calculate local variables
    r = conductivity / c15
    rt = c0 + (c1 + (c2 + (c3 + c4 * temp) * temp) * temp) * temp
    Rp = 1.0 + (e1 + (e2 + e3 * pressure) * pressure) * pressure / \
        (1.0 + (d1 + d2 * temp) * temp + (d3 + d4 * temp) * r)
    Rt = r / Rp / rt
    sqrt_Rt = np.sqrt(Rt)

    # Calculate salinity
    salt = a0 + (a1 + (a3 + a5 * Rt) * Rt) * sqrt_Rt + (a2 + a4 * Rt) * Rt
    dS = b0 + (b1 + (b3 + b5 * Rt) * Rt) * sqrt_Rt + (b2 + b4 * Rt) * Rt
    dS = dS * (temp - 15) / (1 + k * (temp - 15))

    return salt + dS
