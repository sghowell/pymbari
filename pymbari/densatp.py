#!


import numpy as np


def densatp(s, t, p):
	"""
	Calculate the density of seawater at a given s, t, and p.

	Equation of state from Millero & Poisson (1981) DSR V28: 625-629.

	:param s: Salinity in g/kg or pss
	:param t: Temperature in degrees c.
	:param p: Pressure in decibar
	:return: Density [rhp] in g/cc
	"""
	# Define constants for equation of state
	r0 = +9.99842594E2
	r1 = +6.793952E-2
	r2 = -9.095290E-3
	r3 = +1.001685E-4
	r4 = -1.120083E-6
	r5 = +6.536332E-9

	a0 = +8.24493E-1
	a1 = -4.0899E-3
	a2 = +7.6438E-5
	a3 = -8.2467E-7
	a4 = +5.3875E-9

	b0 = -5.72466E-3
	b1 = +1.0227E-4
	b2 = -1.6546E-6

	c = +4.8314E-4

	# Calculate rho
	sr = np.sqrt(s)
	rho_0 = r0 + t * (r1 + t * (r2 + t * (r3 + t * (r4 + t * r5))))
	a = a0 + t * (a1 + t * (a2 + t * (a3 + t * a4)))
	b = b0 + t * (b1 + t * b2)

	rho = rho_0 + s * (a + b * sr + c * s)

	# Define constants for secant bulk modulus
	d0 = +1.965221E+4
	d1 = +1.484206E+2
	d2 = -2.327105E+0
	d3 = +1.360477E-2
	d4 = -5.155288E-5

	e0 = +5.46746E+1
	e1 = -6.03459E-1
	e2 = +1.09987E-2
	e3 = -6.1670E-5

	f0 = +7.944E-2
	f1 = +1.6483E-2
	f2 = -5.3009E-4

	g0 = +3.239908E+0
	g1 = +1.43713E-3
	g2 = +1.16092E-4
	g3 = -5.77905E-7

	h0 = +2.2838E-3
	h1 = -1.0981E-5
	h2 = -1.6078E-6
	h3 = +1.91075E-4

	i0 = +8.50935E-5
	i1 = -6.12293E-6
	i2 = +5.2787E-8

	j0 = -9.9348E-7
	j1 = +2.0816E-8
	j2 = +9.1697E-10

	# Correct P in decibars to bars
	pc = p / 10

	# Calculate K
	h = h0 + t * (h1 + t * h2) + h3 * sr
	j = j0 + t * (j1 + t * j2)

	k1 = d0 + t * (d1 + t * (d2 + t * (d3 + t * d4)))
	k2 = e0 + t * (e1 + t * (e2 + t * e3))
	k3 = f0 + t * (f1 + t * f2)
	k4 = g0 + t * (g1 + t * (g2 + t * g3)) + s * h
	k5 = i0 + t * (i1 + t * i2) + s * j

	k = k1 + s * (k2 + sr * k3) + pc * (k4 + pc * k5)

	# Correct for pressure
	rhp = rho * (1. / (1. - pc / k))

	# Convert kg/m3 to g/cc
	rhp /= 1000.

	return rhp
