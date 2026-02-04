# # 큐
# n, w, L = map(int, input().split())
# a = list(map(int, input().split()))

# q = [0] * w
# time = 0

# while q:
#     time += 1
#     q.pop(0)
#     if a:
#         if sum(q) + a[0] <= L:
#             q.append(a.pop(0))
#         else:
#             q.append(0)

# print(time)

n, w, L = map(int, input().split())
A = list(map(int, input().split()))
bridge = [0] * w
time = 0

while A:
    bridge = bridge[1:] + [0]
    if (sum(bridge) + A[0]) <= L and bridge[-1] == 0:
        bridge[-1] = A.pop(0)
    time += 1

while bridge.count(0) < w:
    bridge = bridge[1:] + [0]
    time += 1

print(time)