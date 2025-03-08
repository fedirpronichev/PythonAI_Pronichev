def min(args):
    min = args[0]
    for num in args:
        if min > num:
            min = num
            return min


num_list = list(map(float, input().split()))
print(min(num_list))