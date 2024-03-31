# 구현, 정렬, 시뮬레이션
# 내 풀이
P = int(input())

for _ in range(P):
    lst = list(map(int, input().split()))
    T = lst[0]
    height = lst[1:]
    line_up = [height[0]] # 첫 번째 학생 추가
    ans = 0


    for i in range(1, 20):
        if height[i] > max(line_up): # 자기 앞에 자기보다 키가 큰 학생이 없다면
            line_up.append(height[i]) # 맨 뒤에 추가
        else: # 자기 앞에 자기보다 키가 큰 학생이 있다면
            for j in range(len(line_up)):
                if line_up[j] > height[i]: # 그중 가장 앞에 있는 학생의 바로 앞에 선다
                    ans += len(line_up) - j
                    line_up.insert(j, height[i])
                    break
            
    print(T, ans)

# 다른 풀이 (버블 정렬)
P = int(input())

for _ in range(P):
    lst = list(map(int, input().split()))
    ans = 0

    for i in range(1, len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                ans += 1

    print(lst[0], ans)