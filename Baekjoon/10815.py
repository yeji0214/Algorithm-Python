# 정렬, 이진 탐색
N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
nums = list(map(int, input().split()))
ans = []

for n in nums:
    s, e = 0, len(cards) - 1

    while s <= e:
        mid = (s + e) // 2
        if n == cards[mid]:
            ans.append(1)
            break
        elif n < cards[mid]:
            e = mid - 1
        else:
            s = mid + 1
    else:
        ans.append(0)

print(*ans)