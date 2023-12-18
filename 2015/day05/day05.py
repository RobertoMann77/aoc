data = [i.strip() for i in open('day05.in')]

vowels='aeiou'
combos=['ab','cd','pq','xy']
nicecount1=0
nicecount2=0

for item in data:
  rule1=0
  rule2=0
  rule3=1

#PART 1
  count=0
  for i in item:
    if i in vowels: count+=1
  if count>2:
    rule1=1

  for i in range(1,len(item)):
    if item[i-1]==item[i]:
      rule2=1
    
    if item[i-1]+item[i] in combos:
      rule3=0
  if rule1==1 and rule2==1 and rule3==1: nicecount1+=1
  
#PART2

for item in data:
  rule4=0
  rule5=0
  paircount=0
  
  i = 0
  while (i < len(item)-1):
    pair = item[i]+item[i+1]
    if pair in item[i+2:]: 
      rule4=1
    i += 1
  i = 0
  while (i < len(item)-2):
    if item[i] == item[i+2]: 
      rule5=1
    i += 1
      
  if rule4==1 and rule5==1: 
    nicecount2+=1
  
print('Answer 1:',nicecount1)
print('Answer 2:',nicecount2)