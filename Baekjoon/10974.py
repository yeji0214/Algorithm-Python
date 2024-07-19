from itertools import permutations

N  = int(input())
lst = []

for i in range(1, N+1):
    lst.append(i)

for p in permutations(lst):
    print(*p)