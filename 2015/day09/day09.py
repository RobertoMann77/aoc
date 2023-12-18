from itertools import permutations
data = [i.strip() for i in open('9.in')]

M = {}  # map distance info
D = []  # destinations

for line in data:
  part = line.split()
  a = part[0]
  b = part[2]
  d = part[4]
  if a not in D: D.append(a)
  if b not in D: D.append(b)
  M[(a,b)] = int(d)
  M[(b,a)] = int(d)

dist = []
perm = permutations(D)
for p in perm:
  d = 0
  for i in range(len(p)-1):
    d += M[(p[i],p[i+1])]
  dist.append(d)
    
print(min(dist))
print(max(dist))