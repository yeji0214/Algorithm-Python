# 구현
N, K = map(int, input().split())
num = list(i for i in range(2, N+1))
ans = []

current_num = num[0]
prime = num[0] # prime의 배수를 지워야 함

while num:
    while current_num <= N:
        if current_num in num:
            ans.append(current_num)
            num.remove(current_num)
        current_num += prime

    if len(num) > 0:
        current_num = num[0]
        prime = num[0]

print(ans[K-1])