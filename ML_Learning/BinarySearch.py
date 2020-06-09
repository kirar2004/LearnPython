import numpy as np

#lis = np.random.randint(0, 100, 20)
lis = [29, 48, 96, 63, 23, 73, 23, 37, 22, 98, 22, 37, 51, 40, 74, 14, 65, 15, 77,  5]
print('The raw list is:\n', lis)
lis.sort()
print('The sorted list is:\n', lis)
print('Length of list is: ', len(lis))
item = np.random.randint(0, len(lis)-1, 1)
item = item[0]
print('Search item is = ', item)

low = 0
high = len(lis)-1
itr = 0
flag = 0
while low <= high:
    itr += 1
    mid = int((low + high)/2)
    if lis[mid] == item:
        flag = 1
        print('The number of iterations is', itr, 'and the item', item, 'found at index', mid)
        break
    elif lis[mid] > item:
        high = mid - 1
    else:
        low = mid + 1
if flag == 0:
    print('The number of iterations is', itr, 'and the item', item, 'could not be found')