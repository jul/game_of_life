Installing
==========

To play with the source, you should use::

    mkdir gof
    cd gof
    virtualenv .
    . bin/activate
    git clone git://github.com/jul/game_of_life.git

    #.... Have Fun using gof interactively ...

    deactivate

Using gof interactively
=======================

python
******

Boring simple::
    
    python -i -mgof



bpython
*******

`bpython`_ is an interactive console for python available normally as a binary
package in your prefered binary distribution, or with pip install.
Its strength lies in the completion, syntax highlihting, 
the ability to save your session either
locally, or snapshot it on bpaste in one keystroke (with its screen output)::

    bpython -i -mgof

ipython
*******

`ipython`_ is pretty much identical to bpython except it is the regular 
interactive session for pylab. So ... it is the tool of choice for 
dynamic plotting. you loose the cool saving part when you want to exchange your
code. 

Using ipython is a bit more complicated once you have typed::
    
    ipython -i

you have to manually type :: 

    >>> from gof.console import *
    >>> intro()
    

.. _bpython: http://pypi.python.org/pypi/bpython
.. _ipython: http://pypi.python.org/pypi/ipython




Forewords
*********

Please read the forewords, and sign with your blood you are fully aware  
this is code is not PEP8 compliant, and not pythonic. It pretty much brings
back the fun of a BASIC like language for playing with game of life. 


For the sake of fun some twists to purity are pretty much acceptable at 
my opinion. It is not a serious project: it is a game. 

.. warning::
   In serious projects : 
    * NEVER import *
    * NEVER **use global variables**
   If you do so, even me will curse your descendants mustache for
   7 generations.





