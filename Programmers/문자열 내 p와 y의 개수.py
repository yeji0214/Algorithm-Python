def solution(s):
    answer = True
    
    count_p = s.count('p') + s.count('P')
    count_y = s.count('y') + s.count('Y')

    if count_p == count_y:
        return True
    return False

print(solution("pPoooyY"))