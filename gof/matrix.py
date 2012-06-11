#!/usr/bin/python
# -*- coding: utf-8 -*-

class matrix:

    def as_table(self):
        return self.matrix
    
    def __init__(self,size_x,size_y, array_of_mutable):
        self.size_y=size_y
        self.size_x=size_x
        self.matrix= array_of_mutable

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
        """CBP powa"""
        return self.matrix[self._oneD_offset(x,y)]
    
    def nb_living_around(self,x,y):
        around = [ -1, 0, 1]

        return sum([ 
            int(self.get(x+dx,y+dy)) for dx in around for dy in around 
                if (dx,dy) != (0,0) 
        ])
        
    def set(self,x,y,val):
        self.matrix[self._oneD_offset(x,y)]=val
    
    def copy(self):
        copied_matrix = None
        if hasattr(self.matrix, "copy"):
            copied_matrix = self.matrix.copy()
        else:
            copied_matrix = [ x for x in self.matrix ] 
        return matrix(self.size_x, self.size_y,copied_matrix )
    
    def __str__(self):
        #to_print="    " 
        #to_print+=" ".join([ "%2d" % x for x in range(self.size_y) ])
        to_print=" "
        to_print+="'    " * (self.size_y/5 )
        for x in range(self.size_x):
            for y in range(self.size_y):
                if (y==0):
                    to_print+='\n ' if x%5 else "\n-"
                    #to_print+="\n%2d " % x
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
