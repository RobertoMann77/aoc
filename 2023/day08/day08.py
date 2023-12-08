# input: https://adventofcode.com/2023/day/8

data = [i.strip() for i in open('day08/8.in')]

M = {}
lr = data.pop(0)
data.pop(0)

for line in data:
    part = line.split()
    M[part[0]] = eval('(\'' + part[2][1:-1] + '\',\''+ part[3][:-1] + '\')')

def count_steps1(p):      # part 1
    count = 0
    while p != 'ZZZ':
        for i in lr:
            if i == 'R': p = M[p][1]
            if i == 'L': p = M[p][0]
            count += 1
    return count

def count_steps2(p):        #part 2
    count = 0
    while p[2] != 'Z':
        for i in lr:
            if i == 'R': p = M[p][1]
            if i == 'L': p = M[p][0]
            count += 1
    return count

def ggT(n, m):
    if m == 0:
        return n
    return ggT(m, n % m)

starts = []
ends = []
for m in M:
    if m[2] == 'A':
        starts.append(m)
    if m[2] == 'Z':
        ends.append(m)

steps = []
for pos in starts: steps.append(count_steps2(pos))

print('Answer 1:',count_steps1('AAA'))

lcm = 1
for i in steps: lcm = lcm * i // ggT(lcm, i)

print('Answer 2:',lcm)
