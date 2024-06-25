# 그리디
N = int(input())
time = []

for i in range(N):
    time.append(list(map(int, input().split())))

# 주의! x[1]로만 정렬 ㄴㄴ
# 끝나는 시간이 같은 회의 오름차순 정렬 -> 시작 시간도 오름차순 정렬해줘야 함.
# 시작 시간과 끝 시간이 같은 회의가 존재하기 때문
time = sorted(time, key=lambda x: (x[1], x[0]))

et = time[0][1] # 첫 회의가 끝나는 시간
ans = 1

for i in range(1, N):
    if time[i][0] >= et: # 다음 회의가 첫 회의가 끝나고 나서 시작될 수 있을 때
        ans += 1
        et = time[i][1]

print(ans)