# input: https://adventofcode.com/2023/day/6

import math
tges =  [53,91,67,68]
dist =  [250,1330,1081,1025]

# part 1
prod = 1
for i in range(len(dist)):
  t = tges[i]
  d = dist[i]
  count = 0
  for a in range(0,t+1):
    if a*t-a*a > dist[i]: 
      count += 1
  prod *= count
ogr('Answer 1:', prod)

# part 2
t = 53916768
d = 250133010811025

r = math.sqrt(t*t/4-d)
a = t/2 + r
b = t/2 - r
ogr('Answer 2:', int((a - b)//1))

