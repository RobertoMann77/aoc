#input: https://adventofcode.com/2023/day/10

M = [i.strip() for i in open('10.in')]
for l in range(len(M)): M[l] = list(M[l])

def print_grid(R):
	for s in range(len(R)):
		l = ''
		for t in range(len(R[0])):
			if (s,t) in trace:	l += 'o'
			elif (s,t)	in found:   l += 'I'
			if (s,t) not in trace and (s,t) not in found: l += M[s][t]
		print(l)

rows = len(M)
col = len(M[0])

# find S pos and form
for i,s in enumerate(M):
		for j,t in enumerate(s):
			if t == 'S': S = (i,j)

def go(z):
	pos = z[0]
	di = z[1]
	x = 0
	y = 0
	m = M[pos[0]][pos[1]]
	if m == '-':
		if di == 'l':
			x = -1
			d = 'l'
		if di == 'r': 
			x = 1
			d = 'r'
	elif m == '|':
		if di == 'u': 
			y = -1
			d = 'u'
		if di == 'd': 
			y = 1
			d = 'd'
	elif m == 'F':
		if di == 'u': 
			x = 1
			d = 'r'
		if di == 'l': 
			y = 1
			d = 'd'
	elif m == 'J':
		if di == 'd': 
			x = -1
			d = 'l'
		if di == 'r': 
			y = -1
			d = 'u'
	elif m == 'L':
		if di == 'd': 
			x = 1
			d = 'r'
		if di == 'l': 
			y = -1
			d = 'u'
	elif m == '7':
		if di == 'r': 
			y = 1
			d = 'd'
		if di == 'u': 
			x = -1
			d = 'l'
	return ((pos[0]+y,pos[1]+x),d)	# from z to next pos

if rows > 30: M[S[0]][S[1]] = '-'	# 10.in
else: M[S[0]][S[1]] = 'F'				# t.in

# find way
old = (S,'r')			# direction must be entered
new = ((0,0),'l')		# because of while loop
count = 0
trace = []				
while new[0] != S:	# find a way on round
	new = (go(old))
	old = new
	count += 1
	trace.append(new[0])
print('Answer 1:',count//2)	# find halfway

empty = []		# all pos not on trace
for s in range(len(M)):
		for t in range(len(M[0])): 
			if (s,t) not in trace : empty.append((s,t))

sum1 = 0
for test in empty:
	r = test[0]
	c = test[1]
	count = 0
	
	fc = 0 	# counter for F
	lc = 0 	# counter for L
	way = ''
	for i in range(c+1,col):	# count pipes on trace from pos to right boarder
		way += M[r][i]
		if M[r][i] == '|' and (r,i) in trace: count += 1
		if M[r][i] == 'J' and (r,i) in trace:					# taking care of edges in pipe
			if fc == 1:
				count += 1
				fc = 0
			if lc == 1:
				lc = 0
		if M[r][i] == '7' and (r,i) in trace:
			if lc == 1:
				count += 1
				lc = 0
			if fc == 1:
				fc = 0
		if M[r][i] == 'F' and (r,i) in trace: fc = 1
		if M[r][i] == 'L' and (r,i) in trace: lc = 1
	if count % 2 == 1:
		sum1 += 1
	#print(test,way,count_right)
print('Answer 2:',sum1)



