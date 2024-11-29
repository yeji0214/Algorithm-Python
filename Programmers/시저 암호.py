def solution(s, n):
    answer = ''
    
    for S in s:
        if 97 <= ord(S) <= 122:
            idx = ord(S) + n
            if idx > 122:
                idx = 97 + (idx - 123)
            answer += chr(idx)
        elif 65 <= ord(S) <= 90:
            idx = ord(S) + n
            if idx > 90:
                idx = 65 + (idx - 91)
            answer += chr(idx)
        else:
            answer += ' '
            
    return answer