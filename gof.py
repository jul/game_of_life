#!/usr/bin/python
from util.matrix import matrix
import os
from time import sleep

X=10
Y=10
grid = matrix(X,Y, 0)

oscill = False
still = False
glide = True
accel = False
#oscill
if oscill:
    grid.set(2,2,1)
    grid.set(3,2,1)
    grid.set(4,2,1)

#still
if still:
    for i in [ 0,1]:
        for j in [ 0,1]:
            grid.set(7+i,7+j,1)

#glider
if glide:
    grid.set(1,4,1)
    grid.set(2,4,1)
    grid.set(3,4,1)
    grid.set(3,3,1)
    grid.set(2,2,1)


for time in range(100):
    if time %4 == 0 and accel or not accel:
        os.system('clear')
        print grid
        print 'time is  %4d' % time
        sleep(1)
    n_grid = grid.copy()
    for x in range(X):
        for y in range(Y):
            if grid.get(x,y):
                ##alive
                n_grid.set(x,y, int(grid.nb_neighbour(x,y) in [ 2, 3] ))
            else:
                ## dead
                n_grid.set(x,y, int(grid.nb_neighbour(x,y) == 3 ))
    grid=n_grid

