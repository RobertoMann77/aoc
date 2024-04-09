cpk = 3469259
dpk = 13170438

cv = 1
sn = 7
cl = 0

while cv != cpk:
    cv = (cv * sn) % 20201227
    cl += 1

erg = 1
for i in range(cl):
    erg = (erg * dpk) % 20201227

print('Answer: ', erg)
