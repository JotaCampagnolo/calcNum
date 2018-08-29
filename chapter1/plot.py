# Imports:
from lib import *

# MAIN:
space = np.arange(LOW_LIMIT, HIGH_LIMIT+1, STEPS)
points = []
roots = [[],[],[],[]]
for i in space: # Looking for ROOTS of the equation on defined interval:
    if points and f(i)*points[-1] < 0:
        roots[0].append(i-STEPS)    # Root X Start
        roots[1].append(i)          # Root X End
        roots[2].append(f(i-STEPS)) # Root Y Start
        roots[3].append(f(i))       # Root Y End
    points.append(f(i))

if roots[0]: # If there is at least one root in the interval:
    space = np.arange(roots[0][0]-(2*STEPS), roots[1][-1]+(2*STEPS), STEPS)

points = [] # Fill the points based on the new space:
for i in space:
    points.append(f(i))

rpoints = [[],[]]
for i in range(len(roots[0])):
    rpoints[0].append([roots[0][i],roots[1][i]]) # X
    rpoints[1].append([f(roots[0][i]),f(roots[1][i])]) # Y

roots_str = "" # Fill the graph roots box str:
for i in range(len(roots[0])):
    roots_str += "Root {}: ( {:^10.3f} and {:^10.3f} )\n".format(i+1, roots[0][i], roots[1][i])

pl.figure(num=1, figsize=(8,8))
pl.get_current_fig_manager().window.wm_geometry("+25+50")
pl.title("Function Graph")
pl.text(space[0], min(points), roots_str[:-1], style='italic', bbox={'facecolor': 'orange', 'alpha': 0.5, 'pad': 10})
pl.ylabel("f(x)")
pl.xlabel("x")
pl.axhline(y=0, color='grey', linewidth = .5)
pl.axvline(x=0, color='grey', linewidth = .5)
pl.plot(space, points, color='blue', linewidth = 1)
for i in range(len(rpoints[0])):
    pl.plot(rpoints[0][i], rpoints[1][i], color='orange', linewidth = 2)
pl.plot(roots[0], roots[2], 'o', color='orange', linewidth = 1)
pl.plot(roots[1], roots[3], 'o', color='red', linewidth = 1)
pl.grid(linestyle='-', color='#eeeeee')
pl.savefig('plots/graph.png', bbox_inches='tight')
