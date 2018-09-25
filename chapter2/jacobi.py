# Imports:
from lib import *

# Function:
def jacobi(A, B, X):
    # Create the submatrices:
    D = np.diag(A) # Creates a vector with the main Diagonal from A matrix.
    R = A - np.diagflat(D) # Subtract the main Diagonal from A matrix.
    # Jacobi's iteration:
    ITER = 0 # Iterations counter.
    M = [np.inf, stopCrit(A, B, X)] # Vector that store all the results vector module.
    while(abs(M[-1] - M[-2]) > ERRO and ITER < MAX_ITER):
        X = (B - np.dot(R, X)) / D
        M.append(stopCrit(A, B, X))
        ITER += 1
        printIteration("GAUSS JACOBI", X, M, ITER)
    # Return the result vector:
    return X

# MAIN:
jacobi(A, B, X)
