def adiabat(salinity: [float], pressure: [float], temperature: [float]) -> float:
    """
    Computes the adiabatic temperature gradient (called by Potentmp.m) and
    returns the gradient.

    REF: BRYDEN,H.,1973,DEEP-SEA RES.,20,401-408

    :param salinity:
    :param pressure:
    :param temperature:
    :return: atg
    """
    ds = salinity - 35.0
    # TODO: disentangle gigantic matlab expression into something more readable
    atg = (((-2.1687E-16 * temperature + 1.8676E-14) * temperature - 4.6206E-13) * pressure +
           ((2.7759E-12 * temperature - 1.1351E-10) * ds +
            ((-5.4481E-14 * temperature + 8.733E-12) * temperature - 6.7795E-10) * temperature + 1.8741E-8)) * \
        pressure + (-4.2393E-8 * temperature + 1.8932E-6) * ds + ((6.6228E-10 * temperature - 6.836E-8) * temperature +
                                                                  8.5258E-6) * temperature + 3.5803E-5
    return atg
