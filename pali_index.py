# -*- coding: utf-8 -*-
"""
Created on Sat May 21 23:34:13 2016

@author: jing
"""
#last case is timeout at the moment
def palindrome_index(s):
    pali = False
    if s == s[::-1]:
        return -1
    elif s[1:] ==s[1:][::-1]:
        return 0
    elif s[:len(s)-1] == s[:len(s)-1][::-1]:
        return len(s)-1
    else:
        for i in range(1, len(s)-1):
            news = s[:i] +s[i+1:]
            if news == news[::-1]:
                pali = True
                return i
                break
        if not pali:
            return -1
t = int(raw_input().strip())
for case in range(t):
    s = raw_input().strip()
    print palindrome_index(s)
            
            