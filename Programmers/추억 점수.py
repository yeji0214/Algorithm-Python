def solution(name, yearning, photo):
    answer = []
    
    for i in range(len(photo)):
        missing = 0
        for j in photo[i]:
            if j in name:
                missing += yearning[name.index(j)]
        answer.append(missing)
        
    return answer

# 테케
print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))