# input: https://adventofcode.com/2023/day/15

#TEST
data = open('15.in').read().split(',')

def doit(raw_c,cv):
	cv += ord(raw_c)
	cv *= 17
	return cv % 256
sum1 = 0 
for line in data:
	cv = 0
	for buchst in line: cv = doit(buchst,cv)
	sum1 += cv
print('Answer 1:',sum1)

len_fl = {}
boxes = {}
for t in range(256):
	boxes[t] = []
for line in data:
	if '-' in line:
		op = '-'
		for i in range(len(line)+1):
			if line[:i].endswith('-'): 
				lens = line[:i-1]+line[-1]

	if '=' in line:
		op = '='
		for i in range(len(line)+1):
			if line[:i].endswith('='): 
				lens = line[:i-1]+line[-1]
				fl = int(line[i:])
		
	cv = 0
	for buchst in lens[:-1]: cv = doit(buchst,cv)
	

	if op == '=':
		found = 0
		for l in boxes[cv]:
			if lens[:-1] == l[:-1]: 
				found = 1
				boxes[cv][boxes[cv].index(l)] = lens

		if found == 0:
			boxes[cv].append(lens)

	if op == '-':
		for l in boxes[cv]:
			if lens[:-1] == l[:-1]: boxes[cv].remove(l)
	
focus_power = 0
for b,box in enumerate(boxes):
	for l,lens in enumerate(boxes[box]):
		if lens != '':
			focus_power += int(lens[-1]) * (b+1) * (l+1)
print('Answer 2:',focus_power)

