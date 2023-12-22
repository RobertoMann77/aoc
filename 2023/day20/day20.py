data = [i.strip() for i in open('t.in')]
import functools


switch = {'lo': 'hi', 'hi': 'lo'}

@functools.lru_cache
def compute(signal,modul):
	print('signal:', signal,' -> ',modul)
	if modul == 'output' or modul == 'rx':
		#print('output:',signal)
		return 'nothing'
	if computer[modul][0] == '%':
		if signal == 'lo':
			computer[modul][1] = switch[computer[modul][1]]
			return (modul, computer[modul][2])
		if signal == 'hi':
			return 'nothing'
	if computer[modul][0] == '&':
		computer[modul][1] = switch[signal]		
		return (modul, computer[modul][2])
		
computer = {}
for line in data:
	a,b = line.split(' -> ')
	if a == 'broadcaster':
		broadcaster = b.split(', ')
	else:
		if a[0] == '%':
			computer[a[1:]] = ['%','lo',b.split(', ')]
		elif a[0] == '&':
			computer[a[1:]] = ['&','lo',b.split(', ')]

lo_count = 0
hi_count = 0

for i in range(1):
	lo_count += 1
	todo = []
	for i in broadcaster:
		print('broadcast',i)
		lo_count += 1
		compute('lo', i)
		todo.append((i,computer[i][2]))
	print()
	#print('todo', todo)

	while todo:
		t = todo.pop(0)
		#print(t)
		if t != 'done':
			for y in t[1]:
				if computer[t[0]][1] == 'lo':
					lo_count += 1
				else: hi_count += 1
				test = compute(computer[t[0]][1],y)

				if test != 'nothing':
					todo.append(test)


print()
print('lo_count:', lo_count)
print('hi_count:', hi_count)
print('Answer 1:', lo_count * hi_count)

