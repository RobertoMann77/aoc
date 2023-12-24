import copy

def look(pos):
	dr = [-1, 1, 0, 0]
	dc = [ 0, 0,-1, 1]
	go = []
	for n in range(4):
		if 0 <= pos[0] + dr[n] < rows and 0 <= pos[1] + dc[n] < cols:
			r = pos[0] + dr[n]
			c = pos[1] + dc[n]
			#if M[r][c] == '.':		part 1
			if M[r][c] != '#':
				go.append((r,c))
			elif M[r][c] == '>' and dc[n] == 1:
				go.append((r,c))
			elif M[r][c] == 'v' and dr[n] == 1:
				go.append((r,c))
	return go

def print_grid(R,w):
	for inds, s in enumerate(R):
		l = ''
		for indt, t in enumerate(s):
			if (inds,indt) in w:
				l += 'O'
			else:
				l += t
		print(l)

M = [i.strip() for i in open('t.in')]

for l in range(len(M)):
	M[l] = list(M[l])

rows = len(M)
cols = len(M[0])

for c, zeichen in enumerate(M[0]):
	if zeichen == '.':
		S = (0,c)

for c, zeichen in enumerate(M[-1]):
	if zeichen == '.':
		E = (rows - 1,c)
print('start:', S, 'end:', E)
print()
ways = []
ways.append([S])
to_kill = []

erg = []
found = 1
cross = set()
print('crossings:')
for r in range(rows):
	for c in range(cols):
		if M[r][c] != '#' and len(look((r,c))) > 2:
			cross.add((r,c))

print(cross)
print()

while found == 1:
	newways = []
	for w,way in enumerate(ways):
		found = 0
		togo = look(way[-1])

		for t in togo:
			if t in way:
				togo.remove(t)
		if togo:
			new = togo.pop(0)
			if new not in way:
				way.append(new)
				found = 1

		if way[-1] == E:
			erg.append(len(way) - 1)
			print(max(erg))
			to_kill.append(w)

		if found == 0:
			ways.pop(w)
		
		while togo:
			t = togo.pop(0)
			newway = copy.deepcopy(way[:-1])
		
			newway.append(t)
			newways.append(newway)

	for way in newways:
		ways.append(way)

	while to_kill:
		ways.pop(to_kill.pop(-1))

print('Answer 1:', max(erg))



