import math

N, A, B = map(int, input().split())
mj, nmj = A, B
subject = []
for _ in range(10):
    subject.append(list(map(int, input().split())))

for i in range(8 - N):
    req_mj = math.ceil((66 - mj) / 3)
    
    mj += subject[i][0] * 3
    nmj += subject[i][0] * 3

    if (6 - subject[i][0]) > 0:
        nmj += min(6 - subject[i][0], subject[i][1]) * 3

if mj >= 66 and nmj >= 130:
    print("Nice")
else:
    print("Nae ga wae")