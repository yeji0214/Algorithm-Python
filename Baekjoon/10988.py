# 문자열
word = input()

# 방법 1
if word == word[::-1]:
    print(1)
else:
    print(0)

# 방법 2 (그냥 reversed()만 하면 안 되고 join()를 통해 문자열로 재결합해야 함)
if word == ''.join(reversed(word)):
    print(1)
else:
    print(0)