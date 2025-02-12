import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    num = 1
    for _ in range(b):
        num *= a
        num %= 10
    if num == 0:
        print(10)
    else:
        print(num)