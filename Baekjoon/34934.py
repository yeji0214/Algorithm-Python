N = int(input())
dic = {}

for _ in range(N):
    name, year = input().split()

    dic[year] = name

print(dic['2026'])