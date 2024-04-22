data = [i.strip() for i in open('t.in')]

M = {}

C = complex

for r, line in enumerate(data):
	for c, char in enumerate(line):
		M[C(r, c)] = char

def neighbours(P):
	neighbours = []
	for dir in [C(1, 0), C(-1, 0), C(0, 1), C(0, -1)]:	
		newP = P + dir
		if newP in M:
			if M[newP] == '.':
				neighbours.append(newP)
	return neighbours

print(neighbours(C(1, 3)))





a = C(0, 1)
b = C(3, 3)

print(a+b)
print()

#rotate π/2
print(a * 1j)
print()


N = {}
N[C(1,3)] = 5
N[C(3,7)] = 6

print(N)

S = {}
for i in N:
	S[i * 1j] = N[i]

print(S)