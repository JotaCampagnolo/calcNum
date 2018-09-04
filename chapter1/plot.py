# Imports:
from lib import *

# MAIN:
time = datetime.now()
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
    space = np.arange(roots[0][0]-(1*STEPS), roots[1][-1]+(2*STEPS), STEPS)

points = [] # Fill the points based on the new space:
for i in space:
    points.append(f(i))

rpoints = [[],[]]
for i in range(len(roots[0])):
    rpoints[0].append([roots[0][i],roots[1][i]]) # X
    rpoints[1].append([f(roots[0][i]),f(roots[1][i])]) # Y

roots_str = "" # Fill the graph roots box str:
for i in range(len(roots[0])):
    roots_str += "Root {}: ( {:^10.5f} and {:^10.5f} )\n".format(i+1, roots[0][i], roots[1][i])

# Creates the plot figure:
figure = pl.figure(figsize=(12, 8))
# Figure: plot1:
plot1 = figure.add_subplot(121)
plot1.set_title('Function Graph')
plot1.set_ylabel("f(x)")
plot1.set_xlabel("x")
plot1.axhline(y=0, color='grey', linewidth = .5)
plot1.axvline(x=0, color='grey', linewidth = .5)
plot1.grid(linestyle='-', color='#eeeeee')
plot1.plot(space, points, color='#4484ff', linewidth = 1)
for i in range(len(rpoints[0])):
    plot1.plot(rpoints[0][i], rpoints[1][i], color='#36cc98', linewidth = 3)
plot1.plot(roots[0], roots[2], 'o', color='#36cc98', linewidth = 1)
plot1.plot(roots[1], roots[3], 'o', color='#1b664c', linewidth = 1)
# Figure: plot2:
plot2 = figure.add_subplot(122)
plot2.set_title('Function Roots')
plot2.axis('off')
plot2.text(0.16, 0.03, roots_str[:-1], style='italic', bbox={'facecolor': '#44ffbf', 'alpha': 0.5, 'pad': 10})
# Saves the figure:
figure.savefig('plots/graph_' + str(time.year) + str(time.month).zfill(2) + str(time.day).zfill(2) + '_' + str(time.hour).zfill(2) + str(time.minute).zfill(2) + str(time.second).zfill(2) + '.png', bbox_inches='tight')
