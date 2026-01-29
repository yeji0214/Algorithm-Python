def solution(sequence, k):
    s = e = 0
    answer = [0, len(sequence)]
    result = sequence[0]
    
    while True:
        if result < k:
            e += 1
            if e == len(sequence):
                break
            result += sequence[e]
        else:
            if result == k:
                if e - s < answer[1] - answer[0]:
                    answer = [s, e]
            result -= sequence[s]
            s += 1
            
    return answer

print(solution([1, 2, 3, 4, 5], 7))