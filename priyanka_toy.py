# -*- coding: utf-8 -*-
"""
Created on Fri May 27 13:49:12 2016

@author: jingyan
"""

def Priyanka_toy(array, N):
    array = sorted(array)
    
    count = 1
    i = 1
    weight = array[0] + 4
    while i < N:
        if array[i] <= weight:
            i += 1
        else:
            count += 1
            weight = array[i] + 4

    return count
    
N = int(raw_input().strip())
array = map(int, raw_input().strip().split(' '))
print Priyanka_toy(array, N)
        
        