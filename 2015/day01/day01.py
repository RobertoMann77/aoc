# input: https://adventofcode.com/2015/day/1

data = open("1.in").read()

print('Answer 1:',data.count('(') - data.count(')'))

floor = 0
for x,c in enumerate(data):
  if c == '(' : floor += 1
  else : floor -= 1
  if floor == -1:
    print('Answer 2:',x+1)
    break
