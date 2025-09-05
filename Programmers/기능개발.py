def solution(progresses, speeds):
    answer = []
    
    while len(progresses) > 0:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0) # 처음에 이 친구를 빼먹어서 틀림
            cnt += 1
                
        if cnt > 0:
            answer.append(cnt)
        
    return answer