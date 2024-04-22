import numpy as np
import copy

def look(pos):
	dr = [-1, -1, -1,  0,  0,  1,  1,  1]
	dc = [-1,  0,  1, -1,  1, -1,  0,  1]
	count = 0
	for d in range(8):
		if 0 <= pos[0] + dr[d] < rows and 0 <= pos[1] + dc[d] < col:
			r = pos[0] + dr[d]
			c = pos[1] + dc[d]
			if M[r][c] == '#' : count += 1
	return (count)

def print_grid(R):
	for s in R:
		l = ''
		for t in s:
			l += t
		print(l)


# only string lines if noch changes gonna be made			
#M = open('t.in').read().splitlines()

#M = [[c for c in lines] for lines in data]

# list of integers
#M = [list(map(int,line)) for line in open('t.in').read().splitlines()]

#element by element 2-dim array
M = [i.strip() for i in open('t.in')]

for l in range(len(M)):
	M[l] = list(M[l])

M = np.array(M)  

rows = len(M)
col = len(M[0])

print_grid(M)

# grid rand anhängen
for l in range(len(M)): data[l] = '.' + data[l] + '.'
data.insert(0, '.' * len(M[0])),
data.append('.' * len(M[0]))


