# -*- coding: utf-8 -*-
"""
Created on Fri May 27 08:59:22 2016

@author: jingyan
"""
def greedy_sort(s, N):
    array = list(s)
    for i in range(N-1):
        for j in range(i+1, N):
            if array[i] > array[j]:
                a = array[i]
                array[i] = array[j]
                array[j] = a
    return ''.join(array) 

def check_columns(s, N):
    sorting = True
    for i in range(N-1):
        j = i + 1
        while j < N and sorting:
            if s[i] > s[j]:
                sorting = False
                break
            else:
                j += 1
    return sorting
     
#N = 4
#s = ['d','c','b','a']
#print  greedy_sort(s, N)              
T = int(raw_input().strip())
for test in range(T):
    array = []
    N = int(raw_input().strip())
    
    for i in range(N):
        s = raw_input().strip()
        array.append(greedy_sort(list(s), N))
        

    sorting = True
    for i in range(N):
        columns = []
        for j in range(N):
            columns.append(array[j][i])
        if not check_columns(columns, N):
            sorting = False
            break
    if sorting:
        print 'YES'
    else:
        print 'NO'


            
    