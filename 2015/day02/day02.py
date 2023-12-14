# input: https://adventofcode.com/2015/day/2

data = [i.strip() for i in open('day2.in')]
a = 0  #paper
r = 0  #ribbon
for x in data:
  l,w,h = x.split('x')
  l,w,h = [int(x) for x in [l,w,h]]
  lw = l * w
  wh = w * h
  lh = l * h
  s = lw
  if wh < s: s = wh
  if lh < s: s = lh
  a += 2*lw + 2*wh + 2*lh + s
  c = [l,w,h]
  c.sort()
  r += 2*(c[0] + c[1]) + c[0]*c[1]*c[2]
  
print('Answer 1:', a)
print('Answer 2:', r)


