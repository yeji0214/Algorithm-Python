# 문자열
document = input()
word = input()
s = 0
ans = 0

while s + len(word) <= len(document):
    current_document = document[s:]
    if word in current_document:
        s += current_document.index(word) + len(word) # 겹치지 않는 다음 인덱스로 시작 위치 변경
        ans += 1
    else:
        break

print(ans)