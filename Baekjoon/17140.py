r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
time = 0

while time <= 100:
    if r <= len(A) and c <= len(A[0]) and A[r-1][c-1] == k:
        print(time)
        exit(0)

    time += 1
    new_A = []

    if len(A) >= len(A[0]): # 행 정렬
        for R in A:
            dic = {}
            new_R = []
            for i in R:
                if i != 0:
                    dic[i] = R.count(i)
            sorted_data = sorted(dic.items(), key=lambda x: (x[1], x[0]))

            for key, value in sorted_data:
                new_R.append(key)
                new_R.append(value)
            new_A.append(new_R)
            
        mx_len = max(len(row) for row in new_A)
        A = [row + [0] * (mx_len - len(row)) for row in new_A]

    else: # 열 정렬
        for C in list(zip(*A)):
            dic = {}
            new_C = []
            for i in C:
                if i != 0:
                    dic[i] = C.count(i)
            sorted_data = sorted(dic.items(), key=lambda x: (x[1], x[0]))

            for key, value in sorted_data:
                new_C.append(key)
                new_C.append(value)
            new_A.append(new_C)
            
        mx_len = max(len(col) for col in new_A)
        new_A = [col + [0] * (mx_len - len(col)) for col in new_A]

        A = list(map(list, zip(*new_A)))

    A = A[:100]
    A = [row[:100] for row in A]

print(-1)