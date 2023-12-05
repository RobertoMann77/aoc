# input file must have an empty line at the ending !!!!!!
# otherwise no block nr 6 at the end!!!
data = [i.strip() for i in open('5.in')]
a, seeds = data.pop(0).split(':')
seeds = [int(i) for i in seeds.split()]

data.pop(0)
blocks = []
new = []

for line in data:
  if line: new.append(line)
  else:
    blocks.append(new)
    new = []

for b, block in enumerate(blocks):
  block.pop(0)
  for l, line in enumerate(block):
    blocks[b][l] = blocks[b][l].split()
    for i, entry in enumerate(blocks[b][l]):
      blocks[b][l][i] = int(blocks[b][l][i])

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
p = 23730000  #to lower the comute time
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
