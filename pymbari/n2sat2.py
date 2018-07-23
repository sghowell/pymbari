#!

import numpy as np


def n2sat2(s, t):
	"""
	Calculate nitrogen concentration at saturation.

	Source: The solubility of neon, nitrogen, and argon in distilled water
			and seawater - Hamme & Emerson (2004) Deep Sea Research V51(11):
			1517-1528.  doi: 10.1016/j.dsr.2004.06.009.

	:param s: Salinity (0/00)
	:param t: Temperature in degrees c
	:return: Nitrogen saturation at one atmosphere in umol/kg
	"""
	# Define constants, etc for saturation calculation
	a0 = 6.42931
	a1 = 2.92704
	a2 = 4.32531
	a3 = 4.69149
	b0 = -7.44129e-03
	b1 = -8.02566e-03
	b2 = -1.46775e-02

	# Calculate nitrogen saturation
	ts = np.log((288.15 - t) / (273.15 + t))

	ln_c = a0 + ts * (a1 + ts * (a2 + ts * a3))
	ln_c += s * (b0 + ts * (b1 + ts * b2))
	n2 = np.exp(ln_c)

	return n2
