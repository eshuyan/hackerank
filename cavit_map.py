# -*- coding: utf-8 -*-
"""
Created on Thu May 19 17:18:44 2016

@author: jingyan
"""

import sys


n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
   grid_t = str(raw_input().strip())
   grid.append(grid_t)
   
for i in range(1, n-1):
    for j in range(1, n-1):
        if grid[i][j]> grid[i][j-1] and grid[i][j]> grid[i][j+1] and grid[i][j]> grid[i-1][j] and grid[i][j]> grid[i+1][j]:
            grid[i] = grid[i][:j] + 'X' +grid[i][j+1:]
for i in range(n):
    print grid[i]