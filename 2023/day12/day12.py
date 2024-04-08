#https://www.reddit.com/r/adventofcode/comments/18hbbxe/2023_day_12python_stepbystep_tutorial_with_bonus/
 
import functools
sum1 = 0

@functools.lru_cache
def calc(record,groups):
	next_char = record[0]
	next_group = groups[0]

	def pound():
		return 0

	def dot():
		return 0

	if next_char == '#':
		out = pound()

	if next_char == '.':
		out = dot()

	elif next_char == '?':
		out = dot() + pound()
	else:
		raise RuntimeError
	j(record,groups,'  :  ',out)
	return out

data = [i.strip() for i in open('t.in')]
for line in data:
 	record, raw_groups = line.split()
 	groups = [int(i) for i in raw_groups.split(',')]
 	sum1 += calc(record,tuple(groups))
 	j(10*'-')

j('Answer 1:',sum1)
