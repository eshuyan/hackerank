# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:04:08 2016

@author: jing
"""
#even slower comparing to orginal code
from collections import Counter
def check_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
def calculate_anagram(s):
    n = len(s)
    count = 0
    for i in range(n-1):#first pointer
        for k in range(1, n-i):#len of the substring
            j = i+1 #second pointer
            while j+k <= n:
                if check_anagram(s[i:i+k], s[j:j+k]):
                    count += 1
                j += 1
    return count
t = int(raw_input().strip())
for case in range(t):
    s = raw_input().strip()
    print  calculate_anagram(s)      

#s1 = 'abab'
#s2 = 'abba'
#print check_anagram(s1, s2)