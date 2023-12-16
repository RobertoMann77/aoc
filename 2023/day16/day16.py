import numpy as np

def move(posdir):
	N = []				
	pos = posdir[0]
	d = posdir[1]
	
	dc = 0
	dr = 0
	if d == 'e': dc = 1
	if d == 'w': dc = -1
	if d == 'n': dr = -1
	if d == 's': dr = +1
	
	nr = pos[0] + dr
	nc = pos[1] + dc

	if  0 <= nr < rows and 0 <= nc < cols:
		if M[nr][pos[1] + dc] == '.':
			N.append(((nr,nc),d))
		if M[nr][pos[1] + dc] == '|':	
			if d == 's' or d == 'n':
				N.append(((nr,nc),d))
			if d == 'e' or d == 'w':
				N.append(((nr,nc),'n'))
				N.append(((nr,nc),'s'))

		if M[nr][pos[1] + dc] == '-':	
			if d == 'e' or d == 'w': 
				N.append(((nr,nc),d))
			if d == 'n' or d == 's':
				N.append(((nr,nc),'e'))
				N.append(((nr,nc),'w'))

		if M[nr][pos[1] + dc] == '\\':	
			if d == 'e': N.append(((nr,nc),'s'))
			if d == 'w': N.append(((nr,nc),'n'))
			if d == 'n': N.append(((nr,nc),'w'))
			if d == 's': N.append(((nr,nc),'e'))

		if M[nr][pos[1] + dc] == '/':
			if d == 'e': N.append(((nr,nc),'n'))
			if d == 'w': N.append(((nr,nc),'s'))
			if d == 'n': N.append(((nr,nc),'e'))
			if d == 's': N.append(((nr,nc),'w'))	
	return N
		
M = [i.strip() for i in open('t.in')]

for l in range(len(M)):
	M[l] = list(M[l])
rows = len(M)
cols = len(M[0])

record = []

# part 1
hist = [((0, -1), 'e')]				
curr = [((0, -1), 'e')]


# part 2
# from north
'''for col_st in range(cols):
	hist = [((-1, col_st), 's')]				
	curr = [((-1, col_st), 's')]	

# from east
for row_st in range(cols):
	hist = [((row_st, -1), 'e')]				
	curr = [((row_st, -1), 'e')]

# from west
for row_st in range(cols):
	hist = [((row_st, cols), 'w')]				
	curr = [((row_st, cols), 'w')]
'''

# from south
for col_st in range(cols):
	hist = [((rows, col_st), 'n')]				
	curr = [((rows, col_st), 'n')]

	while curr:
		new = (move(curr.pop(0)))

		for n in new:
			if n not in hist:
				curr.append(n)
			hist.append(n)

	tiles = []
	for h in hist:
		if h[0] not in tiles: tiles.append(h[0])
	record.append(len(tiles)-1)
print(max(record))

