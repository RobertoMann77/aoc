workflows, parts = open('t.in').read().split('\n\n')

def test_rule(var, values):
	(x, m, a, s) = values
	for w in work[var]: 
		if eval(w[0]) == True:
			if w[1] == 'A': return 'A'
			elif w[1] == 'R': return 'R'
			return test_rule(w[1], values)
	return test_rule(go[var], values)

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



