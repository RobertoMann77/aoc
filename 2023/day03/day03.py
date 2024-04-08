# input: https://adventofcode.com/2023/day/3

data = [i.strip() for i in open('3.in')]

for l in range(len(data)): data[l] = '.' + data[l] + '.'
data.insert(0, '.' * len(data[0])),
data.append('.' * len(data[0]))

G = [[c for c in lines] for lines in data]

zahl = []              #[zahl, row, cmin, cmax]
stern = {}             #(row,char):[n1,n2,....]
for r in range(len(G)):
  n = 0
  for c in range(len(G[r])):
    if G[r][c].isnumeric(): n = 10*n + int(G[r][c])
    elif n:
      zahl.append([n,r,c-len(str(n)),c-1])
      n = 0
      
sum = 0
for z in zahl:
  for r in range(z[1]-1,z[1]+2):
    for c in range(z[2]-1,z[3]+2):
      if not G[r][c].isnumeric() and G[r][c] != '.':
        sum += z[0]
      if G[r][c] == '*':
        if (r,c) in stern: stern[(r,c)].append(z[0])
        else: stern[(r,c)] = [z[0]]

ogr('Answer 1:',sum)
gear = 0
for cand in stern: 
  if len(stern[cand]) == 2: 
    gear += stern[cand][0] * stern[cand][1]
ogr('Answer 2:',gear)


