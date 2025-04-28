max_scores = [100, 100, 200, 200, 300, 300, 400, 400, 500]

scores = list(map(int, input().split()))

if sum(scores) < 100:
    print("none")
    exit(0)
for i in range(9):
    if scores[i] > max_scores[i]:
        print("hacker")
        exit(0)
else:
    print("draw")