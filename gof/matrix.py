#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint
"""a 2D accessor for 1 dimensional array, which is backend agnostic.
you need a MutableSequence as a constructor
"""
from .weird_array import Bitmap
def ift(p, vt, vf):
    return lambda val: (ift(*vt)(val) if isinstance(vt, tuple) else vt) \
        if p(val) else (ift(*vf)(val) if isinstance(vf, tuple) else vf)

compile_nbit = lambda nbit: lambda f: sum([int(f(n))<<n for n in range(1<<nbit)])
compile = compile_nbit(9)
hamming = lambda x: sum([ (x>>i)&1 for i in range(x.bit_length()) ])
interpret = lambda code: lambda val: int((1<<(val))&code != 0)
conway_prog= ift(
    lambda x: (x&1) == 1,
        (lambda y:3 <= hamming(y) <= 4, 1, 0),
        (lambda z:hamming(z)       ==3, 1, 0),
)
assert conway_prog(7)
conway_prog2=ift(
    lambda y: hamming(y&~1)==3,
        1,
        (lambda z:(z&1)&(hamming(z&~1)==2), 1, 0
        )
)
conway_prog3=ift(
    lambda x: x&1,
    ( lambda y: hamming(y&~1)==3,
        1,
        ( lambda y: hamming(y&~1)==2,1,0),
    ),
    ( lambda t: hamming(t&~1)==3,1,0),
)
conway_code = compile(conway_prog)
code_arr=Bitmap(conway_code)
for i in range(12,123):
    assert conway_prog(i) == code_arr[i]


assert compile(conway_prog) == compile(conway_prog2)
assert compile(conway_prog) == compile(conway_prog3)
conway = interpret(conway_code)
assert hamming(3) == 2
assert hamming(1) == 1
assert hamming(7) == 3
assert hamming(0b01111) == 4
assert conway(0b00001) == 0
assert conway_code
assert conway(0b01111) == 1
assert conway(0b11111) == 0
assert conway(0b11110) == 0
assert conway(0b11100) == 1
assert conway(0b10101) == 1

class matrix:

    def __init__(self,size_x,size_y, mutable_sequence):
        """construct a view of a dimension x and y on mutable_sequence
        the mutable_sequence must have a dimension compliant with its size
        """
        self.size_y=size_y
        self.size_x=size_x
        self._compute = conway
        self._code = conway_code
        self.matrix= mutable_sequence
        self.pattern = [ ".", "X" ]

    def mutate(self, nb_flip=1):
        for i in range(nb_flip):
            self._code = self._code^(1<<randint(0,self._code.bit_length()-1))
        self._compute=interpret(self._code)

    def get_rand(self):
        from random import randint
        return self.matrix[ randint(0,self.size_y * self.size_x -1 ) ]

    def _oneD_offset(self,ix,iy):
        x=ix%self.size_x
        y=iy%self.size_y
        offset = y*self.size_x+x
        if offset >= self.size_x * self.size_y :
            print("%d(%d), %d(%d) => %d BOOOM"% (x,ix, y,iy, offset))
        return offset

    def get(self,x,y):
        """get item at coordinates x,y"""
        return self.matrix[self._oneD_offset(x,y)]

    def map_neighbor_to_int(self,x,y):
        """mis placed method
        TODO correct it one day"""
        # LSB counting of neighbors (self is bit 0 , north bit 1 .....)
        ordered_neighbors= [    (0,0), 
            (0,1),(-1,1),(-1,0),(-1,-1), (0,-1),(1,-1), (1,0), (1,1)]

        return sum([
            int(not(not(self.get(x+dx,y+dy))))<<i for i,(dx, dy) in enumerate(ordered_neighbors)
        ])
    def compute_state(self,x, y):
        return self._compute(self.map_neighbor_to_int(x,y))

    def set(self,x,y,val):
        """set value val at coordinates x, y"""
        self.matrix[self._oneD_offset(x,y)]=val
    def duplicate(self):
        """return a copy of itself. Maybe copy would be a better name ? """
        copied_matrix = None
        if hasattr(self.matrix, "copy"):
            copied_matrix = self.matrix.copy()
        else:
            copied_matrix = [ x for x in self.matrix ] 
        return matrix(self.size_x, self.size_y,copied_matrix )

    def copy_in(self,other):
        """copy the underlying mutable_sequence in an other matrix"""
        if hasattr(self.matrix, "copy"):
            copied_matrix = self.matrix.copy()
        else:
            copied_matrix = [ x for x in self.matrix ] 
        other.matrix=copied_matrix

    def __str__(self):
        """poor man's amazing graphical effects:)"""
        to_print=" "
        to_print+="'    " * (self.size_y//5 )
        for x in range(self.size_x):
            for y in range(self.size_y):
                if (y==0):
                    to_print+='\n ' if x%5 else "\n-"
                to_print+="%1s" % ( self.pattern[self.get(x,y)] )
        return to_print

def matrix_check():
#matrice 2x2
    m=matrix(3,2, [0]*6)
    # haut à gauche
    m.set(0,0,1)
    # haut mil
    m.set(1,0,2)
    m.set(2,0,3)
    #mil bas
    m.set(1,1,7)
    print(m)
    print(bin(m.map_neighbor_to_int(0,1)))
    print(bin(m.map_neighbor_to_int(0,0)))
    print(u""" 
should be: 
     0  1
 0   X  .
 1   X  X
 2   X  .

""")
if __name__ == '__main__':
    matrix_check()
