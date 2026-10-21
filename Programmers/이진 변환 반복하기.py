# def solution(s):
#     answer = []
#     time = 0
#     cnt = 0
    
#     while s != '1':
#         time += 1
#         new_s = s.replace('0', '')
#         cnt += len(s) - len(new_s)
#         s = ''.join(list(bin(len(new_s)))[2:])
        
#     answer.append(time)
#     answer.append(cnt)
    
#     return answer

# print(solution("1111111")


def solution(s):
    cnt, zero = 0, 0

    while s != '1':
        cnt_0 = s.count('0')
        zero += cnt_0
        cnt += 1
        s = bin((len(s) - cnt_0))[2:]

    return [cnt, zero]

print(solution("1111111"))