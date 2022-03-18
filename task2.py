# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 12:35:23 2022

@author: MYLENE ROSE ONG
"""

import math

def middle(arr):
    half = math.floor(len(arr) / 2)
    
    if(len(arr) % 2 !=0):
        return arr[half]
    
    return [arr[half-1], arr[half]]

print(middle([1,2,3,4,5,6,7,8]))