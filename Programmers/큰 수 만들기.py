def solution(number, k):
    stack = []
    remove = 0
    
    for i in range(len(number)):
        if len(stack) == 0:
            stack.append(number[i])
            continue
        while stack and stack[-1] < number[i] and remove < k:
            stack.pop()
            remove += 1
        stack.append(number[i])
            
    if remove < k:
        for i in range(k-remove):
            stack.pop()
            
    return ''.join(stack)
            