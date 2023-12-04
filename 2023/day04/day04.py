data = [i.strip() for i in open('t.in')]

sum1 = 0
cc = []  #cardcount   [score,#]
for line in data:
  a,b = line.split('|')
  c,d = a.split(':')
 
  wnum = [int(i) for i in d.split()]
  ynum = [int(i) for i in b.split()]
  
  c = 0  #count
  s = 0  #score
  for number in ynum:
    if number in wnum: c += 1
  if c == 1: s = 1
  elif c: s += 2**(c-1)
  cc.append([c,1])
  sum1 += s
print('Answer 1:',sum1)

for i,card in enumerate(cc):
  for z in range(card[0]): cc[i+z+1][1] += cc[i][1]

print('Answer 2:',(sum([z[1] for z in cc])))
