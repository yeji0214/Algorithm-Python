N, m, M, T, R = map(int, input().split())
exercise = 0
time = 0
heart = m

if M - m < T:
    print(-1)
    exit(0)

while exercise < N:
    if heart + T <= M:
        heart += T
        exercise += 1
    else:
        heart -= R
        if (heart < m): 
            heart = m
    time += 1

print(time)