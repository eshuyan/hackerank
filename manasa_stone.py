# -*- coding: utf-8 -*-
"""
Created on Fri May 20 14:13:40 2016

@author: jingyan
"""

T = int(raw_input().strip())
input_data = []
for i in range(T):
    n = int(raw_input().strip())
    a = int(raw_input().strip())
    b = int(raw_input().strip())
    if a < b:
        input_data.append([n, a, b])
    else:
        input_data.append([n, b, a])
        
def guess_stone(n, a, b):

    stone = ''
    if a == b:
        stone += str(a*(n-1))
    else:
        for i in range(n):
            guess = a*(n-1-i) + b*i
            stone += str(guess)
            stone += ' '
    return stone
        
for data in input_data:
    n,a,b = data[0], data[1],data[2]
    stone = guess_stone(n, a, b)
    print stone
    
    