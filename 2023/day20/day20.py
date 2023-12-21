data = [i.strip() for i in open('t.in')]

switch = {0: 1, 1: 0}

def compute(signal,modul):
	if computer[modul][0] == '%':
		if signal == 0:
			computer[modul][1] = switch[computer[modul][1]]
			return computer[modul][1]
		if signal == 1:
			return 9
	if computer[modul][0] == '&':
		computer[modul][1] = switch[signal]
		return computer[modul][1]
		
computer = {}

for line in data:
	a,b = line.split(' -> ')
	if a == 'broadcaster':
		broadcaster = b.split(', ')
	else:
		if a[0] == '%':
			computer[a[1:]] = ['%',0,b.split(', ')]
		elif a[0] == '&':
			computer[a[1:]] = ['&',0,b.split(', ')]

print('broadcaster:', broadcaster)
print()


for c in computer:
	print(c,computer[c])

todo = []

for i in broadcaster:
	print(compute(0, i))
	todo.append((i,computer[i][2]))


print()
for c in computer:
	print(c,computer[c])

while todo:
	t = todo.pop(0)
	for y in t[1]:
		print(computer[t[0]][1],y)
		sig = (computer[t[0]][1],y)
		compute(computer[t[0]][1],y)

print()
for c in computer:
	print(c,computer[c])



'''
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
'''

