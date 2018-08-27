# Imports:
import numpy as np

# Constants:
ERRO = 1e-2
LOW_LIMIT = -200
HIGH_LIMIT = 200
START_A = -3
START_B = -2

# Classes:
class Table(object):
    def __init__(self):
        self.iters = []

    def show(self, name):
        print("+----------------+----------------+----------------+----------------+----------------+")
        print("| {:^82} |".format(name))
        print("+----------------+----------------+----------------+----------------+----------------+")
        print("|   ITERATION    |        A       |        B       |       XN       |      F(X)      |")
        print("+----------------+----------------+----------------+----------------+----------------+")
        for iter in self.iters:
            print("| {:14.0f} | {:14.10f} | {:14.10f} | {:14.10f} | {:14.10f} |".format(iter[0], iter[1], iter[2], iter[3], iter[4]))
        print("+----------------+----------------+----------------+----------------+----------------+")

# Functions:
def f(x):
    #return (np.e**(np.cos(x))) + (x**3) - (3)
    return (0.1*(x**3)) - (np.e**(2*x)) + (2)
    #return (x**3) - (5*(x**2)) + x + 3
