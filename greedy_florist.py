# -*- coding: utf-8 -*-
"""
Created on Fri May 27 17:56:06 2016

@author: jingyan
"""

N, K = raw_input().split()
N = int(N)
K = int(K)
C = []

numbers = raw_input()

i = 0
for number in numbers.split():
   C.append( int(number) )
   i = i+1

result = 0
print result