# Imports:
import numpy as np
import matplotlib.pyplot as pl
from lib import *

# MAIN:
space = np.arange(LOW_LIMIT, HIGH_LIMIT+1, STEPS)
all_points = []
roots = [[],[],[],[]]
roots_str = ""

for i in space:
    if all_points and f(i)*all_points[-1] < 0:
        roots[0].append(i-1)    # Root X Start
        roots[1].append(i)      # Root X End
        roots[2].append(f(i-1)) # Root Y Start
        roots[3].append(f(i))   # Root Y End
    all_points.append(f(i))

for i in range(len(roots[0])):
    roots_str += "Root {}: ( {:^10.3f} and {:^10.3f} )\n".format(i+1, roots[0][i], roots[1][i])

pl.figure(num=1, figsize=(8,8))
pl.get_current_fig_manager().window.wm_geometry("+25+50")
pl.title("Function Graphic")
pl.text(space[0], min(all_points), roots_str[:-1], style='italic', bbox={'facecolor': '#eeeeee', 'alpha': 0.5, 'pad': 10})
pl.ylabel("f(x)")
pl.xlabel("x")
pl.axhline(y=0, color='grey', linewidth = .5)
pl.axvline(x=0, color='grey', linewidth = .5)
pl.plot(space, all_points, color='blue', linewidth = 1)
pl.plot(roots[0], roots[2], 'o', color='orange', linewidth = 1)
pl.plot(roots[1], roots[3], 'o', color='red', linewidth = 1)
pl.grid(linestyle='-', color='#eeeeee')
pl.show()
