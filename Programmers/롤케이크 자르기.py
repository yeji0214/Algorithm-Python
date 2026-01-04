def solution(topping):
    right = {}
    for t in topping:
        right[t] = right.get(t, 0) + 1
    rightKinds = len(right)
    
    left = {}
    leftKinds = 0
    ans = 0
    
    for i in range(len(topping) - 1):
        x = topping[i]
        
        if left.get(x, 0) == 0:
            leftKinds += 1
        left[x] = left.get(x, 0) + 1
        
        right[x] -= 1
        if right[x] == 0:
            rightKinds -= 1
            del right[x]
        
        if rightKinds == leftKinds:
            ans += 1
    
    return ans