data = [i.strip() for i in open('5.in')]

vowels = ['a', 'e', 'i', 'o', 'u']
combos = ['ab','cd','pq','xy']
nicecount1 = 0
nicecount2 = 0

for line in data:
  rule1 = 0
  rule2 = 0
  rule3 = 1

#PART 1
  count = 0
  for i in line:
    if i in vowels: count += 1
  if count > 2:
    rule1 = 1

  for i in range(1,len(line)):
    if line[i-1] == line[i]:
      rule2 = 1
    
    if line[i-1] + line[i] in combos:
      rule3 = 0
  if rule1 and rule2 and rule3: nicecount1 += 1
  
#PART2
for line in data:
  rule4 = 0
  rule5 = 0
  paircount = 0
  
  i = 0
  while (i < len(line)-1):
    pair = line[i] + line[i+1]
    if pair in line[i+2:]: 
      rule4 = 1
    i += 1
  i = 0
  while (i < len(line)-2):
    if line[i] == line[i+2]: 
      rule5 = 1
    i += 1
      
  if rule4 and rule5: 
    nicecount2 += 1
  
print('Answer 1:', nicecount1)
print('Answer 2:', nicecount2)
