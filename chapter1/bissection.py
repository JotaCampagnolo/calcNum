# Imports:
from lib import *

# MAIN:
table = Table()
ITER = 0
A = START_A
B = START_B
XN = (A+B)/2
table.iters.append([ITER, A, B, XN, f(XN)])
while(np.sqrt(f(XN)**2) > ERRO):
    if f(XN)*f(A) < 0:
        B = XN
    else:
        A = XN
    XN = (A+B)/2
    ITER += 1
    table.iters.append([ITER, A, B, XN, f(XN)])

table.show("BISSECTION")
