# def solution(n):
#     ans = 1
#     stack = [1]
#     num = 1

#     while num != n:
#         if sum(stack) == n:
#             ans += 1
#             stack.pop(0)
#         elif sum(stack) > n:
#             stack.pop(0)
#         else:
#             num += 1
#             stack.append(num)
            
#     return ans

# print(solution(15))


def solution(n):
    s, e = 0, 0
    ans = 0
    arr = [i for i in range(1, n + 1)]

    while s <= e and e < n:
        res = sum(arr[s:e + 1])

        if res == n:
            ans += 1
            e += 1
            s += 1
        elif res < n:
            e += 1
        else:
            s += 1

    return ans

print(solution(15))