# -*- coding: utf-8 -*-
"""
Created on Wed May 25 14:29:00 2016

@author: jingyan
"""

def find_difference(array):
    array.sort()
    diff = []
    for i in range(len(array)-1):
        diff.append(abs(array[i+1]-array[i]))
    low = min(diff)
    pairs = []
    for i in range(len(diff)):
        if diff[i] == low:
            pairs.append(array[i])
            pairs.append(array[i+1])
    return pairs
n = int(raw_input().strip())
array = map(lambda x:int(x),raw_input().strip().split(' ') )
pairs = find_difference(array)
print ' '.join(map(lambda x:str(x),pairs))  