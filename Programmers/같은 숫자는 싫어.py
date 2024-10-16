def solution(arr):
    answer = []
    prev = arr[0]
    answer.append(prev)

    for i in range(1, len(arr)):
        if arr[i] != prev:
            prev = arr[i]
            answer.append(prev)
    return answer

print(solution([4,4,4,3,3]))