# def sq_num(nums):
#     res = []
#     for i in nums:
#         res.append(i ** 2)
#     return res
#
#
my_num = [1, 2, 3, 4, 5]
# my_res = sq_num(my_num)
#
# print(my_res)

def g_sq_num(nums):
    for i in nums:
        yield i ** 2


g_my_res = g_sq_num(my_num)
print(next(g_my_res))
print(next(g_my_res))
