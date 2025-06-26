scores = list(map(int, input().split()))
name = ["Soongsil", "Korea", "Hanyang"]

if sum(scores) >= 100:
    print("OK")
else:
    idx = scores.index(min(scores))
    print(name[idx])