# -*- coding: utf-8 -*-
"""
Created on Sat May 21 22:26:56 2016

@author: jing
"""

t = int(raw_input().strip())
for case in xrange(t):
    s = raw_input().strip()
    r = s[::-1]
    count = 0
    for i in range(len(s)):
        count += abs(ord(s[i])-ord(r[i]))
    print count/2
        
    