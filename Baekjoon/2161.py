# 구현
from collections import deque

N = int(input())
cards = deque()
result = []

for i in range(1, N+1):
    cards.append(i)

# 카드가 한 장 남을 때까지 반복
while len(cards) > 1:
    result.append(cards.popleft()) # 제일 위에 있는 카드를 버린다
    cards.append(cards.popleft()) # 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다

result.append(cards.popleft()) # 마지막 카드

print(*result)