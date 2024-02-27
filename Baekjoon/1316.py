# 구현
# 내 풀이
N = int(input())
ans = 0

def group_sentence(chars, new_word):
    for i in range(len(new_word)):
        if new_word[i] not in chars.keys(): # 처음 발견하는 알파벳인 경우
            chars[new_word[i]] = i
        else: # 기존에 있었던 알파벳인 경우
            if i - chars[new_word[i]] != 1:
                return 0
            else:
                chars[new_word[i]] = i
    return 1

for _ in range(N):
    chars = {}
    new_word = input()

    ans += group_sentence(chars, new_word)

print(ans)

# 더 짧은 풀이

N = int(input())
ans = N

for _ in range(N):
    word = input()
    for i in range(0, len(word) - 1):
        if word[i] == word[i+1]:
            continue
        elif word[i] in word[i+1:]:
            ans -= 1
            break

print(ans)