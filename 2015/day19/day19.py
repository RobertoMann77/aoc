import copy

data = [i.strip() for i in open('t.in')]
mm = data.pop(-1)
data.pop(-1)

def divide(s):
    r = []
    i = 0
    while i<len(s):
        if i+1<len(s):
            if s[i+1].islower():
                r.append(s[i:i+2])
                i += 2
            else:
                r.append(s[i])
                i += 1
        else:
            r.append(s[i])
            i += 1
    return r

rep = {}
for line in data:
    a, b = line.split(' => ')
    if a not in rep:
        rep[a] = [b]
    else:
        rep[a].append(b)

molec = set()

for i in rep:
    for j in rep[i]:
        for k in range(len(mm)):
            if mm[k:].startswith(i):
                molec.add(mm[:k] + j + mm[k+len(i):])

print('Answer 1:', len(molec))

mol = [['e']]
new = [] 
mm = divide(mm)     

c = 0
while mol:
    x = mol.pop()
    for i, a in enumerate(x):
        if a in rep:
            for b in rep[a]:
                n= x[:i] + divide(b) + x[i+1:]
                if len(n) <= len(mm):
                    new.append(n)
    if len(mol) == 0:
        c += 1
        print(c)
        if mm in new:
            print('Answer 2:', c)
        else:
            mol = copy.deepcopy(new)
            new = []
                

