N, game = input().split()
names = []
player = {'Y': 1, 'F': 2, 'O': 3}

for _ in range(int(N)):
    names.append(input())

print(len(set(names)) // player[game])