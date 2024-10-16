N = int(input())
straw = sorted(list(int(input()) for _ in range(N)), reverse=True)

for i in range(0, N - 2):
    s1, s2, s3 = straw[i], straw[i + 1], straw[i + 2]

    if s1 < s2 + s3:
        print(sum(straw[i:i+3]))
        exit(0)

print(-1)