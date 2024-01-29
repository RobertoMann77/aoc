data=open('t.in').read().split('\n')

#create map
R = len(data)
C = len(data[0])
map=[]
for i in range(R):
    line=[]
    for j in range(C):
        x = data[i][j]  
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

dr = (-1,+1,0,0)
dc = (0,0,-1,1)
count=0
while E not in now:
    r = now.pop(0)    
    for n in range(4):
        if 0 <= (r[0] + dr[n]) < R and 0 <= (r[1] +dc[n]) < C:
            if ord(map[r[0]+dr[n]][r[1]+dc[n]]) - ord(map[r[0]][r[1]]) < 2:
                if (r[0]+dr[n],r[1]+dc[n]) not in visited:
                    now.append((r[0]+dr[n],r[1]+dc[n]))
                visited.append((r[0]+dr[n],r[1]+dc[n]))
    count+=1
print('Answer 1: ',count)
