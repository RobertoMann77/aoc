#day 24 2023
import sympy

data = [i.strip() for i in open('t.in')]
hail = []

target = []

for line in data:
	pos, vel = line.split('@')
	pos = list(map(int, pos.split(', ')))
	vel = list(map(int, vel.split(', ')))
	target.append(tuple(pos + vel))
	gl = [vel[1] / vel[0], -1]
	erg = - pos[1] + vel[1] * pos[0] / vel[0]
	t = [1 / vel[0], -pos[0] / vel[0]]
	hail.append([gl, erg, t])


if len(data) > 20:
	testmin = 200000000000000
	testmax = 400000000000000
else:
	testmin = 7
	testmax = 27

count = 0
for i in range(len(hail) - 1):
	for j in range(i + 1, len(hail)):	
		R = hail[i]
		S = hail[j]

		A = np.array([R[0], S[0]])
		b = np.array([R[1], S[1]])
		try: 								
			x = np.linalg.solve(A, b)	# error when parallel
		except:
			continue
		else:
			if testmin <= x[0] <= testmax and testmin <= x[1] <= testmax:
				if x[0] * R[2][0] + R[2][1] >= 0 and x[0] * S[2][0] + S[2][1] >= 0:
					count += 1



print('Answer 1:', count)

equat = []

a = target[0]
b = target[1]
c = target[2]


xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

for i, (sx, sy, sz, vx, vy, vz) in enumerate(target):
	equat.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
	equat.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))

	if i == 2:
		answers = [soln for soln in sympy.solve(equat) if all(x % 1 == 0 for x in soln.values())]
		break



print('Answer 2:', answers[0])
