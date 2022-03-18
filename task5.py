# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 12:54:49 2022

@author: MYLENE ROSE ONG
"""

class Polygon:
    def __init__(self):
        pass
    def area(self):
        raise NotImplemented
        
from math import sqrt
class Triangle(Polygon):
    def __init__(self, s):
        'constructor that iniatializes the side length of an equilateral triangle'
        Polygon.__init__(self, 3, s)
        
    def area(self):
        'returns triangle area'
        return sqrt(3)*self.s**2/4