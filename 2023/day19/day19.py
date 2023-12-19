
workflows, parts = open('t.in').read().split('\n\n')
 
def test_rule(var, values):
	(x, m, a, s) = values
	for w in work[var]: 
		if eval(w[0]) == True:
			if w[1] == 'A': return 'A'
			elif w[1] == 'R': return 'R'
			return test_rule(w[1], values)
	return test_rule(go[var], values)

def go_rev(link):
	print(link,rev_tree[link])
	x = rev_tree[link]
	a = rtree[link[1]]
	if a == 'in' :
		print((link[1],a),rev_tree[(link[1],a)])
		return x
	return x + ' ' + go_rev((link[1],a))
	
parts = parts.split()
wf = workflows.split()

work = {}
sum1 = 0

for w in wf:
	name, rest = w.split('{')
	rules = rest[:-1].split(',')
	rules[-1] = 'True:' + rules[-1]
	
	work[name] = []
	for rule in rules:
		work[name].append(rule.split(':'))

for part in parts:
	p = part[1:-1].split(',')
	x = int(p[0][2:])
	m = int(p[1][2:])
	a = int(p[2][2:])
	s = int(p[3][2:])

	if test_rule('in', (x, m, a, s)) == 'A':
		sum1 += x + m + a + s
print('Answer 1:',sum1)

rev_tree = {}
rtree = {}

ways = []

for z in work:
	bed = ''
	for y in work[z]:
		if (y[1],z) in rev_tree: 
			print('ACHTUNG: old:', rev_tree[(y[1],z)],' new: ',bed + ' ' + y[0])
		rev_tree[(y[1],z)] = bed + ' ' + y[0]
		rtree[y[1]] = z
		bed += ' ' + 'n' + y[0]

path = []
for t in rev_tree:
	if t[0] == 'A': 
		print('-'*20)
		ways.append(go_rev(t).replace('True',' ').split())

sum2 = 0
for w in range(len(ways)):
	if 'True' in ways[w]:
		ways[w].remove('True')

for way in ways:
	print()
	print(way)
	xmin = 0
	xmax = 4001
	mmin = 0
	mmax = 4001
	amin = 0
	amax = 4001
	smin = 0
	smax = 4001
	for w in way:
		if w[0] == 'n':
			if w[2] == '>':	w = w[1] + '<' + str(int(w[3:]) + 1)
			if w[2] == '<':	w = w[1] + '>' + str(int(w[3:]) - 1)
		
		z = int(w[2:])
		if w[0] == 'x':
			if w[1] == '>':
				if z > xmin: xmin = z
			else:
				if z < xmax: xmax = z
		if w[0] == 'm':
			if w[1] == '>':
				if z > mmin: mmin = z
			else:
				if z < mmax: mmax = z
		if w[0] == 'a':
			if w[1] == '>':
				if z > amin: amin = z
			else:
				if z < amax: amax = z
		if w[0] == 's':
			if w[1] == '>':
				if z > smin: smin = z
			else:
				if z < smax: smax = z
	
	sum2 += (xmax - xmin - 1) * (mmax - mmin - 1) * (amax - amin - 1) * (smax - smin - 1)

	print('xmin=',xmin,'xmax=',xmax,'mmin=',mmin,'mmax=',mmax,'amin=',amin,'amax=',amax,'smin=',smin,'smax=',smax)
	
print(sum2)


