def count_tiles(start):
	hist = [start]	
	curr = [start]
	tiles = set()
	while curr:	
		(r,c,dr,dc) = curr.pop(0)

		r += dr
		c += dc

		if  0 <= r  < rows and 0 <= c  < cols:
			ch = M[r][c]
			if ch == '.':
				if (r,c,dr,dc) not in hist:
					curr.append((r,c,dr,dc))
					hist.append((r,c,dr,dc))

			elif ch == '|':	
				if dc == 0: 
					if (r,c,dr,dc) not in hist:
						curr.append((r,c,dr,dc))
						hist.append((r,c,dr,dc))

				elif dr == 0:
					if (r,c,-1,0) not in hist:
						curr.append((r,c,-1,0))
						hist.append((r,c,-1,0))

					if (r,c,1,0) not in hist:
						curr.append((r,c,1,0))
						hist.append((r,c,1,0))
				
			elif ch == '-':	
				if dr == 0:
					if (r,c,dr,dc) not in hist:
						curr.append((r,c,dr,dc))
						hist.append((r,c,dr,dc))

				elif dc == 0:
					if (r,c,0,1) not in hist:
						curr.append((r,c,0,1))
						hist.append((r,c,0,1))

					if (r,c,0,-1) not in hist:
						curr.append((r,c,0,-1))
						hist.append((r,c,0,-1))

			elif ch == '\\' and (r,c,dc,dr) not in hist:
				curr.append((r,c,dc,dr))
				hist.append((r,c,dc,dr))

			elif ch == '/' and (r,c,-dc,-dr) not in hist: 
				curr.append((r,c,-dc,-dr))
				hist.append((r,c,-dc,-dr))
			tiles.add((r,c))

	return len(tiles)

M = open('t.in').read().splitlines()
rows = len(M)
cols = len(M[0])

j('Answer 1:',count_tiles((0, -1, 0, 1)))

record = []
for c in range(cols): record.append(count_tiles((-1, c, 1,0)))
for c in range(cols): record.append(count_tiles((rows, c, -1,0)))
for r in range(cols): record.append(count_tiles((r, -1, 0,1)))
for r in range(cols): record.append(count_tiles((r, rows, 0,-1)))
	
j('Answer 2:',max(record))










