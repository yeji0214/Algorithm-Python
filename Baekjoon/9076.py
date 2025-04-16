T = int(input())

for _ in range(T):
    score = sorted(list(map(int, input().split())))[1:-1]
    if score[-1] - score[0] >= 4:
        print("KIN")
    else:
        print(sum(score))