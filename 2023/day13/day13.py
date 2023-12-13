#input: https://adventofcode.com/2023/day/13/input

import numpy as np

mirrors = open('13.in').read().split('\n\n')

M = []
for mir in mirrors:
	mir = mir.split('\n')
	for l in range(len(mir)):
		mir[l] = list(mir[l])
	mir = np.array(mir)
	M.append(mir)

def comp(a,b):
	found = 0
	for i in range(len(a)):
		for j in range(len(a[0])):
			if a[i][j] != b[i][j]: found += 1
	return found

sum1 = 0
sum2 = 0
for m in M:
	count1 = 0
	count2 = 0
	
	for i in range(1,len(m[0])):
		test = np.split(m, [i], axis=1)
		test[0] = np.flip(test[0],1)
					
		if len(test[0][0]) > len(test[1][0]): 
			j = np.split(test[0], [ len(test[1][1]) ], axis=1)
			test[0] = j[0]
		else:
			j = np.split(test[1], [ len(test[0][1]) ], axis=1)
			test[1] = j[0]
	
		if comp(test[0],test[1]) == 1:
			count2 += i
		if comp(test[0],test[1]) == 0:
			count1 += i
	
	sum1 += count1
	count1 = 0
	sum2 += count2
	count2 = 0

	for i in range(1,len(m)):
		test = np.split(m, [i], axis=0)
		test[0] = np.flip(test[0],0)

		if len(test[0]) > len(test[1]): 
			j = np.split(test[0], [ len(test[1]) ], axis=0)
			test[0] = j[0]
		else:
			j = np.split(test[1], [ len(test[0]) ], axis=0)
			test[1] = j[0]

		if comp(test[0],test[1]) == 1:
			count2 += i * 100
		if comp(test[0],test[1]) == 0:
			count1 += i * 100
	sum1 += count1
	sum2 += count2
print('Answer 1:',sum1)
print('Answer 2:',sum2)


	










