data = [i.strip() for i in open('20.in')]

switch = {'lo': 'hi', 'hi': 'lo'}

def pr_state():
	print()
	print('state of computer:    *******************')
	for c in computer:
		print(computer[c][1], c)
	print()

# processes the signal input of a modul and delivers
def compute(signal,modul):
	if computer[modul][0] == '%':
		if signal == 'lo':
			computer[modul][1] = switch[computer[modul][1]]
			return (modul, computer[modul][2])
		if signal == 'hi':
			return 'nothing'

	if computer[modul][0] == '&':
		if len(conj[modul]) == 1:
			computer[modul][1] = switch[signal]		
			return (modul, computer[modul][2])

		if len(conj[modul]) > 1:
			on = True
			for t in conj[modul]:
				if computer[t][1] == 'lo': 
					on = False
			if on == True: computer[modul][1] = 'lo'
			else: computer[modul][1] = 'hi'
			return (modul, computer[modul][2])

	if computer[modul][0] == '§':
		computer[modul][1] = signal
		return 'nothing'


computer = {}
for line in data:
	a,b = line.split(' -> ')
	if a == 'broadcaster':
		broadcaster = b.split(', ')
	else:
		if a[0] == '%':
			computer[a[1:]] = ['%', 'lo', b.split(', ')]
		elif a[0] == '&':
			computer[a[1:]] = ['&', 'lo', b.split(', '),[]]
computer['output'] = ['§', 'lo',[]]
computer['rx'] = ['§', 'lo',[]]


# find out if & modul has one or more inputs
conj = {}
for c in computer:
	if computer[c][0] == '&': conj[c] = []
for c in computer:
	for test in computer[c][2]:
		if test in conj: conj[test].append(c)

lo_count = 0
hi_count = 0

for i in range(1000):
	lo_count += 1 # for broadcast push
	todo = []
	for j in broadcaster:
		#print('broadcast lo -> ',j)
		lo_count += 1
		compute('lo', j)
		todo.append((j,computer[j][2]))

	while todo:
		t = todo.pop(0)
		for y in t[1]:
			#print(t[0], computer[t[0]][1], ' -> ', y)
			if computer[t[0]][1] == 'lo':
				lo_count += 1
			else: hi_count += 1
			test = compute(computer[t[0]][1],y)

			if test != 'nothing':
				todo.append(test)

print('Answer 1:', lo_count * hi_count)













