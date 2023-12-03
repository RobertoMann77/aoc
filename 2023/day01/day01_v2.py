data = [i.strip() for i in open('1.in')]

s1 = 0
s2 = 0
for line in data:
  d1 = []
  d2 = []
  for i,c in enumerate(line):
    if c.isdigit():
      d1.append(c)
      d2.append(c)
    for d,check in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
      if line[i:].startswith(check):
        d2.append(str(d+1))
  s1 += int(d1[0] + d1[-1])
  s2 += int(d2[0] + d2[-1])

print('Answer 1:',s1)
print('Answer 2:',s2)
