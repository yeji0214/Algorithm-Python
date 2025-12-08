def solution(n, lost, reserve):
    lost, reserve = set(lost), set(reserve)
    inter = lost & reserve
    
    lost -= inter
    reserve -= inter
    
    lost, reserve = list(lost), list(reserve)
    
    for r in reserve:
        pre, nxt = r-1, r+1
        if pre in lost:
            lost.remove(pre)
        elif nxt in lost:
            lost.remove(nxt)
            
    return n - len(lost)

print(solution(3, [3], [1]))