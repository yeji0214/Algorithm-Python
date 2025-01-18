n = int(input())

f0 = 0
f1 = 1

if n == 0:
    print(f0)
    exit(0)
elif n == 1:
    print(f1)
    exit(0)

for i in range(2, n + 1):
    f2 = f0 + f1
    f0 = f1
    f1 = f2

print(f2)