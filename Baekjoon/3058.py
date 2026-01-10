T = int(input())
for _ in range(T):
    nums = list(map(int, input().split()))
    even = []

    for n in nums:
        if n % 2 == 0:
            even.append(n)

    even = sorted(even)
    print(sum(even), even[0])