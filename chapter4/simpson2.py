# Imports:
from lib import *

# Function:
def simpson2(ll, ul, n):
    # Calculate the h value:
    h = (ul - ll) / n
    # Calculates the integral:
    result = f(ll) + f(ul)
    i = 0
    for i in range(1, INTERVALS):
        if i % 3 == 0:
            result += 2 * f(ll + i * h)
        else:
            result += 3 * f(ll + i * h)
    # Returns the integral value:
    return result * ((3 * h) / 8)

# MAIN:
print("%.6f"% simpson2(LOWER_LIMIT, UPPER_LIMIT, INTERVALS))
