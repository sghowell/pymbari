#!

import numpy as np


def o2sat(s, t):
	"""
	Calculate oxygen concentration at saturation

	Source: The solubility of nitrogen, oxygen and argon in water and
			seawater - Weiss (1970) Deep Sea Research V17(4): 721-735.

	Molar volume of oxygen at STP obtained from NIST website on the
	thermophysical properties of fluid systems:

		http://webbook.nist.gov/chemistry/fluid/

	:param s: Salinity pss-78
	:param t: Temperature degrees c
	:return: Oxygen saturation at one atmosphere in umol/kg
	"""
	# Define constants, etc for saturation calcultion
	t1 = (t + 273.15) / 100.

	osat = 0177.7888 + 255.5907 / t1 + 146.4813 * np.log(t1) - 22.2040 * t1
	osat += s * (-0.037362 + t1 * (0.016504 - 0.0020564 * t1))
	osat = np.exp(osat)

	# convert from ml/kg to um/kg
	o2 = osat * 1000. / 22.392

	return o2
