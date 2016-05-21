# -*- coding: utf-8 -*-
"""
Created on Sat May 21 10:17:36 2016

@author: jingyan
"""

s = raw_input().strip()
#s = 'ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots'
n = len(s)
import math
row = int(math.floor(math.sqrt(n)))
column = int(math.ceil(math.sqrt(n)))
if row * column < n:
    row = row + 1


matrix = []
i = 1
while i < row:
    matrix.append(s[(i-1)*column : i*column])
    i += 1
matrix.append(s[(i-1)*column : ])

last = len(matrix[-1])

printout = ''
for i in range(last):
    for j in range(row):
        printout += matrix[j][i]
    printout += ' '
for i in range(last, column):
    for j in range(row-1):
        printout += matrix[j][i]
    printout += ' '
print printout
        
    