T = int(input())
people = [[0] * 15 for _ in range(15)]

for i in range(1, 15):
    people[0][i] = i

for i in range(1, 15):
    for j in range(1, 15):
        people[i][j] = sum(people[i - 1][:j + 1])

for _ in range(T):
    k = int(input())
    n = int(input())

    print(people[k][n])