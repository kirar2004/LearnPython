def my_print():
    n = 1
    print("The value of n is {}".format(n))
    yield n
    n += 1
    print("The value of n is {}".format(n))
    yield n


# g = my_print()
# next(g)
# next(g)

for item in my_print():
    pass
