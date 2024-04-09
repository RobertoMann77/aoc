data = [i.strip() for i in open('25.in')]

trans = {'1' : 1,
         '2' : 2,
         '0' : 0,
         '-' : -1,
         '=' : -2}

def calc(s):
    z = 0
    for j in range(1, len(s) + 1):
        z += trans[s[-j]] * 5**(j-1)
    return z

def back(z):
    for a, b in trans.items():
        if b == z:
            return a
erg = 0
for line in data:
    erg += calc(line)    

c = 0
y = 1
while y < erg:
    y *= 5
    c += 1

digit = ['=', '-', '0', '1', '2']
ans = []
for k in range(c):
    ans += '='

z = ''
for t in range(c):
    n = c - t - 1
    ans[t] = digit[(erg - calc(ans))//5**n]

g = ''
for r in ans:
    g += r
print('Answer: ', g)
