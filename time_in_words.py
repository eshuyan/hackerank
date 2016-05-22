# -*- coding: utf-8 -*-
"""
Created on Fri May 20 22:48:02 2016

@author: jing
"""
D = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
     'eight', 'nine', 'ten', 'eleven','twelve', 'thriteen','fourteen',
     'fifteen', 'sixteen', 'seventeen','eighteen','nineteen','twenty','twenty one', 
     'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six',
     'twenty seven', 'twenty eight', 'twenty nine']
h = int(raw_input().strip())
m = int(raw_input().strip())
def time_in_words(H, M):

    if M <= 30:
        inter = ' past '
    else:
        inter = ' to '
        M = 60- M 
        H = H + 1
    if M == 1:
        left = 'one minute'
    elif M == 15:
        left = 'quarter'
    elif M == 30:
        left = 'half'
    else:
        left = D[M-1] + ' minutes'
    if M == 0:
        time = D[H-1] + " o' clock"
    else:
        time = left + inter + D[H-1]
    return time
print time_in_words(h, m)