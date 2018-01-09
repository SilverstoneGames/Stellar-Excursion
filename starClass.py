# -*- coding: utf-8 -*-
"""
StarObject.py
    Contains Star Class
Created on Sun Jan  7 19:44:36 2018

@author: Shane
"""
from numpy import random as n
import random as r
import starLists as SL
class Star:
    
    def __init__(self, designation):
        x = r.uniform(0, 1)
        y = r.uniform(0, 1)
        self.isExplored = False
        self.starDesignation = designation
        if y <= 0.000001:
            self.starName = r.choice(SL.starNames)
        else:
            self.starName = "Unnamed"
        if x <= 0.00000001:
            self.starType = "Pulsar"
        elif x > 0.00000001 and x <= 0.000000025:
            self.starType = "Neutron Star"
        else:
            self.starType = r.choice(SL.starTypes)
        self.starTypeNum = r.choice(SL.starTypeNum)
        if self.starType == "O":
            self.starColour = "Blue"
            self.starAppTemp = r.randint(25000, 37500)
            self.starMass = r.randint(40, 80)
            self.starLumin = r.randint(1000000, 1800000)
        elif self.starType == "B":
            self.starColour = "Blue"
            self.starAppTemp = r.randint(11000, 25000)
            self.starMass = r.randint(10, 26)
            self.starLumin = r.randint(15000, 25000)
        elif self.starType == "A":
            self.starColour = "Blue"
            self.starAppTemp = r.randint(7500, 11000)
            self.starMass = r.randint(2, 4)
            self.starLumin = r.randint(60, 80)
        elif self.starType == "F":
            self.starColour = r.choice(SL.typeFcolours)
            self.starAppTemp = r.randint(6000, 7500)
            self.starMass = r.uniform(1.5, 1.9)
            self.starLumin = r.randint(4, 10)
        elif self.starType == "G":
            self.starColour = r.choice(SL.typeGcolours)
            self.starAppTemp = r.randint(5000, 6000)
            self.starMass = r.uniform(1.0, 1.2)
            self.starLumin = r.uniform(0.8, 1.4)
        elif self.starType == "K":
            self.starColour = r.choice(SL.typeKcolours)
            self.starAppTemp = r.randint(3500, 5000)
            self.starMass = r.uniform(0.6, 0.9)
            self.starLumin = r.uniform(0.2, 0.5)
        elif self.starType == "M":
            self.starColour = "Red"
            self.starAppTemp = r.randint(2500, 3500)
            self.starMass = r.uniform(0.6, 0.9)
            self.starLumin = r.uniform(0.2, 0.5) 
            
        
        
    def display(self):
        print("Star Designation:                " + str(self.starDesignation))
        print("Star Name:                       " + self.starName)
        print("Star Class:                      " + str(self.starType) + str(self.starTypeNum))
        print("Colour:                          " + self.starColour)
        print("Approximate Surface Temperature: " + str(self.starAppTemp))
        print("Approximate Mass:                " + str(self.starMass) + " Solar Masses")
        print("Approximate Luminosity:          " + str(self.starLumin) + " times Sol luminosity")
