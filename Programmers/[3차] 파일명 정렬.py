# 각 문자열을 HEAD / NUMBER / TAIL로 쪼개기
# HEAD: 첫 문자부터 숫자가 나오기 전까지
# NUMBER: 숫자가 끝날때까지
# TAIL: 나머지

# HEAD 기준 정렬 (대소문자 구분 X)
# NUMBER 기준 정렬
# 정렬된 배열들의 각 문자열 배열을 합쳐서 새 배열에 넣기

# 정렬을 어떻게 하지? 이차원 배열로?
# ex) [['foo', '9', '.txt']]

def solution(files):
    answer = []
    
    for file in files:
        head, number, tail = '', '', ''

        for i in range(len(file)):
            if file[i].isdigit():
                number += file[i]
            elif not number:
                head += file[i]
            else:
                tail += file[i:]
                break
                
        answer.append([head, number, tail])
        
    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
    
    return [''.join(s) for s in answer]