from itertools import permutations

def match(n):
    global ans

    for cn, s, b in answers:
        strike = 0
        ball = 0
        for i in range(3):
            if n[i] == cn[i]:
                strike += 1
            elif cn[i] in list(n):
                ball += 1

        if strike != s or ball != b:
            return
    ans += 1

N = int(input())

num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
nums = map(list, permutations(num, 3))
answers = []
ans = 0

for _ in range(N):
    n, s, b = map(int, input().split())
    n = str(n)
    answers.append([n, s, b])

for n in nums:
    match(n)

print(ans)