import numpy as np

def move(posdir):
	N = []				
	d = posdir[1]
	
	dc = 0
	dr = 0
	
	if d == 'e': dc = 1
	elif d == 'w': dc = -1
	elif d == 'n': dr = -1
	elif d == 's': dr = +1
	
	nr = posdir[0][0] + dr
	nc = posdir[0][1] + dc

	if  0 <= nr < rows and 0 <= nc < cols:
		m = M[nr][nc]
		if m == '.':
			nd = d
		elif m == '|':	
			if d == 's' or d == 'n':
				nd = d
			elif d == 'e' or d == 'w':
				N.append(((nr,nc),'n'))
				nd = 's'

		elif m == '-':	
			if d == 'e' or d == 'w': 
				nd = d
			elif d == 'n' or d == 's':
				N.append(((nr,nc),'e'))
				nd = 'w'

		elif m == '\\':	
			if d == 'e': nd = 's'
			elif d == 'w': nd = 'n'
			elif d == 'n': nd = 'w'
			elif d == 's': nd = 'e'
			N.append(((nr,nc),nd))

		elif m == '/':
			if d == 'e': nd = 'n'
			elif d == 'w': nd = 's'
			elif d == 'n': nd = 'e'
			elif d == 's': nd = 'w'	
		N.append(((nr,nc),nd))
	return N
		
M = [i.strip() for i in open('t.in')]

for l in range(len(M)):
	M[l] = list(M[l])
rows = len(M)
cols = len(M[0])

record = []

# part 1
#hist = [((0, -1), 'e')]				
#curr = [((0, -1), 'e')]


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
	curr = [((rows, col_st), 'n')]
	hist = [((rows, col_st), 'n')]

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

