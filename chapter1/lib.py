# Imports:
from scipy.misc import derivative
import numpy as np
import matplotlib.pyplot as pl
from datetime import datetime

# Constants:
ERRO = 1e-2
STEPS = 2e-1
LOW_LIMIT = -100
HIGH_LIMIT = 100
START_A = -3
START_B = -2.5
START_GUESS = -2.5

# Classes:
class Table(object):
    def __init__(self):
        self.iters = []

    def show(self, name):
        print("+----------+----------------+----------------+----------------+----------------------+")
        print("| {:^82} |".format(name))
        print("+----------+----------------+----------------+----------------+----------------------+")
        print("|  ITERS   |        A       |        B       |       Xn       |         F(X)         |")
        print("+----------+----------------+----------------+----------------+----------------------+")
        for iter in self.iters:
            print("| {:8.0f} | {:14.10f} | {:14.10f} | {:14.10f} | {:20.10f} |".format(iter[0], iter[1], iter[2], iter[3], iter[4]))
        print("+----------+----------------+----------------+----------------+----------------------+")

# Functions:
f = lambda x: (x**3) - (5*(x**2)) + x + 6
#f = lambda x: (np.e**(np.cos(x))) + (x**3) - (3)
#f = lambda x: (0.1*(x**3)) - (np.e**(2*x)) + (2)
#f = lambda x: x**2 + 2
#f = lambda x: 2*x**3
#f = lambda x: (1*x**2) - (1*x) + 10
#f = lambda x: (1*x**3) - (2*x**2) - 10*x + 4
#f = lambda x: (0.1*x**3) - (np.e**(2*x)) + 2
#f = lambda x: np.cos(x) / np.sin(x)

def derivada(f):
    def calculaDev(x, dx=1e-8):
        return (f(x+dx) - f(x))/dx
    return calculaDev
df = derivada(f)
