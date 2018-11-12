# Imports:
from lib import *

# Function:
def trapeze(ll, ul, n):
    # Calculate the h value:
    h = (ul - ll) / n
    # Calculates the integral:
    result = f(ll) + f(ul)
    i = 0
    for i in range(1, INTERVALS):
        result += 2 * f(ll + i * h)
    # Returns the integral value:
    return result * (h / 2)

# MAIN:
print("Trapeze (1/2): " + str(trapeze(LOWER_LIMIT, UPPER_LIMIT, INTERVALS)))
