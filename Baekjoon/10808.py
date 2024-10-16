S = input()
ans = []

for i in range(ord('a'), ord('z')+1):
    ans.append(S.count(chr(i)))

print(*ans)