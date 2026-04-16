N = int(input())
ex = {}

for _ in range(N):
    name = input().split(".")[1]
    ex[name] = ex.get(name, 0) + 1

result = list(sorted(ex.items(), key=lambda x: x[0]))

for r in result:
    print(r[0], r[1])