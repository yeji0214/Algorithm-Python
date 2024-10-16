# 이진 탐색
def cutter():
    s, e = 1, max(wires)

    while s <= e:
        total = 0 # 만들 수 있는 랜선의 개수
        mid = (s+e) // 2
        for i in wires:
            total += i // mid

        if total < N: # 더 많이 잘라야 함
            e = mid - 1
        else:
            s = mid + 1

    return e

K, N = map(int, input().split())
wires = list(int(input()) for _ in range(K))

print(cutter())