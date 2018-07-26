import numpy as np
from dataclasses import dataclass


@dataclass
class SampleData:
    __MAX_LEN: int = 1800
    temperature: np.ndarray = np.random.rand(__MAX_LEN)
    pressure: np.ndarray = np.random.rand(__MAX_LEN)
    salinity: np.ndarray = np.random.rand(__MAX_LEN)
    conductivity: np.ndarray = np.random.rand(__MAX_LEN)
    lat_lon: np.ndarray = np.mgrid[-90:90:0.1, -180:180:0.1]
    lat: np.ndarray = np.linspace(-90, 90, 1800)
    lon: np.ndarray = np.linspace(-180, 180, 1800)
