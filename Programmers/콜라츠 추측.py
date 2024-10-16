def solution(num):
    answer = 0
    while answer < 500:
        if num == 1:
            return answer
        answer += 1
        if num % 2 == 0: # 짝수
            num /= 2
        else: # 홀수
            num *= 3
            num += 1
    return -1

print(solution(6))