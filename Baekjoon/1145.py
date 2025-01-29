nums = list(map(int, input().split()))
mn = min(nums)

while True:
    ans = 0
    for a in nums:
        if mn % a == 0:
            ans += 1
        if ans >= 3:
            print(mn)
            exit(0)
    mn += 1