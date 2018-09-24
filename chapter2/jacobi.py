# Imports:
from lib import *

# Function:
def jacobi(A, B, X):
    # Create the submatrices:
    D = np.diag(A) # Creates a vector with the main Diagonal from A matrix.
    R = A - np.diagflat(D) # Subtract the main Diagonal from A matrix.
    # Iterate N times:
    for i in range(MAX_ITER):
        X = (B - np.dot(R, X)) / D
    # Return the result vector:
    return X

# MAIN:
X = jacobi(A, B, X)
printResult(X, "JACOBI")
