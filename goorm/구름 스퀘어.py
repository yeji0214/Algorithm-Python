N = int(input())
time = []
ans = 1

for i in range(N):
	time.append(list(map(int, input().split())))
	
time = sorted(time, key=lambda x: x[1])
s = time[0][1]

for i in range(1, N):
	if time[i][0] > s:
		ans += 1
		s = time[i][1]
		
print(ans)