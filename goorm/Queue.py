N, K = map(int, input().split())
q = []

for i in range(N):
	cmd = input().split()
	
	if cmd[0] == 'push':
		if len(q) == K:
			print('Overflow')
		else:
			q.append(cmd[1])
	else:
		if len(q) == 0:
			print('Underflow')
		else:
			print(q.pop(0))