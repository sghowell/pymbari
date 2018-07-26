import numpy as np
from pymbari.pressure import pressure


def v_sound(salinity: np.ndarray, temp: np.ndarray, pressure: np.ndarray, alg: str="un95"):
    """

    :param salinity:
    :param temp:
    :param pressure:
    :param alg:
    :return:
    """
    valid_algorithms = {"v1", "v2", "un95"}
    if not alg or alg not in valid_algorithms:
        raise(ValueError, "Invalid sound velocity algorithm specified!")

    if alg == "v1":
        raise(NotImplementedError, "Peltzer & Ryan algorithm not yet implemented")

    if alg == "v2":
        raise(NotImplementedError, "Peltzer & Ryan algorithm not yet implemented")

    if alg == "un95":
        raise(NotImplementedError, "UN95 algorithm not yet implemented")
