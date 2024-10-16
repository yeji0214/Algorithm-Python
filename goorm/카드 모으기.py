# 타임에러 코드
# N, M = map(int, input().split())
# all_cards = []
# cards = []
# ans = -1

# def card():
# 	global ans
# 	complete = 0
# 	for i in range(M):
# 		all_cards.append(int(input()))
# 		if len(set(all_cards)) == N and complete == 0:
# 			ans = i + 1
# 			complete = 1

# card()
# print(ans)

N, M = map(int, input().split())
all_cards = set()
ans = -1

# 입력을 한 번에 받음
card_inputs = [int(input()) for _ in range(M)]

for i in range(M):
	all_cards.add(card_inputs[i])
	if len(all_cards) == N:
		ans = i + 1
		break

print(ans)