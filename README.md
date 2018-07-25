# pymbari
A Python 3 port of the MBARI (Monterey Bay Aquarium Research Institute) oceanography Matlab library (some of which is a port of various WHOI code).

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

Includes MKL and CUDA (via apache mxnet) acceleration options (Coming soon!)

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
from pymbari import depth, n2sat, o2sat
from pymbari.sample_data import SampleData


conductivity = SampleData.conductivity
pressure = SampleData.pressure
salinity = SampleData.salinity
temperature = SampleData.temperature

d = depth(pressure, (-36.3453, 23.2342))
n2 = n2sat(salinity, temperature)
o2 = o2sat(salinity, temperature)
```

## References
Algorithms adapted from the Matlab code found here:
https://www.mbari.org/products/research-software/matlab-scripts-oceanographic-calculations/