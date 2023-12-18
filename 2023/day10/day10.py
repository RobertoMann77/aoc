M = [i.strip() for i in open('10.in')]
for l in range(len(M)): M[l] = list(M[l])

def det(a,b): 
	return(a[0] * b[1] - a[1] * b[0])

rows = len(M)
col = len(M[0])

# find S pos and form
for i,s in enumerate(M):
		for j,t in enumerate(s):
			if t == 'S': S = (i,j)

path = [S]
border = 0
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
		elif di == 'r': 
			x = 1
			d = 'r'
	elif m == '|':
		if di == 'u': 
			y = -1
			d = 'u'
		elif di == 'd': 
			y = 1
			d = 'd'
	elif m == 'F':
		path.append(pos)
		if di == 'u': 
			x = 1
			d = 'r'
		elif di == 'l': 
			y = 1
			d = 'd'
	elif m == 'J':
		path.append(pos)
		if di == 'd': 
			x = -1
			d = 'l'
		elif di == 'r': 
			y = -1
			d = 'u'
	elif m == 'L':
		path.append(pos)
		if di == 'd': 
			x = 1
			d = 'r'
		elif di == 'l': 
			y = -1
			d = 'u'
	elif m == '7':
		path.append(pos)
		if di == 'r': 
			y = 1
			d = 'd'
		elif di == 'u': 
			x = -1
			d = 'l'
	return ((pos[0]+y,pos[1]+x),d)	# from z to next pos

if rows > 30: 
	M[S[0]][S[1]] = '-'		# 10.in
	old = (S,'r')
else: 
	M[S[0]][S[1]] = 'F'		# t.in
	old = (S,'u')

new = ((0,0),'l')		# because of while loop
count = 0
trace = []				
while new[0] != S:		# find a way on round
	border += 1
	new = (go(old))
	old = new
	count += 1
	trace.append(new[0])
print('Answer 1:',count//2)	# find halfway

empty = []				# all pos not on trace
for s in range(len(M)):
		for t in range(len(M[0])): 
			if (s,t) not in trace : empty.append((s,t))

path.append(S)
sum2 = 0
for (p1,p2) in list(zip(path, path[1:])):
	sum2 += det(p1, p2)
print('Answer 2:', int(abs(sum2/2) - border/2 + 1))

