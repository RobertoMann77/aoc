# input: https://adventofcode.com/2023/day/1

data = [i.strip() for i in open('1.in')]
sw = {'one':'o1e', 'two':'t2o', 'three':'t3e', 'four':'f4r', 'five':'f5e', 'six':'s6x', 'seven':'s7n', 'eight':'e8t', 'nine':'n9e'}

def valnum(k):
  r = ''
  for i in k:
    if i.isdigit():  r += i
  return int(r[0] + r[-1])

sum1 = 0
sum2 = 0
for line in data:
  sum1 += valnum(line)
  for n in sw:
    line = line.replace(n,sw[n])
  sum2 += valnum(line)
print('Answer 1:',sum1)
print('Answer 2:',sum2)
