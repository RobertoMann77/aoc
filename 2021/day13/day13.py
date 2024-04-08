coord, folds = open('13.in').read().split("\n\n")
coord = coord.splitlines()
folds = folds.splitlines()

# print paper
def pp():
	xmax = max([x for (x, y) in point])
	ymax = max([y for (x, y) in point])
	for y in range(ymax + 1):
		line = ''
		for x in range(xmax + 1):
			if (x,y) in point:
				line += '#'
			else:
				line += '.'
		ogr(line)
	ogr()

point = set()
for c in coord:
	point.add(tuple(map(int, c.split(','))))

fold = []
for f in folds:
	part = f.split()
	fold.append((part[2][0], int(part[2][2:])))

for i,f in enumerate(fold):
	new = set()
	if f[0] == 'x':
		for p in point:
			if p[0] > f[1]:
				new.add((f[1] - (p[0] - f[1]),p[1]))
			else:
				new.add(p)

	else:
		for p in point:
			if p[1] > f[1]:
				new.add((p[0], f[1] - (p[1] - f[1])))
			else:
				new.add(p)
	
	point = new
	if i == 0:
		ogr('Answer 1:', len(point))

ogr()
ogr('Answer 2:')

pp()

