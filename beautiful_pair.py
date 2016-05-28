# -*- coding: utf-8 -*-
"""
Created on Fri May 27 13:13:03 2016

@author: jingyan
"""

def string_to_dic(s, N):
    d = {}
    for cha in s:
        if cha not in d:
            d[cha] = 1
        else:
            d[cha] += 1
    return d
N = int(raw_input().strip())
A = raw_input().strip().split()
B = raw_input().strip().split()

count = 0
if sorted(A) == sorted(B):
    count -= 1
else:
    count += 1
d1 = string_to_dic(A, N)
d2 = string_to_dic(B, N)
for keys in d1:
    if keys in d2:
        count += min(d1[keys],d2[keys])
print count 