Using the playground
====================

Gof console is leaving you with a depressing empty shell you want to play with. 

Global *evil* variables
***********************

* DEAD or ALIVE : because True and False are too mainstream;
* grid : your playground;
* pixel : the pattern to draw a pixel;
* oscillator, still, glider : a non exhaustive list of singular patterns in game

Global *evil* function
**********************

intro()
-------

A cheat sheet of the console


help
----
It is a builtin of python interpreter.
Abuse it, this one might be useful:: 

    >>> help grid


bleach(grid, x, y, atlernative_empty_mutable_array=x*y*[DEAD])
----------------

Cleans the grid of any living cells, and set time to 0

if X and Y is specified, resize the grid. 

You can specify an alternative 1D sequence of mutable as a backend. Just
remember to allocate enough space.

at(grid, x,y ,pattern=pixel, state=ALIVE)
------------------------------

Set at the position x,y the pattern given as an argument in the grid


dirty(times=1, list_of_pattern)
------------------

Set one random pattern at a random position in the grid.

evolve(grid, time=100,speed )
-------------------------

Make the grid evolve n times according to Conway's Rules. Default speed
is waiting 1sec after each print. If speed is "unseeable" then, It will
evolve quietly at full speed. 

