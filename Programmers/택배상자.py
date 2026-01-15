def solution(order):
    sub = []
    ans = []
    cur = 1
    
    for i in range(len(order)):
        x = order[i]
        while cur <= x:
            sub.append(cur)
            cur += 1
        if x == sub[-1]:
            ans.append(sub.pop(-1))
        else:
            return len(ans)
            
    return len(ans)

print(solution([4, 3, 1, 2, 5]))