# -*- coding: utf-8 -*-
"""
Created on Tue May 24 12:50:06 2016

@author: jingyan
"""

def count_sort(array):
    sort = []
    for i in range(100):
        count = array.count(i)
        sort += [i]*count
        
    return sort
    
n = int(raw_input().strip())
array = map(lambda x:int(x),raw_input().strip().split(' ') )
sort = count_sort(array)
print ' '.join(map(lambda x:str(x),sort))
    
        