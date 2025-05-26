# -*- coding: utf-8 -*-
"""
Created on Thu May 22 15:26:37 2025

@author: rocha
"""

# Write the class according to the specifications below:

class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        self._radius = radius
    def get_radius(self):
        """ Returns the radius of self """
        return self._radius
    def set_radius(self, radius):
        """ radius is a number
        Changes the radius of self to radius """
        self._radius = radius
    def get_area(self):
        """ Returns the area of self using pi = 3.14 """
        from math import pi
        area = pi*(self._radius**2)
        return area
    def equal(self, c):
        """ c is a Circle object
        Returns True if self and c have the same radius value """
        return self._radius == c._radius
    def bigger(self, c):
        """ c is a Circle object
        Returns self or c, the Circle object with the bigger radius """
        if self._radius > c._radius:
            return self
        else:
            return c