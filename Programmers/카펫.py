def solution(brown, yellow):
    if yellow == 1:
        return [3, 3]
    
    for i in range(1, yellow // 2 + 1):
        if yellow % i == 0:
            cw, ch = yellow // i ,i
            cb = cw * 2 + ch * 2 + 4
            if cb == brown:
                return [cw + 2, ch + 2]