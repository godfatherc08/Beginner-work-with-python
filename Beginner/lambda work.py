from functools import reduce

point = [1, 2, 3, 4, 5]
b = map(lambda x : x*2, point)
print(list(b))


c = filter(lambda x : x%2 == 0, point)
print(list(c))
