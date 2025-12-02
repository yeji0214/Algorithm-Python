def solution(s, skip, index):
    answer = ''

    for S in s:
        nex_idx = ord(S)
        for i in range(1, index + 1):
            nex_idx += 1
            if nex_idx > 122:
                nex_idx = (nex_idx % 122) + 96
            while chr(nex_idx) in skip:
                nex_idx += 1
                if nex_idx > 122:
                    nex_idx = (nex_idx % 122) + 96

        answer += chr(nex_idx)
    
    return answer

print(solution("aukks", "wbqd"	, 5))