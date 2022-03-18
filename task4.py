# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 12:48:54 2022

@author: MYLENE ROSE ONG
"""

def fun(a):
    try:
        if a/4:
            b = a / (a - 3)
        print ("value of b =", b)
    except ZeroDivisionError:
        print("value of b =", 0)
        
fun(3)
fun(5)