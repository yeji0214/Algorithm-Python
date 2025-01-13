K = int(input())

for i in range(1, K + 1):
    scores = sorted(list(map(int, input().split()))[1:], reverse=True)
    gap = 0

    for j in range(len(scores) - 1):
        gap = max(gap, scores[j] - scores[j + 1])

    print("Class " + str(i))
    print("Max " + str(scores[0]) + ", Min " + str(scores[-1]) + ", Largest gap " + str(gap))