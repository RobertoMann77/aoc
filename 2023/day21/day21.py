import numpy as np
import functools

@functools.lru_cache
def look1(pos):
	dr = [-1, 1, 0, 0]
	dc = [ 0, 0, 1,-1]

	rr = pos[0]
	cc = pos[1]
	#print('look:',rr, cc)
	can_go = []
	for n in range(4):
		r = rr + dr[n]
		c = cc + dc[n]
		if M[r%rows][c%cols] == '.' :
			#print('r % rows:',r%rows)
			#print('c % cols:',c%cols)
			can_go.append((rr + dr[n] ,cc + dc[n]))
			#print(rr + dr[n] ,cc + dc[n])
		#print()
	return (can_go)

def look(pos):
		 # n  s  e  w
	dr = [-1, 1, 0, 0]
	dc = [ 0, 0, 1,-1]

	rr = pos[0]
	cc = pos[1]

	can_go = []
	for n in range(4):
		if 0 <= rr + dr[n] < rows and 0 <= cc + dc[n] < cols:
			r = rr + dr[n]
			c = cc + dc[n]
			if M[r][c] == '.' : can_go.append((rr + dr[n], cc + dc[n]))

	return (can_go)


def print_grid(R):
	for s in R:
		l = ''
		for t in s:
			l += t
		j(l)

M = [i.strip() for i in open('t.in')]

for l in range(len(M)):
	M[l] = list(M[l])

M = np.array(M)  

rows = len(M)
cols = len(M[0])

#print(rows,cols)

# part 1 ++++++++++++++++++++++++++++++++++++++++
# find S
for r in range(rows):
	for c in range(cols):
		if M[r][c] == 'S': 
			S = (r,c)
			M[r][c] == '.'

 

for r in range()

j(M)

rows = len(M)
cols = len(M[0])

curr = set()
curr.add(S)
for step in range(100):
	#print(curr)
	new = set()
	for c in curr:
		for t in look1(c):
			new.add(t)
	curr = new
	

# why plus 1 ???
j(len(curr)+1)
