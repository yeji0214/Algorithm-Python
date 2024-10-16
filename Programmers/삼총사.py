from itertools import combinations

def solution(number):
    answer = 0
    
    students = list(combinations(number, 3))
    
    for s in students:
        if sum(s) == 0:
            answer += 1
    return answer