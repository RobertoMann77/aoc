data = [i.strip() for i in open('6.in')]
    
mapsize=1000

map1=[[0 for j in range(mapsize)] for i in range(mapsize)]
map2=[[0 for j in range(mapsize)] for i in range(mapsize)]

#decode data corners: u1,u2 and v1,v2
for x in data:
  a,b=x.split(' through ')
  c,u2=a.split(',')
  g=c.split() 
  u1=g.pop()
  if g[0]=='turn': 
    task=g[1]
  else: task=g[0] 

  v1,v2=b.split(',')
  u1,u2,v1,v2=[int(x) for x in [u1,u2,v1,v2]]  

#gridchange lamp by lamp
  for s in range(u1,v1+1):
    for t in range(u2,v2+1):
      if task=='on': 
        map1[s][t]=1
        map2[s][t]+=1
      elif task=='off': 
        map1[s][t]=0
        if map2[s][t]>0: map2[s][t]-=1
      elif task=='toggle':
        if map1[s][t]==1: map1[s][t]=0
        elif map1[s][t]==0: map1[s][t]=1
        map2[s][t]+=2

#counting lights
lightcount1=0
for i in range(mapsize):
  lightcount1+=map1[i].count(1)

lightcount2=0
for i in range(mapsize):
  for j in range(mapsize):  
    lightcount2+=map2[i][j]

print('Answer 1: ',lightcount1)
print('Answer 2: ',lightcount2)