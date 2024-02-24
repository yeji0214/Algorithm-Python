# 구현
from collections import deque

N = int(input())
cards = deque()
result = []

for i in range(1, N+1):
    cards.append(i)

while len(cards) > 1:
    result.append(cards.popleft())
    cards.append(cards.popleft())

result.append(cards.popleft())

print(*result)