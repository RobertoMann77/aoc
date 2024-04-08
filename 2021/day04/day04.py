import numpy as np

data = [i.strip() for i in open('4.in')]
draw = [int(i) for i in data.pop(0).split(',')]
data.pop(0)
data.append('')
boards = []
temp = []

for line in data:
    if line != '':
        temp.append(line)
    else:
        boards.append(temp)
        temp = []
for a in range(len(boards)):
    for b in range(len(boards[0])):
        boards[a][b] = [int(i) for i in boards[a][b].split()]

#create mark boards
M = []
for B in boards:
    temp = []
    for line in B:
        temp.append([0 for _ in range(5)])
    temp = np.array(temp)
    M.append(temp)

found = 0
while found == 0:
    d = draw.pop(0)
    for i,B in enumerate(boards):
        for r in range(len(B)):
            for c in range(len(B[0])):
                if B[r][c] == d:
                    M[i][r][c] = 1
    #check lines
    test = M[i].sum(axis=0)
    for r in range(5):
        if M[i].sum(axis=0)[r] == 5 or M[i].sum(axis=1)[r] == 5:
            found = 1

B = np.array(B)
print(B)
print()
print(M[i])
print()
for x in range(5):
    for y in range(5):
        M[i][y][x] = abs(M[i][y][x] - 1) #invert marks

print(M[i]*B)
print('Answer 1: ', sum(sum(M[i] * B)) * d)

