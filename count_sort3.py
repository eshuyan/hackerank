# -*- coding: utf-8 -*-
"""
Created on Tue May 24 17:40:35 2016

@author: jingyan
"""

def count_sort(array):
    d = {}
    for i in range(100):
        count = array.count(i)
        if i not in d:
            d[i] = count
    return d
    
n = int(raw_input().strip())
array = []
for number in range(n):
    words = raw_input().strip().split(' ')
    array.append(int(words[0]))
d = count_sort(array)
output1 = []
count = 0
for i in range(100):
    count += d[i]
    output1.append(count)
print ' '.join(map(lambda x:str(x),output1))