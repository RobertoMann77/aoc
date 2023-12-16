
#https://www.reddit.com/r/adventofcode/comments/18hbbxe/2023_day_12python_stepbystep_tutorial_with_bonus/
 
import functools

output = 0

@functools.lru_cache
def calc(record,groups):
	next_character = record[0]
	next_group = groups[0]

	def pound():
		return 0

	def dot():
		return 0

	if next_character == '#':
		out = pound()

	if next_character == '.':
		out = dot()

	elif next_character == '?':
		out = dot() + pound()
	else:
		raise RuntimeError
	print(record,groups,'->',out)
	return out


data = [i.strip() for i in open('t.in')]
for line in data:
 	record, raw_groups = line.split()
 	groups = [int(i) for i in raw_groups.split(',')]
 	output += calc(record,tuple(groups))
 	print(10*'-')

print('>>>',output,'<<<')