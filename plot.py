# Imports:
import numpy as np
import matplotlib.pyplot as pl
from lib import *

# MAIN:
points = []
rxs = []
rxe = []
rys = []
rye = []
for i in range(LOW_LIMIT, HIGH_LIMIT+1):
    if points and f(i)*points[-1] < 0:
        rxs.append(i-1)
        rxe.append(i)
        rys.append(f(i-1))
        rye.append(f(i))
    points.append(f(i))

pl.figure(num=1, figsize=(8,8))
pl.get_current_fig_manager().window.wm_geometry("+25+50")
pl.title("Function Graphic")
pl.ylabel("f(x)")
pl.xlabel("x")
pl.axhline(y=0, color='grey', linewidth = .5)
pl.axvline(x=0, color='grey', linewidth = .5)
pl.plot(range(LOW_LIMIT, HIGH_LIMIT+1), points, color='blue', linewidth = 1)
pl.plot(rxs, rys, 'x', color='orange', linewidth = 1)
pl.plot(rxe, rye, 'x', color='red', linewidth = 1)
pl.grid(linestyle='-', color='#eeeeee')
pl.show()
