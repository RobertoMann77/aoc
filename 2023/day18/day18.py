import numpy as np
data = [i.strip() for i in open('18.in')]

def det(a,b): 
	return(a[0] * b[1] - a[1] * b[0])

# part 1
border = 0
pos = [(0,0)]

for line in data:
	d, s, c = line.split()
	s = int(s)

	if d == 'R': pos.append((pos[-1][0], pos[-1][1] + s))
	if d == 'L': pos.append((pos[-1][0], pos[-1][1] - s))
	if d == 'U': pos.append((pos[-1][0] - s, pos[-1][1]))
	if d == 'D': pos.append((pos[-1][0] + s, pos[-1][1]))
	border += s

sum1 = 0
for (p1,p2) in list(zip(pos, pos[1:])):
	sum1 += det(p1, p2)
print('Answer 1:', int(abs(sum1/2) + border/2 + 1))


# part 2
border = 0
pos = [(0,0)]

for line in data:
	code = line.split()[2][2:-1]
	s = code[:-1]
	s = int('0x'+s, 16)
	d = int(code[-1])

	if d == 0: pos.append((pos[-1][0], pos[-1][1] + s))
	if d == 2: pos.append((pos[-1][0], pos[-1][1] - s))
	if d == 3: pos.append((pos[-1][0] - s, pos[-1][1]))
	if d == 1: pos.append((pos[-1][0] + s, pos[-1][1]))
	border += s

sum2 = 0
for (p1,p2) in list(zip(pos, pos[1:])):
	sum2 += det(p1, p2)
print('Answer 2:', int(abs(sum2/2) + border/2 + 1))





