# def solution(array, commands):
#     answer = []
    
#     for c in commands:
#         s, e, i = c[0], c[1], c[2]
        
#         answer.append(sorted(array[s-1:e])[i-1])
        
#     return answer

def solution(array, commands):
    ans = []

    for c in commands:
        ans.append(sorted(array[c[0] - 1:c[1]])[c[2] - 1])

    return ans

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))