def f1(n):
    return n*10

a = [2,3,4,5,6,7,8,9]
b = map(f1, a)
#b = list(map(f1, a))
print(b)
print(list(b))

#+++++++++++++++++++++++++++++++++++++++++

r = '23 45 76 44'
s = list(map(int, r.split()))
print(s)

#+++++++++++++++++++++++++++++++++++++++++