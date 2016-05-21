# -*- coding: utf-8 -*-
"""
Created on Sat May 21 11:37:30 2016

@author: jingyan
"""
##brutal force and timeout for 6,7,8,9
T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    q = map(int,raw_input().strip().split(' '))
    count = 0
    chaotic = False

    for i in range(n):
        print chaotic
        if q[i] -3> i:
            chaotic = True
            break
    if not chaotic:
        for i in range(n-1):
            for j in range(i, n):
                if q[i] >q[j]:
                    count += 1   
        print count
    else:
        print 'Too chaotic'
            
    
        
            
    