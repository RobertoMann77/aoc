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

	if max(ax,bx) > xmax: xmax = max(ax,bx)
	if max(ay,by) > ymax: ymax = max(ay,by)
	if max(az,bz) > zmax: zmax = max(az,bz)


M = []
for x in range(xmax + 1):
	s = []
	for y in range(ymax + 1):
		t = []
		for z in range(zmax + 1):
			t.append(0)
		s.append(t)
	M.append(s)

M = np.array(M)

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

	A = (ax, ay, az)
	B = (bx, by, bz)
	bricks.append(((ax, ay, az),(bx, by, bz)))

	if ax != bx:
		for x in range(min(ax,bx),max(ax,bx) + 1):
			M[x][ay][az] = 1
	if ay != by:
		for y in range(min(ay,by),max(ay,by) + 1):
			M[ax][y][az] = 1
	if az != bz:
		for z in range(min(az,bz),max(az,bz) + 1):
			M[ax][ay][z] = 1

for brick in bricks:
	print(brick)
print()
print(M)