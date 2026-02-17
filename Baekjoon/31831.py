N, M = map(int, input().split())
stress = list(map(int, input().split()))
ans = 0
current_stress = 0

for s in stress:
    nxt = current_stress + s

    if nxt < 0:
        nxt = 0
    elif nxt >= M:
        ans += 1

    current_stress = nxt

print(ans)