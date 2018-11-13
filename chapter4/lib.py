# Imports:
import math
import numpy as np
import matplotlib.pyplot as pl
from datetime import datetime

# Constants:
LOWER_LIMIT = 0
UPPER_LIMIT = 1
INTERVALS = 3
ERRO = 1e-4
RESULTS = [0, np.inf]

# Functions:
def f(x):
    return (3*x**(1/3))*(np.e**(-x**(2)))
