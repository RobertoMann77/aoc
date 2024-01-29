data=open('t.in').read().split('\n')

#create map
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

now = []
visited = []
now.append(S)
visited.append(S)

dx = (-1,+1,0,0)
dy = (0,0,-1,1)
count=0
while E not in now:
    r = now.pop(0)    
    for n in range(4):
        if 0 <= (r[0] + dx[n]) < xmax and 0 <= (r[1] +dy[n]) < ymax:
            if ord(map[r[0]+dx[n]][r[1]+dy[n]]) - ord(map[r[0]][r[1]]) < 2:
                if (r[0]+dx[n],r[1]+dy[n]) not in visited:
                    now.append((r[0]+dx[n],r[1]+dy[n]))
                visited.append((r[0]+dx[n],r[1]+dy[n]))
    count+=1
print('Answer 1: ',count)
