n = int(input())
seat = [['.'] * 20 for _ in range(10)]

for i in range(n):
    s = input()
    s1, s2 = s[0], int(s[1:])

    seat[ord(s1) - ord('A')][s2 - 1] = 'o'

for s in seat:
    print(''.join(s))