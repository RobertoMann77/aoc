p = 'hepxcrrq'

def check(z):
  r1 = 0
  r2 = 0
  r3 = 0
  found = []

  for i in range(len(z)-3):
    if ord(z[i]) + 1 == ord(z[i+1]) and ord(z[i+1]) + 1 == ord(z[i+2]):  r1 = 1
    if 'i' not in z and 'o' not in z and 'l' not in z: r2 = 1
  for i in range(7):
    if z[i] == z[i+1] and z[i] not in found: 
      found.append(z[i])
  if len(found) > 1: r3 = 1
  if r1 == 1 and r2 == 1 and r3 == 1: return True
  return False

def step(z,n):
  if z[n] != 'z':
    z = z[:n] + chr(ord(z[n])+1) + z[n+1:]
  else:
    z = step(z,n-1)
    z = z[:n] + 'a' + z[n+1:]
  return z

while check(p) == False: p = step(p,7)

ogr('Answer 1:',p)

p = step(p,7)
while check(p) == False: p = step(p,7)

ogr('Answer 2:',p)
