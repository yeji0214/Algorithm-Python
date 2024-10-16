from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
nums = list(map(int, input().split()))

print(bisect_right(nums, x) - bisect_left(nums, x))