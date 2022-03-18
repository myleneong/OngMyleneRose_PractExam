# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 12:38:08 2022

@author: MYLENE ROSE ONG
"""

def get_perimeter(perimeter):
    # hexagon perimeter formula p = 6a
    return list(map((lambda a: 6*a), perimeter))

hexagons = [4,6,2,9,5]

print(get_perimeter(hexagons))