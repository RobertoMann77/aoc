data=open('t.in').read().split('\n')

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
        nr = r[0] + dr[n]
        nc = r[1] + dc[n]
        if 0 <= nr < R and 0 <= nc < C:
            if ord(map[nr][nc]) - ord(map[r[0]][r[1]]) < 2:
                if (nr,nc) not in visited:
                    now.append((nr,nc))
                visited.append((nr,nc))
    count+=1
print('Answer 1: ',count)
