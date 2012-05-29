#!/usr/bin/python
from util.matrix import matrix
import os
from time import sleep

X=10
Y=10
grid = matrix(X,Y, 0)

oscill = False
still = False
glide = False
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
grid.set(1,6,1)
grid.set(2,6,1)
grid.set(3,6,1)
grid.set(3,5,1)
grid.set(2,4,1)


for time in range(20):
    os.system('clear')
    print grid
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
    sleep(1)

