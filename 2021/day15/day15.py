data = [i.strip() for i in open('t.in')]

C = complex

RL = {}
for r,line in enumerate(data):
	for c, rl in enumerate(line):
		RL[C(r,c)] = (int(rl),0)

print(RL)

curr = [(0,0)]

while curr:
	d = [C(0,1), C(1,0), C(0,-1), C(-1,0)]
	pos = curr.pop(0)
