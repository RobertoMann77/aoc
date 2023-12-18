data = [i.strip() for i in open('7.in')]
data = sorted(data, key=len)

table = {}
mem = {}

for line in data:
  cmd,variable = line.split(' -> ')
  if cmd.strip().isdigit():
    mem[variable] = int(cmd)
  table[variable] = cmd

def getval(var):
  if var in mem: return mem[var]
  if var.isdigit(): return int(var)
  s = table[var]
  print(s)
  if 'AND' in s:
    x1,x2 = s.split(' AND ')
    mem[var] = getval(x1) & getval(x2)
    return mem[var]
    
  if 'OR' in s:
    x1,x2 = s.split(' OR ')
    mem[var] = getval(x1) | getval(x2)
    return mem[var]
    
  if 'LSHIFT' in s:
    x1,d = s.split(' LSHIFT ')
    mem[var] = getval(x1) << int(d)
    return mem[var]
    
  if 'RSHIFT' in s:
    x1,d = s.split(' RSHIFT ')
    mem[var] = getval(x1) >> int(d)
    return mem[var]
    
  if 'NOT' in s:
    wert = s.replace('NOT ','')
    mem[var] = eval(str(getval(wert)) + '^ 6553')
    return mem[var]
    
  mem[var] = getval(s)
  return mem[var]
  
ans = getval('a')
print('Answer 1 :',ans)

mem = {}
mem['b'] = ans
print('Answer 2:',getval('a'))




