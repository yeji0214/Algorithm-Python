def solution(keymap, targets):
    answer = []
    
    for T in targets:
        ans = 0 # 눌려야 하는 키의 수
        exist = 0 # 찾는 문자가 없는 경우 -1
        for t in T:
            indexes = [] # 찾는 문자가 저장되어 있는 위치들 저장
            for k in keymap:
                indexes.append(k.find(t)) # 찾는 문자의 인덱스 저장
            index = set(indexes) # 중복 제거
            if -1 in index: # 못 찾은 케이스가 있는 경우
                index.remove(-1) # -1 삭제
            if len(index) == 0: # 못 찾은 케이스 밖에 없었던 경우 (찾는 문자가 어디에도 없음)
                answer.append(-1)
                exist = -1 # 찾는 문자가 없음을 표시
                break
            ans += min(index) + 1 # 눌러야 하는 최소 횟수 더하기
        if exist == 0: # 찾는 문자가 있는 경우에만 answer에 ans 추가
            answer.append(ans)
        
    return answer

print(solution(["ABACD", "BCEFD"], ["ABCD","AAHB"]))
print(solution(["AA"], ["B"]))
print(solution(["AGZ", "BSSS"], ["ASA","BGZ"]))
print(solution(["BC"], ["AC", "BC"]))
print(solution(["ABCE"], ["ABDE"]))