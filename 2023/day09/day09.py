#input: https://adventofcode.com/2023/day/9

data = [i.strip() for i in open('9.in')]

for l,line in enumerate(data):
	data[l] = [i.strip() for i in line.split()]

for l,line in enumerate(data):
	for c,ccc in enumerate(line):
		data[l][c] = int(data[l][c])


def zero_check(a):
	check = 0
	for j in a:
		if j != 0: check =1
	if check == 1: 
		return True
	else:
		return False

#part 1
sum1 = 0
sum2 = 0
for line in data:
	new = [line]
	while zero_check(new[-1]) == True:
		new_line = []
		for i in range(len(new[-1])-1):
			new_line.append(new[-1][i+1]-new[-1][i])
		new.append(new_line)

	new1 = new

	#part 1
	new[-1].append(0)
	for i in range(len(new)-2,-1,-1):
		new[i].append(new[i][-1]+new[i+1][-1])
	sum1 += new[0][-1]

	#part 2
	new[-1] = [0] + new[-1]
	for i in range(len(new)-2,-1,-1):
		new[i] = [new[i][0] - new[i+1][0]] + new[i]
	sum2 += new[0][0]

print('Answer 1:', sum1)
print('Answer 2:', sum2)



