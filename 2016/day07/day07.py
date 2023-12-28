data = [i.strip() for i in open('7.in')]

def abba(s):
	rule = False
	for i in range(len(s) - 3):
		r = s[i:i+4]
		if r[0] == r[3] and r[1] == r[2] and r[0] != r[1]:
			rule = True
	return rule

c1 = 0
c2 = 0
for l,line in enumerate(data):
	outside = ''
	inside = ''
	parts = line.replace(']','[').split('[')

	for p,part in enumerate(parts):
		if p % 2 == 0:
			outside += ' ' + part
		else:
			inside += ' ' + part
		
	#part 1:
	if abba(outside) == True and abba(inside) == False:
		c1 += 1

	# part 2:
	for i in range(len(outside) - 2):
		r = outside[i:i+3]
		if r[0] == r[2] and r[0] != r[1] and r[1] + r[0] +r[1] in inside:
			c2 += 1
			break

print('Answer 1:', c1)
print('Answer 2:', c2)





