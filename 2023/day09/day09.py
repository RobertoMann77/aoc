#input: https://adventofcode.com/2023/day/9

data = [i.strip() for i in open('9.in')]

for l,line in enumerate(data):
	data[l] = [i.strip() for i in line.split()]

for l,line in enumerate(data):
	for c,ccc in enumerate(line):
		data[l][c] = int(data[l][c])

#part 1
sum1 = 0
for line in data:
	new = [line]
	not_zero = True
	while not_zero == True:
		n = []
		for i in range(len(new[-1])-1):
			n.append(new[-1][i+1]-new[-1][i])
		new.append(n)

		check = 0
		for j in new[-1]:
			if j != 0: check =1
		if check == 1: 
			not_zero = True
		else:
			not_zero = False

	new[-1].append(0)
	for i in range(len(new)-2,-1,-1):
		new[i].append(new[i][-1]+new[i+1][-1])
	sum1 += new[0][-1]
print('Answer 1:', sum1)
		
#part 2
sum2 = 0
for line in data:
	new = [line]
	test = True
	while test == True:
		n = []
		for i in range(len(new[-1])-1):
			n.append(new[-1][i+1]-new[-1][i])
		new.append(n)

		check = 0
		for j in new[-1]:
			if j != 0: check =1
		if check == 1: 
			test = True
		else:
			test = False


	new[-1] = [0] + new[-1]
	for i in range(len(new)-2,-1,-1):
		new[i] = [new[i][0] - new[i+1][0]] + new[i]

	sum2 += new[0][0]

print('Answer 2:', sum2)



