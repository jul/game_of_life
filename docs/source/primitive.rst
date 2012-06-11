Using the playground
====================

Gof console is leaving you with a depressing empty shell you want to play with. 

Global *evil* variables
***********************

* DEAD or ALIVE : because True and False are too mainstream;
* grid : your playground;
* time : the number of time the game of life was played;
* X,Y the size of the grid;
* pixel : the pattern to draw a pixel;
* oscillator, still, glider : a non exhaustive list of singular patterns in game
* speed : the higher the variable the faster the animation

Global *evil* function
**********************

intro()
-------

A cheat sheet of the console


help
----

Abuse it, this one might be useful:: 

    >>> help grid


bleach(x=Y, Y=Y, atlernative_empty_mutable_array=X*Y*[DEAD])
----------------

Cleans the **evil global variable grid** of any living cells, and set time to 0

if X and/or Y is specified, resize the grid. 

at( x,y ,pattern=pixel, state=ALIVE)
------------------------------

Set at the position x,y the pattern given as an argument in the 
**evil global variable grid**. 


schmutzig(times=1)
------------------

Set one random pattern at a random position in the grid.

play(time=100, show=True)
-------------------------

Make the grid evolve n times according to Conway's Rules. If show is True 
(default value) all states are printed, else you will need to type ::
    >>> print grid

to have a result.




