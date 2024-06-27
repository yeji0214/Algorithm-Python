# 이진탐색
def cutter():
    s = 0
    e = max(rice_cake)
    result = 0

    while s <= e:
        total = 0
        mid = (s + e) // 2
        for i in rice_cake:
            if i > mid:
                total += i - mid

        if total >= M: # M 이상인 경우 (더 길게 잘라보기)
            result = mid
            s = mid + 1
        else: # M 미만인 경우 (더 짧게 잘라보기)
            e = mid - 1

    return result
    

N, M = map(int, input().split())
rice_cake = list(map(int, input().split()))

print(cutter())