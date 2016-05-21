# -*- coding: utf-8 -*-
"""
Created on Thu May 19 17:18:45 2016

@author: jingyan
"""

[n, k] = map(lambda x: int(x), raw_input().split(' '))
problems = map(lambda x: int(x), raw_input().split(' '))


pages = 0
pro_per_page = []
for i in range(n):
    p = problems[i]/ k
    if problems[i]% k == 0:
        
        pages += p
        for j in range(p):    
            pro_per_page.append(range(1, problems[i] + 1)[j*k :(j+1)*k])
    else:
         
        pages += (p +1)
        for j in range(p):    
            pro_per_page.append(range(1, problems[i] + 1)[j*k :(j+1)*k])
        pro_per_page.append(range(1, problems[i] + 1)[p*k:])

count = 0
for i in range(1, pages+1):
    if i in pro_per_page[i-1]:
        count += 1
print count
    
    
    
        