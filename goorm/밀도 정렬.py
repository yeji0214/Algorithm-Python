N = int(input())
info = [] # 각 물질의 밀도, 무게, 번호 저장

for i in range(N):
	w, v = map(int, input().split())
	info.append([w/v, w, i+1])
	
sorted_info = sorted(info, key=lambda x: (-x[0], -x[1], x[2]))

print(sorted_info[0][2])