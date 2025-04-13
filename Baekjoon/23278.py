N, L, H = map(int, input().split())
scores = sorted(list(map(int, input().split())))

if H == 0:
    new_scores = scores[L:]
else:
    new_scores = scores[L:-H]

print(sum(new_scores) / len(new_scores))