data = [i.strip() for i in open('t.in')]

trans = {'1' : 1,
         '2' : 2,
         '0' : 0,
         '-' : -1,
         '=' : -2}

def back(z):
    for a, b in trans.items():
        if b == z:
            return a
erg = 0
for line in data:
    for j in range(1, len(line) + 1):
        erg += trans[line[-j]] * 5**(j-1)
j(erg)

c = -1
y = 1
while y < erg:
    y *= 5
    c += 1

j(c)

ans = ''

j(erg//(5**c))
