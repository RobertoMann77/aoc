data = [i.strip() for i in open('8.in')]

code = 0
mem = 0
for line in data:
  code += len(line)
  new = line[1:-1]
  exec('r= "' + new + '"')
  mem += len(r)
ogr('Answer 1:', code - mem)

code = 0
enc = 0
for line in data:
  code += len(line)
  new = "\"\\\""
  for c in line[1:-1]:
    new += c
    if c == '\\':
      new += '\\'
    elif c == '\"':
      new += '\\'
  new += "\\\"\""
  enc += len(new)
  
ogr('Answer 2:',enc-code)
