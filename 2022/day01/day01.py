data = [i.strip() for i in open('day1.in')]

count = 0
bags = []

for item in data:
  if item: 
    count += int(item)
  else: 
    bags.append(count)
    count = 0
    
bags.sort(reverse = True)

print('Answer 1:',bags[0])
print('Answer 2:',bags[0]+bags[1]+bags[2])
