# -*- coding: utf-8 -*-
"""
StarObject.py
    Contains Star Class
Created on Sun Jan  7 19:44:36 2018

@author: Shane
"""
import numpy as n
import random as r
import StarLists.py as SL
class Star:
    
    def __init__(self):
        self.name = r.choice(SL.starNames)
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
            self.starColour = r.choice("White", "Blue", "Blue-white")
            self.starAppTemp = r.randint(6000, 7500)
            self.starMass = r.uniform(1.5, 1.9)
            self.starLumin = r.randint(4, 10)
        elif self.starType == "G":
            self.starColour = r.choice("White", "Yellow-white", "Yellow")
            self.starAppTemp = r.randint(5000, 6000)
            self.starMass = r.uniform(1.0, 1.2)
            self.starLumin = r.uniform(0.8, 1.4)
        