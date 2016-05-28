# -*- coding: utf-8 -*-
"""
Created on Fri May 27 13:38:50 2016

@author: jingyan
"""

N = int(raw_input().strip())
d = {}
for i in range(N):
    d[i] = sum(map(int, raw_input().strip().split(' ')))
order = []
for keys in sorted(d, key =d.get):
    order.append(keys+1)
print ' '.join(map(str, order))
    