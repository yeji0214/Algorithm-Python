# n = int(input())
# nums = sorted(list(map(int, input().split())))
# x = int(input())

# s = 0
# e = n - 1
# ans = 0

# while s < e:
#     res = nums[s] + nums[e]
#     if res == x:
#         s += 1
#         e -= 1
#         ans += 1
#     elif res < x:
#         s += 1
#     else:
#         e -= 1

# print(ans)

n = int(input())
a = sorted(list(map(int, input().split())))
x = int(input())

s = 0
e = n - 1
ans = 0

while s < e:
    result = a[s] + a[e]
    if result < x:
        s += 1
    elif result > x:
        e -= 1
    else:
        s += 1
        e -= 1
        ans += 1

print(ans)