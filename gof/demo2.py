#!/usr/bin/python
import os
from .console import *
from time import sleep
from .matrix import hamming
x,y=16,14
speed=5
### All these works ! 
#grid = matrix(x, y, bytearray(x*y))
#from numpy import array,zeros
#grid = matrix(x, y, zeros(x*y))
#from collections import defaultdict
#grid = matrix(x,y,defaultdict(int,{}))
from .weird_array import Bitmap, SparseArray
grid = matrix(x,y,Bitmap(ALIVE<<x*y))
grid_p = matrix(x,y,Bitmap(ALIVE<<x*y))
#grid = matrix(x,y,SparseArray(set()))

at(grid, 3,9, glider)
at(grid, 2,2, oscillator)
at(grid, 6,5, still)
dirty(grid, 5)

grid_p.matrix._int = grid.matrix._int

grid_p.mutate(5)

grid_f = matrix(x, y, [DEAD]* x*y)
grid_f.pattern = [ " ", "x" , "." , "X" ]
print grid_f
for frame in range(20):
    evolve(grid, 1,"unseeable")
    evolve(grid_p, 1,"unseeable")

    for l in range(grid.matrix._int.bit_length()-1):
        grid_f.matrix[l] = grid.matrix[l] + 2 * grid_p.matrix[l]
    os.system('clear')

    print "\n".join(map(lambda t:"%s\t%s\t%s" %(t),zip(str(grid).split("\n"),str(grid_p).split("\n"),str(grid_f).split("\n"))))
    print "time is %d" % grid.time
    print "pertubation %d"  % (hamming(grid.matrix._int^grid_p.matrix._int))
    sleep(.2)

rstr = lambda s: "".join(reversed([ c for c in s ]))
z=str(bin(grid._code ^ grid_p._code))[2:]
y=str(bin(grid_p._code))[2:]
w=str(bin(grid._code))[2:]
w, y, z = map(rstr,(w, y, z))
#print "diff"
#print "\n".join([ "\t".join([w[x:x+9], y[x:x+9],z[x:x+9].replace("0"," ")]) for x in range(0,max(len(w),len(y),len(z)),9) ])

