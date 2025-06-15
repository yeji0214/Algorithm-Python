J = input()
N = int(input())
ans = 0

for _ in range(N):
    mbti = input()

    if J == mbti:
        ans += 1

print(ans)