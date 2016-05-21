# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:54:20 2016

@author: jingyan
"""

d1,m1,y1 = raw_input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = raw_input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]

def library_fine(d1,m1,y1,d2,m2,y2):
    if y1 < y2:
        return 0
    elif y1 > y2:
        return 10000
    else:
        if m1 < m2:
            return 0
        elif m1 == m2:
            if d1 <= d2:
                return 0
            else:
                return (d1-d2)*15
        else:
            return 500*(m1-m2)
            
print library_fine(d1,m1,y1,d2,m2,y2)       
    