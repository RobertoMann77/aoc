def count_tiles(p):
	hist = [p]				
	curr = [p]
	tiles = set()
	while curr:
		posdir = curr.pop(0)
		N = []				
		d = posdir[1]
		#	   n  e  s  w
		dc = [ 0, 1, 0,-1]
		dr = [-1, 0, 1, 0]
		
		nr = posdir[0][0] + dr[d]
		nc = posdir[0][1] + dc[d]

		if  0 <= nr < rows and 0 <= nc < cols:
			m = M[nr][nc]
			if m == '.': N.append(((nr,nc),d))

			elif m == '|':	
				if d == 2 or d == 0: N.append(((nr,nc),d))
				elif d == 1 or d == 3:
					N.append(((nr,nc),0))
					N.append(((nr,nc),2))
				
			elif m == '-':	
				if d == 1 or d == 3: N.append(((nr,nc),d))
				elif d == 0 or d == 2:
					N.append(((nr,nc),1))
					N.append(((nr,nc),3))

			elif m == '\\':	N.append(((nr,nc),{1 : 2, 3 : 0, 0 : 3, 2 : 1}[d]))
			elif m == '/': N.append(((nr,nc),{1 : 0, 3 : 2, 0 : 1, 2 : 3}[d]))

			tiles.add((nr,nc))
		
		for n in N:
			if n not in hist:
				curr.append(n)
			hist.append(n)
	return len(tiles)

M = open('16.in').read().splitlines()

rows = len(M)
cols = len(M[0])


print('Answer 1:',count_tiles(((0, -1), 1)))


'''record = []

for c in range(cols):
	record.append(count_tiles(((-1, c), 2)))

for c in range(cols):
	record.append(count_tiles(((rows, c), 0)))

for r in range(cols):
	record.append(count_tiles(((r, -1), 1)))

for r in range(cols):
	record.append(count_tiles(((r, rows), 3)))
	
print('Answer 2:',max(record))'''










