S_len, E_len = map(int, input().split())
S = input()
E = input()

while S in E:
	E = E.replace(E[E.find(S):E.find(S)+S_len], "")

if E == "":
	print("EMPTY")
else:
	print(E)