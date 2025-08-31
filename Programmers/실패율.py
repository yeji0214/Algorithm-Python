# def solution(N, stages):
#     answer = {}
#     player = len(stages)

#     for i in range(1, N + 1):
#         if player != 0:
#             fail = stages.count(i)
#             answer[i] = fail / player
#             player -= fail
#         else:
#             answer[i] = 0
#     return sorted(answer, key=lambda x: answer[x], reverse=True)

def solution(N, stages):
    result = {}
    total = len(stages)
    
    for i in range(1, N + 1):
        count = stages.count(i)
        
        if total == 0:
            result[i] = 0
        else:
            result[i] = count / total
            
        total -= count
        
    return [k for k, v in sorted(result.items(), key=lambda item: (-item[1], item[0]))]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
