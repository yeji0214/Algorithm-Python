N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
nums = list(map(int, input().split()))

for n in nums:
    s = 0
    e = N - 1
    exist = False

    while s <= e:
        mid = (s + e) // 2
        if n < A[mid]:
            e = mid - 1
        elif n > A[mid]:
            s = mid + 1
        else:
            exist = True
            break

    print(1 if exist else 0)