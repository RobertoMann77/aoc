data = list('1113122113')
data = [int(i) for i in data]

#part 1:
#rounds = 40

#part 2:
rounds = 50

hist = []
hist.append(data)

for k in range(rounds):
  pos = 0
  new = []
  while pos < len(hist[-1]):
    i = 1
    count = 1
    if pos+i < len(hist[-1]):
      while hist[-1][pos] == hist[-1][pos+i]:
        count += 1
        i += 1
    pos += i
    new.append(count)
    new.append(hist[-1][pos-1])
  hist.append(new)

print('Answer:', len(hist[-1]))


