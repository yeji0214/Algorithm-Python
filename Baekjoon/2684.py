P = int(input())

for _ in range(P):
    coin = {'TTT': 0, 'TTH': 0, 'THT': 0, 'THH': 0, 'HTT': 0, 'HTH': 0, 'HHT': 0, 'HHH': 0}
    res = input()

    for i in range(38):
        coin[res[i: i + 3]] += 1

    print(*coin.values())