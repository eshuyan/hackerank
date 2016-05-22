# -*- coding: utf-8 -*-
"""
Created on Fri May 20 21:33:16 2016

@author: jing
"""

def kaprekar(number):
        n = len(str(number))
        square = number * number
        square = str(square)
        n2 = len(square)
        if n2 == n:
            l = int(square)
            r = 0
            if number == (l+r):
                return True
            else:
                return False
        else:
            l1 =  int(square[:n])
            r1 =  int(square[n:])
            l2, r2 = 0, '0'
            if n > 1:
                l2 =  int(square[:(n-1)])
                r2 = square[n-1:]
       
            if number == (l1+r1) and r1!= 0 or (number == (l2 + int(r2))  and len(r2) <= n):
                return True
            else:
                return False

kaprekar_list = ''

p = int(raw_input())
q = int(raw_input())


for i in range(p, q+1):
    if kaprekar(i):
        kaprekar_list += str(i)
        kaprekar_list += ' '
print kaprekar_list
        