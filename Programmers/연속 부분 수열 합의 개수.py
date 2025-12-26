def solution(elements):
    arr = []
    
    for i in range(1, len(elements) + 1):
        for j in range(len(elements)):
            s = j
            e = s + i
            
            if e > len(elements):
                result = sum(elements[s:])
                result += sum(elements[:e % len(elements)])
                arr.append(result)              
            else:
                arr.append(sum(elements[s:e]))
                
    return len(set(arr))

print(solution([7,9,1,1,4]))