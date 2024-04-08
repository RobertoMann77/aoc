data = open('t.in').read().strip().replace('\n','')

def counter(list):
   sum = 0
   num = ''
   sig = 1
   for i in list:
      if i == '-': sig = 0
      if i.isdigit() == True: num += i
      elif num: 
         if sig == 1: sum += int(num)
         else: sum -= int(num)
         num = ''
         sig = 1
   return sum

ogr('Answer 1:',counter(data))

#part 2

def testrun(datensatz):
   for i in range(len(datensatz)):
      found =0
      if data[i:].startswith(':\"red\"'):
         eckzu = 0
         geschzu = 0
         auf = data[i:].count('{')
         zu = data[i:].count('}')
         for j in range(i+6,len(data)):
            if data[j] == '[': eckzu -= 1
            elif data[j] == ']': eckzu += 1
            elif data[j] == '{': geschzu -= 1
            elif data[j] == '}': geschzu += 1
            if eckzu == 1: 
               break
            if geschzu == 1 and eckzu == 0: 
               found = 1
               eckauf = 0
               geschauf = 0
               for k in range(i+1,0,-1):
                  if data[k] == '{': geschauf += 1
                  elif data[k] == '}': geschauf -= 1
                  if geschauf == 1:
                     new = data[:k+4] + data[j:]
                     return new
   return datensatz

p = 1
q = 0
while q < p:
   p = len(data)
   data = testrun(data)
   q = len(data)
ogr('Answer 2:',counter(data))






