data = [i.strip() for i in open('1.in')]
f = 0
for line in data:
    f = eval('f' + line)
print('Answer 1:', f)


w = []
f = 0
found = 0
while found == 0: 
    for line in data:
        f = eval('f' + line)
        w.append(f)
        if len(w) > len(set(w)):
            print('Answer 2:', w[-1])
            found = 1
            break
