import numpy as np
import copy
data = [i.strip() for i in open('t.in')]

def look(pos):
    togo = []
    dr = [ 0,  0, -1,  1]
    dc = [-1,  1,  0,  0]
    for n in range(4):
        r = pos[1] + dr[n]
        c = pos[2] + dc[n]
        if 0 <= r < len(M) and 0 <= c < len(M[0]):
            togo.append((pos[0] + M[r][c], r,c))
    return togo

M = []
for row in data:
    r = []
    for char in row:
        r.append(int(char))
    M.append(r)
M = np.array(M)
print(M)

visited = set()
visited = {(0,0) : 0}
#rl  r  c
curr = [(0, 0, 0)]
new = []

while curr:
    c = curr.pop()
    for n in look(c):
        if n not in visited:
            new.append(n)
            print(n)
    if (len(M) - 1, len(M[0] - 1)) in new:
        print('found')
        break
    curr = copy.deepcopy(new)
    new = []

print(new)
