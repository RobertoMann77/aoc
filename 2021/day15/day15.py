import numpy as np
data = [i.strip() for i in open('t.in')]

def look(pos):
	togo = []
	dr = [ 0,  0, -1,  1]
	dc = [-1,  1,  0,  0]
	for n in range(4):
		r = pos[0] + dr[n]
		c = pos[1] + dc[n]
		if 0 <= r < len(M) and 0 <= c < len(M[0]):
			togo.append((r,c))

M = []
visited = {(0,0) : 0}
for row in data:
	r = []
	for char in row:
		r.append(int(char))
	M.append(r)

M = np.array(M)
print(M)

	   #rl  r  c
curr = [(0, 0, 0)]

visited = set()
