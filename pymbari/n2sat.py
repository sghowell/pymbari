#!

import numpy as np


def n2sat(s, t):
	"""
	Calculate nitrogen (n2) concentration at saturation.

	Source: The solubility of nitrogen, oxygen and argon in water and
			seawater - Weiss (1970) Deep Sea Research V17(4): 721-735.
			http://webbook.nist.gov/chemistry/fluid/

	:param s: Salinity (0/00)
	:param t: Temperature degrees c
	:return: Nitrogen saturation at one atmosphere in umol/kg
	"""
	# Define constants, etc for saturation calculation
	t1 = (t + 273.15) / 100.

	nsat = -177.0212 + 254.6068 / t1 + 146.3611 * np.log(t1) - 22.0933 * t1
	nsat += s * (-0.054052 + t1 * (0.027266 - 0.0038430 * t1))
	nsat = np.exp(nsat)

	# Convert from ml/kg to um/kg
	n2 = nsat * 1000. / 22.404

	return n2
