A, B = map(int, input().split())
ans = 0
i = A

while i <= B:
    ans += 1
    if i % 2 == 1:
        i += 2
    else:
        i += 1

print(ans)