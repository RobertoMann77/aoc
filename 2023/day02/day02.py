data = [i.strip() for i in open('2.in')]

sum1 = 0
sum2 = 0
for line in data:
  x,y = line.split(': ')
  games = y.split('; ')
  id = int(x.split(' ')[1])
  r = 0
  g = 0
  b = 0
  for game in games:
    pair = game.split(', ')
    for test in pair:
      anz,farbe = test.split(' ')
      if farbe == 'red' and int(anz) > r : r = int(anz)
      if farbe == 'green' and int(anz) > g : g = int(anz)
      if farbe == 'blue' and int(anz) > b : b = int(anz)
  if r < 13 and g < 14 and b < 15: sum1 += id
  sum2 += r*g*b
print('Answer 1:',sum1)
print('Answer 2:',sum2)

    
