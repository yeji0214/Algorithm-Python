import sys
input = sys.stdin.readline
res = ''

name = input().split('-')

for n in name:
    res += n[0]

print(res)