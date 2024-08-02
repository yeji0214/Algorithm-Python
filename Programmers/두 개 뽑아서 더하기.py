from itertools import combinations

def solution(numbers):
    ans = []
    for c in list(combinations(numbers, 2)):
        ans.append(sum(c))
    ans = set(ans)
    return sorted(ans)