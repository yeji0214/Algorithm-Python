def solution(today, terms, privacies):
    terms_info = { k: int(v) for k, v in (item.split() for item in terms) }
    answer = []
    ty, tm, td = map(int, today.split('.'))
    
    for i in range(len(privacies)):
        s, e = privacies[i].split()
        e = terms_info[e]
        y, m, d = map(int, s.split('.'))
        
        if d == 1:
            e -= 1
            next_date = 28
        else:
            next_date = d - 1
            
        ny, nm, nd = y + (m + e - 1) // 12, (m + e - 1) % 12 + 1, next_date
        
        pre = ty * 12 * 28 + tm * 28 + td
        nxt = ny * 12 * 28 + nm * 28 + nd
        
        if pre > nxt:
            answer.append(i + 1)
    
    return answer