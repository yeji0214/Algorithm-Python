# 그리디, 비트마스킹
# 이진수를 이용하여 해결 (생각 못함^^)
# 물을 합칠 때 같은 수(2의 배수)끼리만 합칠 수 있음. 이진수로 변환했을 때 1의 개수가 현재 물병의 개수.
# K보다 큰 경우, 새 물병을 가져와서 합치기

N, K = map(int, input().split())
ans = 0

while bin(N).count('1') > K:
    N += 1
    ans += 1

print(ans)