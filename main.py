# -*- coding: utf-8 -*-
"""

Created on Sun Jan  7 19:43:04 2018

@author: Shane
"""

import starLists.py as SL
import starClass.py as SC
import random as r

def main():
  
  star = SL.Star(r.choice(SL.starNames))
  
  star.display()
  
  print("Press enter to exit...")
