t = int(input())

for _ in range(t):
    n = int(input())
    clothes = {}
    ans = 1

    for i in range(n):
        name, category = input().split()
        if category not in clothes.keys():
            clothes[category] = [name]
        else:
            clothes[category].append(name)

    for v in clothes.values():
        ans *= (len(v) + 1)

    print(ans - 1)