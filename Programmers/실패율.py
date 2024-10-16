def solution(N, stages):
    answer = {}
    player = len(stages)

    for i in range(1, N + 1):
        if player != 0:
            fail = stages.count(i)
            answer[i] = fail / player
            player -= fail
        else:
            answer[i] = 0
    return sorted(answer, key=lambda x: answer[x], reverse=True)

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
# print(solution(4, [4,4,4,4,4]))