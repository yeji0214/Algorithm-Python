# 큐
n, w, L = map(int, input().split())
a = list(map(int, input().split()))

q = [0] * w
time = 0

while q:
    time += 1
    q.pop(0)
    if a:
        if sum(q) + a[0] <= L:
            q.append(a.pop(0))
        else:
            q.append(0)

print(time)