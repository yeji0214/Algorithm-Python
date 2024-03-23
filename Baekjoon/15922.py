# 2번 코드
N = int(input())#N개의 선분
x = []
y = []

for _ in range(N):
    X, Y = map(int, input().split())
    x.append(X)
    y.append(Y)

pre_s, pre_e = x[0],y[0]
ans = pre_e-pre_s

for i in range(1,N):
    cur_s,cur_e = x[i],y[i]
    if cur_s < pre_e: #현재_s <이전_e -> 둘이 겹치는 부분 존재
        if cur_e < pre_e:#두번째케이스 -> 아예 현재값이 이전값 안에 있는 경우
            continue
        else: #한쪽만 겹치는 경우 
            ans +=  cur_e - pre_e #현재_e - 이전_e 길이 더해줌
    else: #겹치는 부분이 존재하지 않는다면
        ans += cur_e - cur_s #현재선분길이만 더해줌
    pre_s,pre_e = cur_s,cur_e #현재값을 전값으로 업데이트 해줌
print(ans)
