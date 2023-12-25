import numpy as np
from z3 import *

data = [i.strip() for i in open('24.in')]
hail = []

for line in data:
	pos, vel = line.split('@')
	pos = list(map(int, pos.split(', ')))
	vel = list(map(int, vel.split(', ')))
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

