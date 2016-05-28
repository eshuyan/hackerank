# -*- coding: utf-8 -*-
"""
Created on Fri May 27 10:49:25 2016

@author: jingyan
"""
def greedy_sort(s, N):
    for i in range(N-1):
        for j in range(i+1, N):
            if s[i] > s[j]:
                a = s[i]
                s[i] = s[j]
                s[j] = a
    return s 
s = 'trpqs'
print greedy_sort(list(s), 5)