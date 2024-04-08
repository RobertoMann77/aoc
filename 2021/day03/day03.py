import copy
data = [i.strip() for i in open('3.in')]
gamma = ''
epsilon = ''

for a in range(len(data[0])):
    mcb = 0 
    for b in range(len(data)):
        if data[b][a] == '1':
            mcb += 1
    if mcb > len(data) // 2:
        gamma += '1'
    else:
        gamma += '0'

for i in range(2,len(gamma)):
    if gamma[i] == '1':
        epsilon += '0'
    else:
        epsilon += '1'

print('Answer 1: ', int(epsilon,2) * int(gamma,2))
temp = copy.deepcopy(data)

a = -1 
while len(temp) > 1:
    a += 1
    mcb = 0
    for b in range(len(temp)):
        if temp[b][a] == '1':
            mcb += 1

    if mcb * 2  >= len(temp):
        erg = '1'
    else:
        erg = '0'
    new = []
    while temp:
        test = temp.pop()
        if test[a] == erg:
            new.append(test)
    temp = copy.deepcopy(new)
ogr = int(temp[0],2)

temp = copy.deepcopy(data)
a = -1 

while len(temp) > 1:
    a += 1
    mcb = 0
    for b in range(len(temp)):
        if temp[b][a] == '1':
            mcb += 1
    if mcb * 2 < len(temp):
        erg = '1'
    else:
        erg = '0'
    new = []
    while temp:
        test = temp.pop()
        if test[a] == erg:
            new.append(test)
    temp = copy.deepcopy(new)
co2 = int(temp[0],2)
print('Answer 2: ',ogr * co2)
