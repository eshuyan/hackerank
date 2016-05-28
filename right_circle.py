# -*- coding: utf-8 -*-
"""
Created on Wed May 25 15:36:45 2016

@author: jingyan
"""

[n,k,q] = map(lambda x:int(x),raw_input().strip().split(' ') )
array = map(lambda x:int(x),raw_input().strip().split(' ') )
indice = []
for i in range(q):
    indice.append(int(raw_input().strip()))
for item in indice:
    for i in range(k%n):
        item = (item + n-1)%n
    print array[item]