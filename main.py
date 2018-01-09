# -*- coding: utf-8 -*-
"""

Created on Sun Jan  7 19:43:04 2018

@author: Shane
"""

import starLists as SL
import starClass as SC
import random as r

play = 1

def main():
  
    
    print("Placeholder intro")
  
    target = input("Enter new to travel to a new star: ")
    play = 1
    while play == 1:
        if target.lower() == "new":
            star = SC.Star(r.randint(10000, 9999999999999))
            
            star.display()
      
            target = input("Enter new to travel to a new star: ")
        elif target.lower() == "exit" or target.lower() == "quit":
            input("Thank you for playing Stellar Excursion!")
            play = 0
        else:
            
            star = SC.Star(r.randint(10000, 9999999999999))
            
            star.display()
      
            target = input("Enter new to travel to a new star: ")
            
main()