N = int(input())
words = []
ans = []

for _ in range(N):
    words.append(input())

words = list(set(words))

i = 1
while len(ans) < len(words):
    temp = []
    for w in words:
        if len(w) == i:
            temp.append(w)
    ans += sorted(temp)
    i += 1

print(*ans, sep='\n')