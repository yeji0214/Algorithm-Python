# 구현
T = int(input())

for _ in range(T):
    N = int(input())
    t = list(map(int, input().split()))
    out = [] # 참가 선수가 6명 미만인 팀 번호 저장
    score = {}

    # 6명 미만인 팀 번호 저장
    for i in t:
        if t.count(i) < 6:
            out.append(i)
        else:
            # 점수 초기화
            score[i] = []
    
    current = 1
    for i in t:
        if i not in out:
            score[i].append(current)
            current += 1

    print(sorted(score, key= lambda x: (sum(score[x][0:4]), score[x][4]))[0])