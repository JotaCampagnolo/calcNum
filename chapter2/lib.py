# Imports:
import numpy as np
import matplotlib.pyplot as pl
from datetime import datetime

# Constants:
ERRO = 1e-2 # Absolute error to stop the program.
MAX_ITER = 1000 # Maximum of iterations to stop the program.
A = np.array([ # A Matrix:
    [3, 1],
    [2, 2]
])
B = np.array([5, 4]) # Independent terms.
X = np.array([0, 0]) # Guess vector.

# Function:
def stopCrit(A, B, X):
    return sum(abs(np.dot(A, X) - B))


def printIteration(method, X, M, ITER):
    print("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
    print("| {:^48} |".format(method + " METHOD"))
    print("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
    for i in range(len(X)):
        print("| {:^12} | {:>33} |".format("X" + str(i+1), X[i]))
        if (i+1) < len(X):
            print("+--------------------------------------------------+")
    print("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
    print("| {:^12} | {:>33} |".format("ITERATION", ITER))
    print("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
    print("| {:^12} | {:>33} |".format("MODULE", M[-1]))
    print("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
    print("| {:^12} | {:>33} |".format("ERROR", abs(M[-1]-M[-2])))
    print("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+\n")
