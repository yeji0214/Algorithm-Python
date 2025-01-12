while True:
    n = int(input())
    nums = []
    if n == -1:
        exit(0)
    
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            nums.append(i)

    if sum(nums) == n:
        str_nums = map(str, nums)
        result = ' + '.join(str_nums)
        print(str(n) + ' = ' + result)
    else:
        print(str(n) + ' is NOT perfect.')