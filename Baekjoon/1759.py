# 백트래킹
# 내 풀이
def dfs(n, s, lst):
    if n == L: # 길이가 L인 암호가 만들어진 경우
        ans.append(lst) # 정답 리스트에 추가
        return
    else:
        for i in range(s, C):
            dfs(n+1, i+1, lst+[chars[i]]) # 암호에 알파벳 추가

vowel = ['a', 'e', 'i', 'o', 'u'] # 모음 리스트
chars = [] # 주어지는 문자들
ans = [] # 정답 리스트

L, C = map(int, input().split())
chars = sorted(list(input().split())) # 정렬

dfs(0, 0, [])

for i in range(len(ans)):
    vowel_count = 0
    consonant_count = 0

    for j in ans[i]:
        if j in vowel: # 모음의 개수 체크
            vowel_count += 1
        else: # 자음의 개수 체크
            consonant_count += 1
    if vowel_count < 1 or consonant_count < 2: # 모음이 1개 미만이거나, 자음이 2개 미만인 경우
        ans[i] = "" # 임의로 삭제
    
for i in ans:
    if i != '': # 빈 문자가 아닌 경우 정답
        print(*i, sep='')


# 다른 풀이
def dfs(n, vowel_count, str):
    if n == C: # 모든 알파벳의 사용여부 선택 완료
        if len(str) == L and vowel_count >= 1 and L - vowel_count >= 2:
            ans.append(str)
        return
    
    # 포함하는 경우
    dfs(n+1, vowel_count + table[ord(chars[n])], str+chars[n])
    # 포함하지 않는 경우
    dfs(n+1, vowel_count, str)

L, C = map(int, input().split())
chars = sorted(input().split()) # 정렬

# lookup table (모음인 경우 1, 자음인 경우 0)
table = [0] * 128
for i in "aeiou":
    table[ord(i)] = 1

ans = []

dfs(0, 0, "") # index, 모음의 개수, 완성된 암호 문자열

for i in ans:
    print(i)