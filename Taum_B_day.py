# -*- coding: utf-8 -*-
"""
Created on Fri May 20 17:44:41 2016

@author: jingyan
"""

def B_gift(X, Y, Z, B, W):
    
    if X - Y > Z:
        amount = Y*B + (Y+Z)*W
    elif Y-X > Z:
        amount = X*W + (X+Z)*B
    else:
        amount = X*W + Y*B
    return amount

print B_gift(2,3,4,5,9)      
            
            