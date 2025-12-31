def solution(citations):
    for i in range(max(citations), -1, -1):
        temp = citations
        possible = [t for t in temp if t >= i]
        rest = list(set(temp) - set(possible))
        
        if len(possible) >= i and len(rest) <= i:
            return i