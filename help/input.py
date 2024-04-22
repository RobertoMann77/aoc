#8890
#13468

#4580
#3529
data = [i.strip() for i in open('t.in')]
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#kjherkfhgiuerguioergergubn
data = open('t.in').read().strip()
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

inputs, *blocks = open('t.in').read().split("\n\n")
inputs = list(map(int, inputs.split(":")[1].split()))
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def ggT(n, m):
    if m == 0:
        return n
    return ggT(m, n % m)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# remove duplicate char in string
from collections import OrderedDict
def rem_dup(s): 
    return ''.join(OrderedDict.fromkeys(s))
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Höhenprofil 2dim
import numpy as np
from numpy import unravel_index

map = []
for line in data:
  map.append([int(x) for x in list(line.strip())])
map = np.array(map)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#spaltenweise max werte
print(np.max(map, axis = 0))
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Koordinaten von max und min
min = np.unravel_index(map.argmin(),map.shape)
max = np.unravel_index(map.argmax(),map.shape)
print(min)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




eval(statement)

exec(command)







