def solution(lottos, win_nums):
    answer = []
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    match = 0
    unknown = 0
    
    for l in lottos:
        if l in win_nums:
            match += 1
        elif l == 0:
            unknown += 1
            
    answer.append(rank[match + unknown])
    answer.append(rank[match])
    
    return answer