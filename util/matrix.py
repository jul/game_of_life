#!/usr/bin/python
# -*- coding: utf-8 -*-

class matrix:
    matrix=[]
    size_x=None
    size_y=None

    def as_table(self):
        return self.matrix
    
    def __init__(self,size_x,size_y, default=0):
        self.size_y=size_y
        self.size_x=size_x
        self.matrix= [ default ] * size_x*size_y

    def get_rand(self):
        from random import randint 
        return self.matrix[ randint(0,self.size_y * self.size_x -1 ) ]

    def _oneD_offset(self,ix,iy):
        x=self.size_y-1 if -1==ix  else ix
        y=self.size_x-1 if -1==iy  else iy
        x=0 if ix==self.size_x else x
        y=0 if iy==self.size_y else y
        offset = y*self.size_x+x
        return offset
        
    def get(self,x,y):
        """CBP powa"""
        return self.matrix[self._oneD_offset(x,y)]
    
    def nb_neighbour(self,x,y):
        around = [ -1, 0, 1]

        return sum(
            [ self.get(x+dx,y+dy) for dx in around for dy in around 
                if (dx,dy) != (0,0) ]
        )
        
    def set(self,x,y,val):
        self.matrix[self._oneD_offset(x,y)]=val
    
    def copy(self):
        new_matrix= matrix(self.size_x, self.size_x,0)
        new_matrix.matrix = [ x for x in self.matrix ]
        return new_matrix
    def __str__(self):
        to_print="  "
        
        for x in range(0,self.size_x):
            to_print+=" %3d" % x 

        for cursor in range(0,self.size_x*self.size_y):
            cur_val=self.matrix[cursor]
            if (cursor %self.size_x==0):
                to_print+="\n%3d " % (int( cursor  ) / self.size_y)
            if (cursor%(self.size_x)!=0):
                to_print+=" "
            to_print+="%3s" % ( str( cur_val ) if cur_val else "." )
        return to_print
def matrix_check():
#matrice 2x2
    m=matrix(3,2)
    # haut à gauche
    m.set(0,0,1)
    # haut mil
    m.set(1,0,2)
    m.set(2,0,3)
    #mil bas
    m.set(1,1,7)
    print m._oneD_offset(1,1)
    print(m)
    print(u""" 
résultat souhaité : 
  0 1 2
0 1 2 3
1 X 7 X
""")
if __name__ == '__main__':
    matrix_check()
