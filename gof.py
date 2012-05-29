#!/usr/bin/python
from util.matrix import matrix
import os
from time import sleep

X = 12
Y = 8
grid = matrix(X, Y, DEAD)
ALIVE = 1
DEAD = 0

oscill = False
still = False
glide = True
accel = False
#oscill
if oscill:
    grid.set(2, 2, ALIVE)
    grid.set(3, 2, ALIVE)
    grid.set(4, 2, ALIVE)

#still
if still:
    for i in [0, 1]:
        for j in [0, 1]:
            grid.set(7 + i, 7 + j, ALIVE)

#glider
if glide:
    grid.set(1, 4, ALIVE)
    grid.set(2, 4, ALIVE)
    grid.set(3, 4, ALIVE)
    grid.set(3, 3, ALIVE)
    grid.set(2, 2, ALIVE)


for time in range(100):
    if not time % 4 and accel or not accel:
        os.system('clear')
        print grid
        print 'time is  %4d' % time
        sleep(1)
    n_grid = grid.copy()
    for x in range(X):
        for y in range(Y):
            if n_grid.get(x, y) is ALIVE:
                n_grid.set(x, y, int(grid.nb_neighbour(x, y) in [2, 3]))
            else:
                n_grid.set(x, y, int(grid.nb_neighbour(x, y) == 3))
    grid = n_grid
