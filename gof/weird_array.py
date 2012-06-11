#!/usr/bin/python
# -*- coding: utf-8 -*-

class SparseArray(object):
    def __init__(self,_set):
        self._set = _set

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
    def __init__(self,_int):
        self._int = int(_int)

    def __setitem__(self,offset, val):
        if val:
            self._int |= 1<<offset
        else:
            self._int &= ~(1<<offset)

    def __getitem__(self,offset):
        return int(bool(self._int & 1<<offset))

    def copy(self):
        return Bitmap(self._int)
