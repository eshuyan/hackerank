# -*- coding: utf-8 -*-
"""
Created on Thu May 26 11:27:25 2016

@author: jingyan
"""

def sherlock_array(n,array):
    found = False
    if n == 1:
        return 'YES'
    else:
        sum1 = sum(array)
        sum2 = 0
        i = 1
        while not found and i < n:
            sum2 += array[i-1]
             
            if sum2 == (sum1-array[i])/2:
                found = True
            else:
                i += 1
        if found:
            return 'YES'
        else:
            return 'NO'
    
T = int(raw_input().strip())
for test in range(T):
    
    N = int(raw_input().strip())
    c = map(lambda x:int(x),raw_input().strip().split(' ') )
    print sherlock_array(N,c)