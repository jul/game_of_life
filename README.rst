complete doc: http://gof.readthedocs.org/en/latest/
source : https://github.com/jul/game_of_life
ticketing : https://github.com/jul/game_of_life/issues


game_of_life
============

http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

Motivation
==========

http://beauty-of-imagination.blogspot.fr/2012/05/teachers-stop-misleading-your-students.html

just for fun

Direct in the fun
=================

Quick install
*************
First install the package either from github
    git clone git://github.com/jul/game_of_life.git

And do what you have to do :)

Or
    pip install gof

I made a package to write less docs.

To dive directly in the core of the topic 
    python -i -mgof.demo

You'll have a *pseudo* animation (could work on windows, but I am lazy), of a 
cellular automata. But this is not fun, you have to manipulate to really have 
fun.

Since you use *python -i* at the end of the demo you are left with an
interactive session

*New*: 
    ipython -i -mgof.demo2

A console for seeing what happens if you change 5 bits of the turing machine 
describing a conway rule. 


Quick tour
**********

Let's use all the functions: 

First seeing is believing
    >>> print grid
     '    '    
    -..............
     ..............
     ..............
     ..............
     ..............
    -...X..........
     ...X..........
     ...X..........
     ..............
     XX...XXX.....X
    -..............
     ...X..........
     ...X..........
     ...X..........
     ..............
    -..............

So I may have overloaded __str__ so that you have a matrix. 
If you want to know more about the grid object

    >>> help(grid)

It does not tells you : grid.size_x, grid._size_y are attributes  where
the dimension of the matrix are stored.

Now, you want to clean the matrix, to play

    >>> bleach(grid, 20,40)
    >>> print grid

This should show you a nice empty grid.

Before you play the game of life, you want to draw patterns on your grid. 
(The one I defined are not exhautive, you can draw your own.)
Let's add a glider, an oscillator, and a fixed block

    >>> at(grid, 10,20, glider)
    >>> at(grid, 5,5, oscillator)
    >>> at(grid, 15,25, still)

and see the result  
    >>> print grid
     '    '    '    '    '    '    '    '    
    -........................................
     ........................................
     ........................................
     ........................................
     ........................................
    -.....XXX................................
     ........................................
     ........................................
     ........................................
     ........................................
    -....................X.X.................
     ......................X.................
     .....................XX.................
     ........................................
     ........................................
    -.........................XX.............
     .........................XX.............
     ........................................
     ........................................
     ........................................
let's see how it evolves 
    >>> evolve(grid, 10, 5)

not stable yet? Let's play 10 more iterations, slower
    >>> evole(grid, 10, 2)

Boring, want more surprises?
    >>> bleach(grid, 20,40, Bitmap(1<<20*40))
    >>> dirty(grid, 10)
It adds pattern randomly on the grid

Then, just sit back and play 200 iterations at 5 times the slow speed
    >>> evolve(grid, 200,5)

You may have stable result around 100-200 iterations. 
What it the Bitmap by the way ? 

Well, then fun part is matrix is just a view on anything that looks like 
a mutable sequence, and an int is a mutable sequence of bits, no ? 

When (and only when) using Bitmap you can make
    >>> print "{0:b}".format(grid.matrix._int)
    100000000110000000000000000000000000011100000000000000000101100000100000000000011000001000000000001000000010000000000010000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000001100000000000000000100000000000000000001010000001110000000000000000000000000111000000010000010001000000000100000100010100000001000001000100000000000001100001000000000001111000000000000000000000000000000000000000000000000000000001000000000000000000010000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000110000000000000000001100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000110000000000

The quickstart is other :) 

Have fun

