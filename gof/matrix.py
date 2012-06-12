#!/usr/bin/python
# -*- coding: utf-8 -*-
"""a 2D accessor for 1 dimensional array, which is backend agnostic.
you need a MutableSequence as a constructor
"""
class matrix:

    def __init__(self,size_x,size_y, mutable_sequence):
        """construct a view of a dimension x and y on mutable_sequence
        the mutable_sequence must have a dimension compliant with its size
        """
        self.size_y=size_y
        self.size_x=size_x
        self.matrix= mutable_sequence

    def get_rand(self):
        from random import randint 
        return self.matrix[ randint(0,self.size_y * self.size_x -1 ) ]

    def _oneD_offset(self,ix,iy):
        
        x=ix%self.size_x
        y=iy%self.size_y
        offset = y*self.size_x+x
        if offset >= self.size_x * self.size_y :
            print "%d(%d), %d(%d) => %d BOOOM"% (x,ix, y,iy, offset)
        return offset
        
    def get(self,x,y):
        """get item at coordinates x,y"""
        return self.matrix[self._oneD_offset(x,y)]
    
    def nb_living_around(self,x,y):
        """mis placed method
        TODO correct it one day"""
        around = [ -1, 0, 1]

        return sum([ 
            int(self.get(x+dx,y+dy)) for dx in around for dy in around 
                if (dx,dy) != (0,0) 
        ])
        
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
        to_print+="'    " * (self.size_y/5 )
        for x in range(self.size_x):
            for y in range(self.size_y):
                if (y==0):
                    to_print+='\n ' if x%5 else "\n-"
                to_print+="%1s" % ( "X" if self.get(x,y) else "." )
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
    print(u""" 
should be: 
     0  1
 0   X  .
 1   X  X
 2   X  .

""")
if __name__ == '__main__':
    matrix_check()
