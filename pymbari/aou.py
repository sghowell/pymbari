#!


import numpy as np


def aou(s, t, o2):
	"""
	Calculate oxygen concentration at saturation.

	Python port of MBARI Matlab scripts by Edward T Peltzer.

	Source:  The solubility of nitrogen, oxygen and argon in water and
			seawater - Weiss (1970) Deep Sea Research V17(4): 721-735.

	Molar volume of oxygen at STP obtained from NIST website on the
	thermophysical properties of fluid systems:

	http://webbook.nist.gov/chemistry/fluid/


	CALCULATE AOU BY DIFFERENCE:

	AOU (umol/kg) = sat O2 (umol/kg) - obs o2 (umol/kg).


	:param s: Salinity (pss-78)
	:param t: Potential Temp (deg C)
	:param o2: Measured Oxygen Concentration (umol/kg)
	:return: Apparant Oxygen Utilization (umol/kg)
	"""
	# DEFINE CONSTANTS, ETC FOR SATURATION CALCULATION
	# The constants -177.7888, etc., are used for units of ml O2/kg.
	t1 = (t + 273.15) / 100

	o_sat = -177.7888 + 255.5907 / t1 + 146.4813 * np.log(t1) - 22.2040 * t1
	o_sat = o_sat + s * (-0.037362 + t1 * (0.016504 - 0.0020564 * t1))
	o_sat = np.exp(o_sat)

	# CONVERT FROM ML/KG TO UM/KG
	o_sat *= 1000. / 22.392

	return o_sat - o2
