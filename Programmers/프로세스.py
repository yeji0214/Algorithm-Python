def solution(priorities, location):
    process = []
    ans = []
    
    for i in range(len(priorities)):
        process.append([i, priorities[i]])

    while process:
        p = process.pop(0)
        
        if p[1] == max(priorities):
            ans.append(p[0])
            priorities.remove(p[1])
        else:
            process.append(p)
            
    return ans.index(location) + 1