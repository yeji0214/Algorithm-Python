S = input()
suffix = []

for i in range(len(S)):
    suffix.append(S[i:])

print(*sorted(suffix), sep='\n')