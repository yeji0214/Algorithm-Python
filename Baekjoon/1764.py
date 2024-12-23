N, M = map(int, input().split())

unheard = []
unseen = []

for _ in range(N):
    unheard.append(input())

for _ in range(M):
    unseen.append(input())

people = sorted(list(set(unheard) & set(unseen)))

print(len(people))
print(*people, sep='\n')