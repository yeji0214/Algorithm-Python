def solution(strings, n):
    answer = []
    dic = {}
    
    for s in strings:
        dic[s] = s[n]
        
    answer = list(dict(sorted(dic.items(), key=lambda x: (x[1], x[0]))).keys())
        
    return answer