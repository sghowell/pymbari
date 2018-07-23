#!


import numpy as np


def density(s, t):
	"""
	Calculate the density of seawater at a given salinity and temperature.
	Pressure is assumed to be 1 ATM. (ie, that the ocean is at sea level.)

	:param s: Salinity in g/kg or pss
	:param t: Temperature in degrees c.
	:return: Density (rho) in g/cc
	"""
	# Define constants for equation of state
	r0 = 9.99842594E2
	r1 = 6.793952E-2
	r2 = -9.095290E-3
	r3 = 1.001685E-4
	r4 = -1.120083E-6
	r5 = 6.536332E-9

	a0 = 8.24493E-1
	a1 = -4.0899E-3
	a2 = 7.6438E-5
	a3 = -8.2467E-7
	a4 = 5.3875E-9

	b0 = -5.72466E-3
	b1 = 1.0227E-4
	b2 = -1.6546E-6

	c = 4.8314E-4

	# Calculate rho
	rho_0 = r0 + t * (r1 + t * (r2 + t * (r3 + t * (r4 + t * r5))))

	a = a0 + t * (a1 + t * (a2 + t * (a3 + t * a4)))
	b = b0 + t * (b1 + t * b2)
	rho = (rho_0 + s * (a + b * np.sqrt(s) + c * s)) / 1000.

	return rho
