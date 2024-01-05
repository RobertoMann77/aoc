data = [i.strip() for i in open('t.in')]

reg = {'a' : 0,
	   'b' : 0,
	   'c' : 1,			# part 1: c = 0  part 2: c = 1
	   'd' : 0}

instr = []
for line in data:
	instr.append(line.split())

n = 0
while n < len(instr):
	if instr[n][0] == 'cpy':
		if instr[n][1].isdigit():
			reg[instr[n][2]] = int(instr[n][1])
		else:
			reg[instr[n][2]] = int(reg[instr[n][1]])
	if instr[n][0] == 'inc':
		reg[instr[n][1]] += 1
	if instr[n][0] == 'dec':
		reg[instr[n][1]] -= 1
	if instr[n][0] == 'jnz':
		if instr[n][1].isdigit():
			if instr[n][1] != 0:
				n += int(instr[n][2]) - 1
		else:
			if reg[instr[n][1]] != 0:
				n += int(instr[n][2]) - 1	
	n += 1
	

print('Answer 1:',reg['a'])
