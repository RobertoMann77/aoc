#https://adventofcode.com/2022/day/2

data = [l.strip() for l in open('day2.in')]
score1 = 0
score2 = 0
for x in data:
  a,b = x.split()
  score1 += {'X' : 1, 'Y' : 2, 'Z' : 3}[b]
  score1 += {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
            ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
            ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3}[(a,b)]
print('Answer 1:',score1)

for x in data:
  a,b = x.split()
  score2 += {'X' : 0, 'Y' : 3, 'Z' : 6}[b]
  score2 += {('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2,
            ('B', 'X'): 1, ('B', 'Y'): 2, ('B', 'Z'): 3,
            ('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1}[(a,b)]
print('Answer 1:',score2)
