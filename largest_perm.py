# -*- coding: utf-8 -*-
"""
Created on Fri May 27 14:32:47 2016

@author: jingyan
"""

def largest_perm(array,index, N, K):

    i = 0
    while K > 0 and i < N:
        if array[i] == N-i:
            i += 1
        else:
            array[index[N - i]] = array[i];
            index[array[i]] = index[N - i];
            array[i] = N - i;
            index[N - i] = i;
            K -= 1
            i += 1
        
    return array
    
[N,K] = map(int, raw_input().strip().split(' '))
array = map(int, raw_input().strip().split(' '))
index = [0]*(N+1)
for i in range(N):
    index[array[i]] = i
    
print ' '.join(map(str,largest_perm(array, index,N, K) ))

                

