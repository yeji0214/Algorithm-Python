time = []

for _ in range(4):
    time.append(int(input()))

print(sum(time) // 60)
print(sum(time) % 60)