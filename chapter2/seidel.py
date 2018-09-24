# Imports:
from lib import *

# Function:
def seidel(A, B, X):
    # Instanciation of L, D and U matrices:
    L = np.zeros((len(A[0]),len(A[0]))) # Lower from A matrix.
    D = np.zeros((len(A[0]),len(A[0]))) # Main diagonal from A matrix.
    U = np.zeros((len(A[0]),len(A[0]))) # Upper from A matrix.
    for i in range(len(A[0])):
        for j in range(len(A[0])):
            if i == j:
                D[i][j] = A[i][j]
            elif i > j:
                L[i][j] = A[i][j]
            else:
                U[i][j] = A[i][j]
    # Calculating the initial error:
    M = (np.dot(X.T, X))**0.5
    ITER = 0
    # Seidel's iteration:
    while(M > ERRO and ITER < MAX_ITER):
        X = np.dot(np.linalg.inv(L + D), (B - np.dot(U, X)))
        M = (np.dot(X.T, X))**0.5
        ITER += 1
    # Return the result vector:
    return X

# MAIN:
X = seidel(A, B, X)
printResult(X, "SEIDEL")
