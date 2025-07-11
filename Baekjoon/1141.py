# # 그리디
# # 내 풀이
# N = int(input())
# words = []
# ans = 0

# for _ in range(N):
#     words.append(input())

# for i in range(N):
#     for j in range(N):
#         if i == j:
#             continue
#         if words[j].find(words[i]) == 0: # 0일 때 접두사
#             words[i] = ""
        
# for j in words:
#     if j != "":
#         ans += 1

# print(ans)

# # 정렬 사용
# N = int(input())
# words = []
# ans = 0

# for _ in range(N):
#     words.append(input())

# words.sort(key=len)

# for i in range(N):
#     for j in range(i+1, N):
#         if words[j].find(words[i]) == 0: # 0일 때 접두사
#             words[i] = ""
        
# for j in words:
#     if j != "":
#         ans += 1

# print(ans)


###

N = int(input())
sentences = []

for _ in range(N):
    sentences.append(input())

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if sentences[j].find(sentences[i]) == 0:
            sentences[i] = ""

print(N - sentences.count(""))