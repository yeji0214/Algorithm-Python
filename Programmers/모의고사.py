def solution(answers):
    answer = [0 for _ in range(3)]
    
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]

    for i in range(0, len(answers)):
        if s1[i % len(s1)] == answers[i]:
            answer[0] += 1
        if s2[i % len(s2)] == answers[i]:
            answer[1] += 1
        if s3[i % len(s3)] == answers[i]:
            answer[2] += 1
            
    result = []
    score = max(answer)
    
    for i in range(len(answer)):
        if answer[i] == score:
            result.append(i + 1)
    
    return sorted(result)