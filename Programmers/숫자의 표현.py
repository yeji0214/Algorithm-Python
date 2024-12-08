def solution(n):
    ans = 1
    stack = [1]
    num = 1

    while num != n:
        if sum(stack) == n:
            ans += 1
            stack.pop(0)
        elif sum(stack) > n:
            stack.pop(0)
        else:
            num += 1
            stack.append(num)
            
    return ans

print(solution(15))