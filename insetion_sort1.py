# -*- coding: utf-8 -*-
"""
Created on Sun May 22 13:09:30 2016

@author: jing
"""
def print_array(array):
    s = ''
    for i in array:
        s += str(i)
        s += ' '
    return s

n = int(raw_input().strip()) 
array = map(lambda x: int(x), raw_input().strip().split(' ')) 
number = array[-1]
for i in range(n-2, -1, -1):
    if number < array[i]:
        array[i+1] = array[i]

        print print_array(array)
    else:
        array[i+1] = number
        print print_array(array)
        break
    if i == 0 and number < array[0]:
        array[0] = number 
        print print_array(array)
      
   # print print_array(array) 
    