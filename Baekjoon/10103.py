n = int(input())
c = 100
s = 100

for _ in range(n):
    nc, ns = map(int, input().split())
    if nc < ns:
        c -= ns
    elif nc > ns:
        s -= nc

print(c)
print(s)