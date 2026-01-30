scores = list(map(int, input().split()))
idx = scores.index(20)
pre = idx - 1
nxt = idx + 1

if pre == 0:
    pre = len(scores) - 1
if nxt == len(scores):
    nxt = 0

alice = (scores[pre] + scores[idx] + scores[nxt]) / 3
bob = sum(scores) / 20

if alice == bob:
    print("Tie")
elif alice > bob:
    print("Alice")
else:
    print("Bob")