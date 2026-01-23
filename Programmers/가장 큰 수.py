def solution(numbers):
    arr = list(map(str, numbers))
    arr.sort(key=lambda x: x*3, reverse=True)
    
    if arr[0] == '0':
        return '0'
    
    return ''.join(arr)