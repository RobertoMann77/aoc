data = [i.strip() for i in open('t.in')]

def test(n):
	found = 0
	t = 1
	while found == 0:
		check = 1
		for i in range(1,n):
			if (disk[i][1] + t + i) % disk[i][0]:
				check = 0
		if check == 1:
			return t
		t += 1

disk = {}
for n,line in enumerate(data):
	part = line.split()
	disk[n+1] = (int(part[3]), int(part[11][:-1]))
	
ogr('Answer 1:', test(len(data) + 1))
disk[7] = (11,0)
ogr('Answer 2:', test(len(data) + 2))
