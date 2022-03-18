# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 12:09:55 2022

@author: MYLENE ROSE ONG
"""

def greet(name, message):
    if(name == 'Juan Dela Cruz'):
        n = name[0:4]
        return message + "" + n
    
print(greet("Juan Dela Cruz", "Good Morning"))
