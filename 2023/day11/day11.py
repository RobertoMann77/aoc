# input: https://adventofcode.com/2023/day/11#part2

import numpy as np
import copy

M = [i.strip() for i in open('11.in')]

def print_grid(R):
	for s in R:
		l = ''
		for t in s: 
			l += t
		print(l)

# build grid				
for l in range(len(M)):
	M[l] = list(M[l])
M = np.array(M)  

# find dimensions
rows = len(M)
col = len(M[0])


# expand universe
empty_rows = []
for i,row in enumerate(M):
	if '#' not in row:
		empty_rows.append(i)
		
while empty_rows:
	i = empty_rows.pop(-1)
	M = np.insert(M, i, '.', axis=0)
rows = len(M)

empty_col = []
for c in range(col):
	found = 0
	for r in range(rows):
		if M[r][c] == '#': found = 1
	if not found: empty_col.append(c)

while empty_col:
	i = empty_col.pop(-1)
	M = np.insert(M, i, '.', axis=1)
col = len(M[0])


galaxies = []
for r in range(rows):
	for c in range(col):
		if M[r][c] == '#': 
			galaxies.append((r,c))
			M[r][c] = len(galaxies)

# calculate distances
dist = {}
for gal in galaxies:
	for look in galaxies:
		if gal != look and (galaxies.index(look)+1,galaxies.index(gal)+1) not in dist:
			dist[galaxies.index(gal)+1,galaxies.index(look)+1] = abs(gal[0] - look[0]) + abs(gal[1] - look[1])
		


sum1 = 0
for r in dist:
	sum1 += dist[r]

print('Answer 1:',sum1)
