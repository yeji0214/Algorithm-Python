def solution(babbling):
    pro = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for b in babbling:
        if "ayaaya" in b or "yeye" in b or "woowoo" in b or "mama" in b:
            continue
        b = b.replace("aya", '.')
        b = b.replace("ye", '.')
        b = b.replace("woo", '.')
        b = b.replace("ma", '.')
        
        if b.replace('.', '') == '':
            answer += 1
    
    return answer