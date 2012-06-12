#!/usr/bin/python
# -*- coding: utf-8 -*-
"""facade design pattern to make : set() and int look like a mutable sequence
of 0 and 1"""

class SparseArray(object):
    """a mtuable sequence facade for set()"""
    def __init__(self,_set=None):
        self._set = _set if _set else {0}^{0}

    def __setitem__(self,offset, val):
        if val:
            self._set.add(offset)
        else:
            self._set.discard(offset)

    def __getitem__(self,offset):
        return int(bool(offset in self._set))

    def copy(self):
        return SparseArray(self._set.copy())


class Bitmap(object):
    """bit array view on an int"""
    def __init__(self,_int=None):
        if not _int:
            raise Exception("Please provide a non null int")

        self._int = _int

    def __setitem__(self,offset, val):
        if val:
            self._int |= 1<<offset
        else:
            self._int &= ~(1<<offset)

    def __getitem__(self,offset):
        return int(bool(self._int & 1<<offset))

    def copy(self):
        return Bitmap(self._int)
