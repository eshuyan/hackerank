# -*- coding: utf-8 -*-
"""
Created on Sun May 22 10:32:11 2016

@author: jing
"""
def two_strings(s1,s2):
    s1 = list(set(list(s1)))
    s2 = list(set(list(s2)))
    i = 0
    found = False
    while not found and i <len(s1):
        if s1[i] in s2:
            found = True
            break
        else:
            i += 1
    if found:
        return 'YES'
    else:
        return 'NO'
            
            
t = int(raw_input().strip())
for case in range(t):
    s1 = raw_input().strip()
    s2 = raw_input().strip()
    print two_strings(s1,s2)
    