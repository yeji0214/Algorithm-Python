def solution(n, arr1, arr2):
    answer = [''] * n
    binary_arr1 = [[0] * n for _ in range(n)]
    binary_arr2 = [[0] * n for _ in range(n)]
    final_arr = [[''] * n for _ in range(n)]
    
    # arr1 이진수로 변환 후 배열에 저장
    for i in range(n):
        binary_line = list(bin(arr1[i])[2:])
        length = len(binary_line)
        new_line = [0] * (n - length) + binary_line
        binary_arr1[i] = new_line
        
    # arr2 이진수로 변환 후 배열에 저장
    for i in range(n):
        binary_line = list(bin(arr2[i])[2:])
        length = len(binary_line)
        new_line = [0] * (n - length) + binary_line
        binary_arr2[i] = new_line
        
    # 둘을 비교해서 최종 배열 도출
    for i in range(n):
        for j in range(n):
            if binary_arr1[i][j] == '1' or binary_arr2[i][j] == '1':
                final_arr[i][j] = '#'
            else:
                final_arr[i][j] = ' '
                
    for i in range(n):
        answer[i] = ''.join(final_arr[i])

    return answer

print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))