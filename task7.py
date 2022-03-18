# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:05:50 2022

@author: MYLENE ROSE ONG
"""

class Vehicle:
   
    def __init__(self, size, color, weight, travel):
        self.size = size
        self.color = color
        self.weight = weight
        self.travel = travel
    

    
    def displayVehicle(self):
        print ("Size:  ", self.size, " Color: ", self.color, " Weight: ", 
               self.weight, " Travel:", self.travel)
    
    def distanceTravel(self):
        self.travel = 7890
        print('Distance travel of this car is: ', self.travel)
        
class Car(Vehicle):
        
    def __init__(self, model, provideComfort, travel):
        self.model = model
        self.provideComfort = provideComfort
        
    def display(self):
        print(distanceTravel)
        
c1 = Vehicle('fourseater','silver',1238, 7890)

print(c1.displayVehicle())