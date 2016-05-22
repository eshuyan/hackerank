# -*- coding: utf-8 -*-
"""
Created on Sat May 21 22:42:20 2016

@author: jing
"""

n = int(raw_input().strip())
D = {}
for case in range(n):
    st = list(raw_input().strip())
    st = set(st)
    for i in st:
        if i not in D:
            D[i] = 1
        else:
            D[i] += 1

count = 0
for i in D:
    if D[i] == n:
        count += 1
print count