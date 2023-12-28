data = [i.strip() for i in open('15.in')]

# part 1 delete last lien in 7.in. !!!
def pos(t,d):
	(m, n) = d
	return (n + t) % m

disk = {}
for n,line in enumerate(data):
	part = line.split()
	disk[n+1] = (int(part[3]), int(part[11][:-1]))

for t in range(10000000):
	check = 1
	for i in range(1,len(data) + 1):
		if pos(i+t,disk[i]) != 0:
			check = 0
	if check == 1:
		print(t)
		break