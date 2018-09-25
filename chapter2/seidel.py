# Imports:
from lib import *

# Function:
def seidel(A, B, X):
    # Instanciation of L, D and U matrices:
    L = np.tril(A, k=-1) # Lower from A matrix.
    D = np.diag(np.diag(A)) # Main diagonal from A matrix.
    U = np.triu(A, k=1) # Upper from A matrix.
    # Seidel's iteration:
    ITER = 0 # Iterations counter.
    while(abs(M[-1] - M[-2]) > ERRO and ITER < MAX_ITER):
        X = np.dot(np.linalg.inv(L + D), (B - np.dot(U, X)))
        M.append(sum(abs(X)))
        ITER += 1
        printIteration("GAUSS SEIDEL", X, M, ITER)
    # Return the result vector:
    return X

# MAIN:
seidel(A, B, X)
