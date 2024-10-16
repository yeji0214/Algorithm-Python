N, K = map(int, input().split())
stack = []

for i in range(N):
	command = input().split()
	if command[0] == 'push':
		if len(stack) >= K:
			print('Overflow')
		else:
			stack.append(command[1])
	else:
		if len(stack) <= 0:
			print('Underflow')
		else:
			print(stack.pop())