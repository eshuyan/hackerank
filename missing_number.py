# -*- coding: utf-8 -*-
"""
Created on Thu May 26 13:32:10 2016

@author: jingyan
"""

def count_list(alist):
    d = {}
    for item in alist:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1
    return d
def missing_numbers(A, B):
    d1 = count_list(A)
    d2 = count_list(B)
    d2_keys = list(set(d2.keys()))
   
    miss_keys = []
    for keys in d2_keys:
        if keys not in d1:
            miss_keys.append(keys)
        elif d2[keys]>d1[keys]:
            miss_keys.append(keys)
    return miss_keys
    
A = [203, 204, 205,206, 207,208,203,204,205,206]
B = [203,204,204,205,206,207,205,208,203,206,205,206,204]
print sorted(missing_numbers(A, B))