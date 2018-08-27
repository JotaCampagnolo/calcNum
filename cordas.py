# Imports:
from lib import *

# MAIN:
table = Table()
ITER = 0
A = START_A
B = START_B
XN = ((A * f(B)) - (B * f(A))) / (f(B) - f(A))
table.iters.append([ITER, A, B, XN, f(XN)])
while(np.sqrt(f(XN)**2) > ERRO):
    if f(XN)*f(A) > 0:
        A = XN
    else:
        B = XN
    XN = ((A * f(B)) - (B * f(A))) / (f(B) - f(A))
    ITER += 1
    table.iters.append([ITER, A, B, XN, f(XN)])

table.show("CORDAS")
