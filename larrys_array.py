# -*- coding: utf-8 -*-
"""
Created on Sat May 21 11:25:24 2016

@author: jingyan
"""

T = int(raw_input().strip())

for case in range(T):
    n = int(raw_input().strip())
    numbers = map(lambda x: int(x), raw_input().split(' '))
    i = 0
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if numbers[i] > numbers[j]:
                count += 1
    if count%2 == 0:
        print 'YES'
    else:
        print 'NO'
        
            