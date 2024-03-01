# 백트래킹
# 내 첫 번째 풀이
# def dfs(n, sIndex, S, lst):
#     if n == 6:
#         ans.append(lst)
#         return
    
#     for i in range(sIndex, k):
#         if S[i] not in lst:
#             dfs(n+1, i+1, S, lst + [S[i]])

# while True:
#     nums = list(map(int, input().split()))
#     ans = []
#     k = nums[0]
#     if k == 0:
#         exit(0)
#     S = sorted(list(nums[1:]))

#     dfs(0, 0, S, [])
#     for j in ans:
#         print(*j)
#     print()

# 좀 더 깔끔하게 수정
def dfs(n, sIndex, lst):
    if n == 6:
        ans.append(lst)
        return
    
    for i in range(sIndex, k):
        dfs(n+1, i+1, lst + [S[i]])

while True:
    nums = list(map(int, input().split()))
    ans = []
    k = nums[0]
    if k == 0:
        break
    S = list(nums[1:])

    dfs(0, 0, [])
    
    for j in ans:
        print(*j)
    print()