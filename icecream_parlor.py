# -*- coding: utf-8 -*-
"""
Created on Thu May 26 11:13:48 2016

@author: jingyan
"""

T = int(raw_input().strip())
for test in range(T):
    M = int(raw_input().strip())
    N = int(raw_input().strip())
    c = map(lambda x:int(x),raw_input().strip().split(' ') )
    answer = []
    for i in range(N-1):
        if c[i] < M:
            for j in range(i+1, N):
                if c[i]+c[j]== M:
                    print str(i+1) +' '+str(j+1)