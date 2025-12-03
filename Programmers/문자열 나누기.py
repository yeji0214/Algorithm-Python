def solution(s):
    answer = 0
    
    while s:
        x = s[0]
        same = 0
        different = 0
        
        for i in range(len(s)):
            if s[i] == x:
                same += 1
            else:
                different += 1
            if same == different:
                answer += 1
                if i < len(s) - 1:
                    s = s[i + 1:]
                else:
                    s = ''
                break
                
        if same != different:
            answer += 1
            break
        
    return answer