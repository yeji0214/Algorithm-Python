N = int(input())
scores = []

for _ in range(N):
    score = input()
    if score == '100':
        scores.append(100)
    else:
        new_score = ''
        for s in score:
            if s == '0' or s == '6':
                new_score += '9'
            else:
                new_score += s
        scores.append(int(new_score))

ans = sum(scores) / N

if ans - int(ans) == 0.5:
    print(int(ans) + 1)
else:
    print(round(ans))