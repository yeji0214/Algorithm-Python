def solution(arr):
    answer = 0
    
    arr.sort()
    initial = arr[-1]
    num = initial
    mul = 1
    
    while True:
        cnt = 0
        for a in arr:
            if num % a == 0:
                cnt += 1
            else:
                break
        if cnt == len(arr):
            return num
        mul += 1
        num = initial * mul

print(solution([2,6,8,14]))