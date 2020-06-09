def local():
    print('The file OOP2 is being executed directly')


def non_local():
    print('The file OOP2 is being executed indirectly')


print('This will always run!!')

if __name__ == '__main__':
    local()
else:
    non_local()
