# Imports:
import numpy as np
import matplotlib.pyplot as pl
from datetime import datetime

# Constants:
ERRO = 1e-6 # Absolute error to stop the program.
MAX_ITER = 1000 # Maximum of iterations to stop the program.
A = np.array([ # A Matrix:
    [4, -1, -1, 0, 0, 0, 0, 0],
    [-1, 4, 0, -1, 0, 0, 0, 0],
    [-1, 0, 4, -1, 0, -1, 0, 0],
    [0, -1.5, -1.5, 6, -1.5, 0, -1.5, 0],
    [0, 0, 0, -1, 4, 0, 0, -1],
    [0, 0, -1, 0, 0, 4, -1, 0],
    [0, 0, 0, -1, 0, -1, 4, -1],
    [0, 0, 0, 0, -1, 0, -1, 4]
])
B = np.array([95, 50, 80, 0, 50, 190, 110, 160]) # Independent terms.
X = np.array([1, 1, 1, 1, 1, 1, 1, 1]) # Guess vector.
M = [np.inf, sum(abs(np.dot(A, X) - B))] # Vector that store all the results vector module.

# Function:
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
