# Imports:
from lib import *

# Function:
def simpson1(ll, ul, n):
    # Calculate the h value:
    h = (ul - ll) / n
    # Calculates the integral:
    result = 0
    i = 0
    while i <= n:
        if i == 0 or i == n:
            result += f(ll + i * h)
        elif i % 2 != 0:
            result += 4 * (f(ll + i * h))
        else:
            result += 2 * (f(ll + i * h))
        i += 1
    # Returns the integral value:
    return result * (h / 3)

# MAIN:
while abs(RESULTS[-1] - RESULTS[-2]) > ERRO:
    RESULTS.append(simpson1(LOWER_LIMIT, UPPER_LIMIT, INTERVALS))
    print("Simpson1 (1/3): " + str(INTERVALS) + " : " + str(RESULTS[-1]))
    INTERVALS += 2
