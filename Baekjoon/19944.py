N, M = map(int, input().split())

if M > N:
    print("TLE!")
else:
    if M == 1 or M == 2:
        print("NEWBIE!")
    else:
        print("OLDBIE!")