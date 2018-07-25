import numpy as np


class SampleData:
    __MAX_LEN = 500000
    temperature = np.random.rand(__MAX_LEN)
    pressure = np.random.rand(__MAX_LEN)
    salinity = np.random.rand(__MAX_LEN)
    conductivity = np.random.rand(__MAX_LEN)
