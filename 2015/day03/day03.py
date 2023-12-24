# input: https://adventofcode.com/2015/day/3

data = open('3.in').read().strip()

h = [(0,0)]

go = {'^': (0,-1),
      'v': (0,1),
      '<': (-1,0),
      '>': (1,0)}

for r in data:
  dx = go[r][0]
  dy = go[r][1]
  h.append((h[-1][0] + dx , h[-1][1] + dy))

h = set(h)
print('Answer 1:', len(h))

san = [(0,0)]
rob = [(0,0)]
for r in range(0,len(data)-1,2):
  dx = go[data[r]][0]
  dy = go[data[r]][1]
  san.append((san[-1][0] + dx , san[-1][1] + dy))
  dx = go[data[r+1]][0]
  dy = go[data[r+1]][1]
  rob.append((rob[-1][0] + dx , rob[-1][1] + dy))
h = set(rob + san)
print('Answer 2:', len(h))

