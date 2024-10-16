def solution(arr):
    idx = arr.index(min(arr))
    arr.pop(idx)

    if len(arr) == 0:
        arr.append(-1)

    return arr

print(solution([4,3,2,1]))