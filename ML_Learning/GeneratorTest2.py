# def reverse_str(my_str):
#     for st in range(len(my_str) - 1, -1, -1):
#         yield my_str[st]
#
#
# for ch in reverse_str('Arun'):
#     print(ch)

# my_list = [1, 2, 3, 4, 5]
# y = [x**x for x in my_list]
# z = (x**x for x in my_list)
# print('The values in y are:', y)
# print('The values in z are:', next(z))
# print('The values in z are:', next(z))
# # print('The maximum value in the list is:', max(z))
# print('The values in z are:', next(z))
# print('The values in z are:', next(z))
# print('The values in z are:', next(z))
# print('The values in z are:', next(z))


def all_even():
    n = 0
    while True:
        yield n**n
        n = n+10


x = all_even()
while True:
    print(next(x))
