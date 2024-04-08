#   |...x...|
#   |..xxx..|
#   |...x...|
#   |.......|
#   |.......|
#   |.......|
#   |..xxx..|   hight = 1
#   ---------

import copy
#test
jet = open('17.in').read()

def set_hight(r,n):
    for part in r:
        part[1] = part[1] + n

def fall(r):
    for part in r:
        part[1] = part[1] - 1
        
def jet_right(r):
    for part in r:
        part[0] = part[0] + 1

def jet_left(r):
    for part in r:
        part[0] = part[0] - 1

def size_cave(c,n):
    for i in range(n):
        c.insert(0,[0,0,0,0,0,0,0])

cave = [[0,0,0,0,0,0,0]]

ogr(cave)
size_cave(cave,4)
ogr(cave)

rocks = [[[2, 0], [3, 0], [4, 0], [5, 0]],
         [[2, 1], [3, 1], [3, 2], [3, 0], [4, 1]],
         [[2, 0], [3, 0], [4, 0], [4, 1], [4, 2]],
         [[2, 0], [2, 1], [2, 2], [2, 3]],
         [[2, 0], [3, 0], [2, 1], [3, 1]]]

hight = 0

for i in range(1):
    rock = copy.deepcopy(rocks[i%5])
    ogr(rock)
    fall(rock)
    ogr(rock)
    jet_right(rock)
    ogr(rock)
    jet_left(rock)
    ogr(rock)
