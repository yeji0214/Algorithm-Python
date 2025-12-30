def solution(n, left, right):
    ans = []
    
    for k in range(left, right + 1):
        i, j = k // n, k % n
        ans.append(max(i+1, j+1))
        
    return ans