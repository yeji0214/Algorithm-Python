N = int(input())
S = list(map(int, input().split()))
scores = []

prev = S[0]
for i in range(N):
	s = i
	e = s
	
	while e < N - 1 and S[e] + 1 == S[e+1]:
		e += 1
		
	scores.append(sum(S[s:e+1]))
	
print(max(scores))