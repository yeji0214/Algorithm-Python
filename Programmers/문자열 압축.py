# 무조건 제일 앞부터 정해진 길이만큼 잘라야 함 !
def solution(s):
    answer = len(s)
    
    for i in range(1, len(s) // 2 + 1):
        count = 1
        sZip = ''

        for index in range(0, len(s), i):
            now = s[index:index + i]
            next = s[index + i:index + 2 * i]

            if now == next:
                count += 1

            else:
                if count == 1:
                    sZip += now
                else:
                    sZip += str(count) + now

                now = next
                count = 1

        answer = min(answer, len(sZip))
        
    return answer

print(solution("aabbaccc"))