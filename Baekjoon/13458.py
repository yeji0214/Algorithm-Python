N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

a = [i - B for i in A]
ans = N

for i in a:
    if i > 0:
        ans += i // C
        if i % C != 0:
            ans += 1

print(ans)