N = int(input())
p = list(map(int, input().split()))
questions = []
ans = 0

for _ in range(N):
    questions.append(list(map(int, input().split())))

# [0]으로 오름차순 정렬 -> [1]로 오름차순 정렬
sorted_questions = sorted(questions, key=lambda x: (x[0], x[1]))

for i in range(1, 6):
    current_list = [x for x in sorted_questions if x[0] == i][:p[i-1]] # 걸리는 시간이 적은 애들만 데려오기 (앞에서부터 데려오기)
    for c in range(len(current_list)):
        ans += current_list[c][1]
        if c < len(current_list) - 1:
            ans += current_list[c+1][1] - current_list[c][1]
    if i < 5:
        ans += 60
        
print(ans)