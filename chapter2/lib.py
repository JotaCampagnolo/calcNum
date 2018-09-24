# Imports:
import numpy as np
import matplotlib.pyplot as pl
from datetime import datetime

# Constants:
ERRO = 1e-4
MAX_ITER = 1000
A = np.array([ # A Matrix:
    [4, -1, 0, -1, 0, 0, 0, 0, 0],
    [-1, 4, -1, 0, -1, 0, 0, 0, 0],
    [0, -1, 4, 0, 0, -1, 0, 0, 0],
    [-1, 0, 0, 4, -1, 0, -1, 0, 0],
    [0, -1.5, 0, -1.5, 6, -1.5, 0, -1.5, 0],
    [0, 0, -1, 0, -1, 4, 0, 0, -1],
    [0, 0, 0, -1, 0, 0, 4, -1, 0],
    [0, 0, 0, 0, -1, 0, -1, 4, -1],
    [0, 0, 0, 0, 0, -1, 0, -1, 4]
])
B = np.array([50, 40, 90, 10, 0, 50, 140, 130, 180]) # Independent terms.
X = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1]) # Guess vector.

# Function:
def printResult(X, method):
    print("[ ### {:^30} ### ]".format(method + " METHOD"))
    for i in range(len(A[0])):
        print("X" + str(i+1) + " = " + str(X[i]))
