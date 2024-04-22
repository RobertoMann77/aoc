a = [2, 4, 6, 8]
b = [1, 6, 7, 3]

c = list(zip(a,b))
print(c)

c = [y-x for x,y in(zip(a,a[1:]))]	#deltas from a	

print(c)

print(list(zip(b, b[1:])))
delta = [y - x for x, y in zip(b, b[1:])]
print(delta)