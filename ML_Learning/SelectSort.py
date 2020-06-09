lis = [100, 48, 96, 63, 23, 73, 23, 37, 22, 98, 22, 37, 51, 40, 74, 14, 65, 15, 77, 5]

print('The raw list is:\n', lis)
l = len(lis)
for i in range(0, l - 1):
    #print('i=', i)
    for j in range(i + 1, l):
        #print('j=', j)
        if lis[j] < lis[i]:
            temp = lis[j]
            lis[j] = lis[i]
            lis[i] = temp
        else:
            continue
print('The sorted list is:\n', lis)
