#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 18:02:17 2025

@author: rocha
"""

class Container(object):
    """
    A container object is a list and can store elements of any type
    """
    def __init__(self):
        """
        Initializes an empty list
        """
        self._my_list = []
    def size(self):
        """
        Returns the length of the container list
        """
        return len(self._my_list)
    def add(self, elem):
        """
        Adds the elem to one end of the container list, keeping the end
        you add to consistent. Does not return anything
        """
        self._my_list.append(elem)
    
class Queue(Container):
    """
    A subclass of Container. Has an additional method to remove elements.
    """
    def __init__(self):
        Container.__init__(self)
    def remove(self):
        """
        The oldest element in the container list is removed
        Returns the element removed or None if the stack contains no elements
        """
        try:
            return self._my_list.pop(0)
        except IndexError: # if _myList is empty
            return None