def solution(X, Y):
    pair = []
    dic = {}
    
    for y in Y:
        dic[y] = dic.get(y, 0) + 1   
    
    for x in X:
        if dic.get(x, 0) > 0:
            pair.append(x)
            dic[x] -= 1
                
    if not pair:
        return "-1"
    
    pair.sort(reverse=True)

    if pair[0] == "0":
        return "0"
    return ''.join(pair)