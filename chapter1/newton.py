# Imports:
from lib import *

# MAIN:
table = Table()
ITER = 0
XN = START_GUESS
table.iters.append([ITER, 0, 0, XN, f(XN)])
while(np.sqrt(f(XN)**2) > ERRO):
    XN = XN - (f(XN)/df(XN))
    ITER += 1
    table.iters.append([ITER, 0, 0, XN, f(XN)])

table.show("NEWTON")
