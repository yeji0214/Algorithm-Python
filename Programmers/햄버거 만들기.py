def solution(ingredient):
    answer = 0
    h = []
    for i in ingredient:
        h.append(i)
        if h[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                h.pop()

    return answer
        
print(solution([1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 1, 1]))