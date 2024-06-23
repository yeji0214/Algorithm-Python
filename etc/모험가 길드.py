N = int(input())
adventurer = sorted(list(map(int, input().split())))
group = 0
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in adventurer:
    count += 1
    if count >= i:
        group += 1
        count = 0

print(group)