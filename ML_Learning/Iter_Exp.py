import sys

x = iter([1, 9, 3, 4])
# x = [1, 2, 3]
y = (i ** 2 for i in x)
print(next(y))
print(sys.getsizeof(y))
print(next(y))
