# input: https://adventofcode.com/2023/day/11#part2

import numpy as np
import copy

M = [i.strip() for i in open('11.in')]
			
for l in range(len(M)):	M[l] = list(M[l])
M = np.array(M)  

rows = len(M)
col = len(M[0])

empty_rows = []
for i,row in enumerate(M):
	if '#' not in row: empty_rows.append(i)
		
empty_cols = []
for c in range(col):
	found = 0
	for r in range(rows):
		if M[r][c] == '#': found = 1
	if not found: empty_cols.append(c)


galax = []
for r in range(rows):
	for c in range(col):
		if M[r][c] == '#': galax.append((r,c))
			

dist1 = {}
dist2 = {}
for gal in galax:
	for look in galax:
		if gal != look and (look,gal) not in dist1:
			count = 0
			for r in empty_rows: if min(gal[0],look[0]) < r < max(gal[0],look[0]): count += 1
			for c in empty_cols: if min(gal[1],look[1]) < c < max(gal[1],look[1]): count += 1
			dist1[(gal,look)] = abs(gal[0] - look[0]) + abs(gal[1] - look[1]) + count * 999999
			dist2[(gal,look)] = abs(gal[0] - look[0]) + abs(gal[1] - look[1]) + count * 1

sum1 = 0
sum2 = 0
for r in dist1: sum1 += dist1[r]
for r in dist2: sum2 += dist2[r]
print('Answer 1:',sum1)
print('Answer 2:',sum2)

