def solution(cards1, cards2, goal):
    answer = ''
    c1_idx = 0
    c2_idx = 0
    
    for g in goal:
        if g in cards1:
            idx = cards1.index(g)
            if idx > c1_idx:
                return "No"
            else:
                c1_idx += 1
        else:
            idx = cards2.index(g)
            if idx > c2_idx:
                return "No"
            else:
                c2_idx += 1
            
    return "Yes"