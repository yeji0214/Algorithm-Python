N = int(input())
users = []

for i in range(N):
    age, name = input().split()
    users.append([int(age), name, i])

users = sorted(users, key=lambda x: (x[0], x[2]))

for user in users:
    print(str(user[0]) + ' ' + user[1])