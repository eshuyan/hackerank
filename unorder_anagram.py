# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:04:08 2016

@author: jing
"""
#Brutal force, could not pass test03/05 due to timeout
def calculate_char(s):
    D = {}
    for i in s:
        if i not in D:
            D[i] = 1
        else:
            D[i] += 1
    return D
    
def check_anagram(s1, s2):
    set1 = set(list(s1))
    set2 = set(list(s2))
    if not set1.difference(set2):
        d1 = calculate_char(s1)
        d2 = calculate_char(s2)
        i = 0
        for char in set1:
            if d1[char] == d2[char]:
                i += 1
            else:
                return False
                break
        if i == len(set1):
            return True
    else:
        return False
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