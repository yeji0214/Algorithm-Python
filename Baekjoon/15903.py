# 그리디
# 내 풀이
n, m = map(int, input().split())
cards = sorted(list(map(int, input().split())))

for i in range(m):
    new_card = cards[0] + cards[1] # 카드 합체
    cards[0] = cards[1] = new_card
    cards.sort()

print(sum(cards))


# 효율성 good 풀이
import heapq

n, m = map(int, input().split())
cards = list(map(int, input().split()))

heapq.heapify(cards) # 리스트 cards를 heap으로 변환

for _ in range(m):
    card1 = heapq.heappop(cards) # 가장 작은 원소 힙에서 제거 & 결과값으로 리턴
    card2 = heapq.heappop(cards)
    sum_card = card1 + card2
    heapq.heappush(cards, sum_card) # 원소 추가
    heapq.heappush(cards, sum_card)

print(sum(cards))