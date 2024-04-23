import numpy as np
data = [i.strip() for i in open('t.in')]

xmax = 0
ymax = 0
zmax = 0

bricks = []
for line in data:
	A, B = line.split('~')
	ax, ay, az = A.split(',')
	bx, by, bz = B.split(',')
	ax = int(ax)
	ay = int(ay)
	az = int(az)

	bx = int(bx)
	by = int(by)
	bz = int(bz)

	if max(ax, bx) > xmax: xmax = max(ax, bx)
	if max(ay, by) > ymax: ymax = max(ay, by)
	if max(az, bz) > zmax: zmax = max(az, bz)

M = []
for x in range(xmax + 1):
	s = []
	for y in range(ymax + 1):
		t = []
		for z in range(zmax + 1):
			t.append('.')
		s.append(t)
	M.append(s)

M = np.array(M)

bricks = []

for l,line in enumerate(data):
	ax, ay, az ,bx ,by, bz = list(map(int, line.replace('~', ',').split(',')))
	bricks.append((ax, ay, az, bx, by, bz))

	if ax != bx:
		for x in range(min(ax, bx), max(ax, bx) + 1):
			M[x][ay][az] = chr(ord('A') + l)
	if ay != by:
		for y in range(min(ay, by), max(ay, by) + 1):
			M[ax][y][az] = chr(ord('A') + l)
	if az != bz:
		for z in range(min(az, bz), max(az, bz) + 1):
			M[ax][ay][z] = chr(ord('A') + l)

print()
print(M)
