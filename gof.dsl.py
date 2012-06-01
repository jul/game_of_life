#!/usr/bin/python
from util.matrix import matrix
import os
from time import sleep

X = 22
Y = 60
DEAD = 0
ALIVE = 1

grid = matrix(X, Y, [DEAD]* X*Y)
speed=1.0

oscillator = [(0,0),(0,1),(0,2)]
still = [(0,0),(0,1),(1,0),(1,1)]
glider = [(0,2),(1,2),(2,2),(2,1),(0,0)]

def at(x,y, pattern):
    global grid
    for dx,dy in pattern:
        grid.set(x+dx,y+dy,ALIVE)

at(1,8, glider)
at(2,3, oscillator)
at(6,5, still)

time=0
def play(times=1):
    global grid
    global time
    global speed
    while times:
        os.system('clear')
        times-=1
        time+=1
        print grid
        print "time:<%3d>" % time
        sleep(1.0/speed)
        n_grid = grid.copy()
        for x in range(grid.size_x):
            for y in range(grid.size_y):
                if grid.get(x, y):
                    n_grid.set(x, y, grid.nb_living_around(x, y) in [2, 3])
                else:
                    n_grid.set(x, y, grid.nb_living_around(x, y) == 3)
        grid = n_grid

def reset(x=X,y=Y):
    global grid
    global time
    time = 0
    grid = matrix(x, y, [DEAD]*x*y)
