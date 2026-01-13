def solution(prices):
    stack = []
    result = [0] * len(prices)
    
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
        
    while stack:
        j = stack.pop()
        result[j] = (len(prices) - 1) - j
        
    return result