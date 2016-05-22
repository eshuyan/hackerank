# -*- coding: utf-8 -*-
"""
Created on Sat May 21 23:02:15 2016

@author: jing
"""
def calculate_char(s):
    D = {}
    for i in s:
        if i not in D:
            D[i] = 1
        else:
            D[i] += 1
    return D
def make_anagram(s):
    count = -1
    if len(s)%2 == 1:
        return count
    else:
        char = set(list(s))
        s1 = s[:len(s)/2]
        s2 = s[len(s)/2:]
        D1 = calculate_char(s1)
        D2 = calculate_char(s2)
        count = 0
        for ch in char:
            if ch in D1 and ch in D2:
                count += abs(D1[ch]-D2[ch])
            elif ch in D1 and ch not in D2:
                count += D1[ch]
            else:
                count += D2[ch]
        return count/2
t = int(raw_input().strip())
for case in range(t):
    s = raw_input().strip()
    print make_anagram(s)
        
            
        