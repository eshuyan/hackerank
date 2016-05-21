# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:00:49 2016

@author: jingyan
"""

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in xrange(n):
   topic_t = str(raw_input().strip())
   topic.append(topic_t)
   
def count_interact(a, b):
    count = 0
    for i in range(len(a)):
        if (a[i]=='1' or b[i] =='1'):
            count += 1
    return count

max_topic = 0
max_count = 1
j = 1

for i in range(n-1):
    j = i+1
    while j < n:
        count = count_interact(topic[i], topic[j])
        if count > max_topic:
            max_topic = count
            max_count = 1
        elif count == max_topic:
            max_count += 1
        j += 1
print max_topic  
print max_count 
        
        

        