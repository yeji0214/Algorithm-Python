# 그리디
N = int(input())
score = []
ans = 0

for _ in range(N):
    score.append(int(input()))

for i in range(N-1, 0, -1):
    if score[i-1] >= score[i]:
        new_score = score[i] - 1
        ans += score[i-1] - new_score
        score[i-1] = new_score

print(ans)