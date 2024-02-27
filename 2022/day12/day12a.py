import colorama
from colorama import Fore

data=open('t.in').read().split('\n')

def printmap():
    for i in range(xmax):
        line=''
        for j in range(ymax):
            if (i,j) in path: 
                line+=Fore.RED+map[i][j]
            elif map[i][j]=='~': line+=Fore.BLUE+map[i][j]
            else: line+=Fore.GREEN+map[i][j]
        print(line)
    print(Fore.WHITE)    

#create mapx
xmax=len(data)
ymax=len(data[0])
map=[]
for i in range(xmax):
    line=[]
    for j in range(ymax):
        x=data[i][j]  
        if ord(x)<ord('a'):        
            if x=='S': 
                S=(i,j)
                line.append('a')
            else: 
                E=(i,j)
                line.append('z')
        else: line.append(x)
    map.append(line)

path=set()
path.add((S[0],S[1]))
printmap()

dx = (-1,+1,0,0)
dy = (0,0,-1,1)
count=0
while (E[0],E[1]) not in path:
    temppath=set()
    for r in path:
        for n in range(4):
            if 0 <= (r[0] + dx[n]) < xmax and 0 <= (r[1] +dy[n]) < ymax:
                if ord(map[r[0]+dx[n]][r[1]+dy[n]]) - ord(map[r[0]][r[1]]) < 2:
                    temppath.add((r[0]+dx[n],r[1]+dy[n]))

    for r in path:
        map[r[0]][r[1]]='~'
        
    count+=1
    path=temppath
    printmap()
print(count)
