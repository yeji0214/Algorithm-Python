N = int(input())
pattern = input().split('*')

for _ in range(N):
    file = input()

    p1 = pattern[0]
    p2 = pattern[1]

    if len(p1) + len(p2) > len(file):
        print("NE")
        continue
    if p1 in file and p2 in file and file.index(p1) == 0 and file.rfind(p2) == (len(file) - len(p2)):
        print("DA")
    else:
        print("NE")