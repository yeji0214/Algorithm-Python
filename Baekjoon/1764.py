# N, M = map(int, input().split())

# unheard = []
# unseen = []

# for _ in range(N):
#     unheard.append(input())

# for _ in range(M):
#     unseen.append(input())

# people = sorted(list(set(unheard) & set(unseen)))

# print(len(people))
# print(*people, sep='\n')


N, M = map(int, input().split())
unheard = []
unseen = []
ans = []

for _ in range(N):
    unheard.append(input())

for _ in range(M):
    unseen.append(input())

# &는 집합 간의 교집합을 구하는 연산자이기 때문에 set으로 형변환을 해줘야 함
ans = sorted(set(unheard) & set(unseen))
print(len(ans))
print(*ans, sep='\n')