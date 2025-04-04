n, m = map(int, input().split())
students = []
question = []

for _ in range(n):
    students.append(list(input().split()))

for _ in range(m):
    question.append(list(input().split()))

for i in range(m):
    ans = 0
    for j in range(n):
        res = 0
        for k in range(3):
            if question[i][k] == students[j][k] or question[i][k] == '-':
                res += 1
        if res == 3:
            ans += 1
    print(ans)