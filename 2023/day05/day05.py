seeds, *changes = open('t.in').read().split('\n\n')
seeds = list(map(int, seeds.split(":")[1].split()))

blocks = []
for block in changes:
  ranges = []
  for line in block.splitlines()[1:]:
      ranges.append(list(map(int, line.split())))
  blocks.append(ranges)

def calc(r):
  for i in range(len(blocks)):
    c = 0
    for line in blocks[i]:
      ds = line[0]
      sr = line[1]
      l = line[2]
      if sr <= r and r <= sr + l and c == 0:
        r = ds + r - sr
        c = 1
  return r

def revcal(r):
  for i in range(6, -1, -1):
    c = 0
    for line in blocks[i]:
      ds = line[0]
      sr = line[1]
      l = line[2]
      if ds <= r and r <= ds + l and c == 0:
        r = sr + r - ds
        c = 1
  return r

#part 1
loc = []
for seed in seeds:
  loc.append(calc(seed))
print('Answer 1:', min(loc))

#part 2
#p = 0  
p = 23730000  #to lower the compute time
found = 0
while found == 0:
  cal = revcal(p)
  i = 0
  while i < len(seeds):
    if seeds[i] <= cal <= seeds[i] + seeds[i + 1]:
      print('Answer 2:', p)
      found = 1
    i += 2
  p += 1
