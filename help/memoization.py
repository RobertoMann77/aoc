#https://www.reddit.com/r/adventofcode/comments/18hbbxe/2023_day_12python_stepbystep_tutorial_with_bonus/

import functools
@functools.lru_cache

def fib(x):
	print(x)
	if x == 0: return 0
	elif x == 1: return 1
	return fib(x-1) + fib(x-2)

print(fib(50))
