# pymbari
A Python 3 port of the MBARI (Monterey Bay Aquarium Research Institute) oceanography Matlab library

Simple Python functions for performing a variety of oceanographic calculations.

Includes functions for:
- oxygen utilization
- seawater density
- n2 saturation
- o2 saturation
- pH
- salinity
- vapor pressure
- speed of sound in seawater
- adiabatic temperature gradient
- depth
- potential temperature
- pressure

## Requirements
- numpy (>=1.14.x)
- mkl (optional)
- mxnet (optional, required for GPU acceleration)

## Installation
- Clone this repo `git clone https://github.com/sghowell/pymbari.git`
- `pip install -r requirements.txt`
- Run `setup.py` in a terminal
- NB: Only tested on Ubuntu

## Usage
```python
import numpy as np
from pymbari import depth, n2sat, o2sat, sample_data


conductivity, pressure, salinity, temperature = sample_data

d = depth(pressure, (-36.3453, 23.2342))
n2 = n2sat(salinity, temperature)
o2 = o2sat(salinity, temperature)
```

## References
Algorithms adapted from the Matlab code found here:
https://www.mbari.org/products/research-software/matlab-scripts-oceanographic-calculations/