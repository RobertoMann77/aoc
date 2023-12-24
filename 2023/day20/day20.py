data = [i.strip() for i in open('20.in')]

switch = {'lo': 'hi', 'hi': 'lo'}



watch = {}
watch['kk'] = []
watch['vt'] = []
watch['sk'] = []
watch['xc'] = []

# processes the signal input of a modul and push to destinaton modules
def compute(signal,modul):

	if comp[modul][0] == '%':
		if signal == 'lo':
			comp[modul][1] = switch[comp[modul][1]]
			return (modul, comp[modul][2])
		if signal == 'hi':
			return 'nothing'

	if comp[modul][0] == '&':
		if len(conj[modul]) == 1:
			comp[modul][1] = switch[signal]		
			return (modul, comp[modul][2])

		if len(conj[modul]) > 1:
			on = True
			for t in conj[modul]:
				if comp[t][1] == 'lo': 
					on = False
			if on == True: 
				comp[modul][1] = 'lo'

			else: comp[modul][1] = 'hi'
			return (modul, comp[modul][2])

	if comp[modul][0] == '§':	# for rx and output modul
		comp[modul][1] = signal
		return 'nothing'

	if comp[modul][1] == 'lo':
		if modul == 'kk':
			watch['kk'].append((i,signal))
		if modul == 'vt':
			watch['vt'].append((i,signal))
		if modul == 'sk':
			watch['sk'].append((i,signal))
		if modul == 'xc':
			watch['xc'].append((i,signal))


comp = {}
for line in data:
	a,b = line.split(' -> ')
	if a == 'broadcaster':
		bc = b.split(', ')
	else:
		if a[0] == '%':
			comp[a[1:]] = ['%', 'lo', b.split(', ')]
		elif a[0] == '&':
			comp[a[1:]] = ['&', 'lo', b.split(', '),[]]

# 
comp['output'] = ['§', 'lo',[]]
comp['rx'] = ['§', 'lo',[]]


# find out if & modul has one or more inputs
conj = {}
for c in comp:
	if comp[c][0] == '&': conj[c] = []
for c in comp:
	for test in comp[c][2]:
		if test in conj: conj[test].append(c)

lo_count = 0
hi_count = 0
rx_states = []



for i in range(1000000):
	if i%100000 == 0:
		for tt in watch:
			print(tt,watch[tt][-5:])
		print()
	lo_count += 1 # for broadcast push
	todo = []
	for j in bc:
		lo_count += 1
		compute('lo', j)
		todo.append((j,comp[j][2]))

	while todo:
		t = todo.pop(0)
		for y in t[1]:
			if y == 'rx' and comp[t[0]][1] == 'lo':
				print('Answer 2:', i)
				break
				
			if comp[t[0]][1] == 'lo':
				lo_count += 1
			else: hi_count += 1
			test = compute(comp[t[0]][1],y)

			if test != 'nothing':
				todo.append(test)
	if i == 999:
		print('Answer 1:', lo_count * hi_count)
print()













