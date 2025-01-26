nums = [i for i in range(1, 10001)]

for i in range(1, 10001):
    splitedNum = list(map(int, list(str(i))))
    newNum = i + sum(splitedNum)

    if newNum in nums:
        nums.remove(newNum)

print(*nums, sep='\n')