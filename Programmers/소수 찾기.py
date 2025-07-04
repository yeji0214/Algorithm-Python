import math

def solution(n):
    answer = 0
    for i in range(2, n + 1):
        no = False
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                no = True
                break
        if not no:
            answer += 1
            
    return answer