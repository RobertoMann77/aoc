# input: https://adventofcode.com/2023/day/14

import numpy as np

def pr_gr(R):
	for s in R:
		l = ''
		for t in s:
			l += t
		print(l)

def find_rr(m):
	rr = []
	for r in range(rows):
		for c in range(cols):
			if m[r][c] == 'O': rr.append((r,c))
	return(rr)

M = [i.strip() for i in open('14.in')]

for l in range(len(M)): M[l] = list(M[l])

M = np.array(M) 
rows = len(M)
cols = len(M[0])

def fall(m):
	round_rocks = find_rr(m)
	while round_rocks:
		to_move = round_rocks.pop(0)
		n_pos = to_move[0]
		while m[n_pos -1][to_move[1]] == '.' and n_pos != 0:
			n_pos -= 1
		m[to_move[0]][to_move[1]] = '.'
		m[n_pos][to_move[1]] = 'O'
	return m

def rotate(m):
	for j in range(3):
		m = [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]
	return m

found = 0
history = {}
summen = []
step = 1
#while found == 0:
for t in range(300):
	for t in range(4):
		M = fall(M)	
		M = rotate(M)

	round_rocks = find_rr(M)
	sum1 = 0
	for rr in round_rocks: sum1 += rows - rr[0]
	
	if sum1 not in history:
		history[sum1] = []
	if step >100:
		history[sum1].append((step,sum1,M))
	summen.append(sum1)
	#print(step,sum1)
	step += 1

z = 100311
for r in range(len(history[z])-1):
	for s in range(r+1,len(history[z])):
		if np.array_equal(history[z][r][2],history[z][s][2]):
			print()
			print('found:',history[z][r][0],history[z][s][0])
			d = history[z][s][0]-history[z][r][0]
			marker = history[z][r][0]
			print('d:',d)
			print('look at:',(1000000000 - history[z][r][0])%d)
			pr_gr(history[z][r][2])
			print()
			pr_gr(history[z][s][2])


print('Answer 2:',summen[marker+(1000000000 - marker)%d])
#print((1000000000 - 141)%52)















