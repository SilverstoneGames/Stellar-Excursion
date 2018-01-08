# -*- coding: utf-8 -*-
"""

Created on Sun Jan  7 19:43:04 2018

@author: Shane
"""

import starLists as SL
import starClass as SC
import random as r

def main():
  
  star = SC.Star(r.choice(SL.starNames))
  
  star.display()
  
  print("And the journey continues...")
  input("Press enter to exit the program...")

main()