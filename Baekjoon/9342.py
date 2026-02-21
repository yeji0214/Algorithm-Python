T = int(input())
strs = ['A', 'B', 'C', 'D', 'E', 'F']

for _ in range(T):
    s = input()

    if 'A' not in s or s.index('A') > 1:
        print("Good")
    else:
        head = s[0]
        if head not in strs:
            print("Good")
        else:
            res = []
            for i in range(1, len(s)):
                if s[i] not in res:
                    res.append(s[i])

            if res == ['A', 'F', 'C'] or (res == ['F', 'C'] and head == 'A'):
                print("Infected!")
            else:
                print("Good")