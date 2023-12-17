from heapq import heappush, heappop

M = open('t.in').read().splitlines()
visited = set()

R = len(M)
C = len(M[0])

#        hl r  c  dr dc n
curr = [(0, 0, 0, 0, 0, 0)]	# (9, 9) impossible direction for start

while curr:
	hl, r, c, dr, dc, n = heappop(curr)
	
	if r == R-1 and c == C-1:
		print('Answer 1:', hl)
		break
		
	if (r, c, dr, dc, n) in visited: 
		continue

	visited.add((r,c,dr,dc,n))

	if n < 3 and (dr, dc) != (0,0):			#(dr,dc) != 0 because of the start!
		nr = r + dr
		nc = c + dc
		if 0 <= nr < R and 0 <= nc < C:
			heappush(curr, (hl + int(M[nr][nc]), nr, nc, dr, dc, n + 1))
	
	for ndr,ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
		if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
			nr = r + ndr
			nc = c + ndc
			if 0 <= nr < R and 0 <= nc < C:
				heappush(curr, (hl + int(M[nr][nc]), nr, nc, ndr, ndc, 1))




