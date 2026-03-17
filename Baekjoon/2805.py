# # 이진 탐색
# def cutter():
#     s = 0
#     e = max(trees)
#     height = 0

#     while s <= e:
#         total = 0
#         mid = (s + e) // 2
#         for i in trees:
#             if i > mid:
#                 total += i - mid

#         if total >= M:
#             s = mid + 1
#             height = mid
#         else:
#             e = mid - 1

#     return height

# N, M = map(int, input().split())
# trees = list(map(int, input().split()))

# print(cutter())

def cutting():
    s, e = 1, max(trees)

    while s <= e:
        mid = (s + e) // 2
        total = 0

        for t in trees:
            if t > mid:
                total += (t - mid)

        if total < M:
            e = mid - 1
        else:
            s = mid + 1

    return e

N, M = map(int, input().split())
trees = list(map(int, input().split()))

print(cutting())