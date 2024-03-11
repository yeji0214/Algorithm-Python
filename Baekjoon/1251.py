# 문자열, 브루트포스, 정렬
# 내 풀이 (조합 사용)
from itertools import combinations

word = input()
split_length = [x for x in range(len(word)-1)]
split_index = []
split_words = []

for i in combinations(split_length, 2):
    split_index.append(list(i))

for i in range(len(split_index)):
    str1 = word[0:split_index[i][0]+1][::-1]
    str2 = word[split_index[i][0]+1:split_index[i][1]+1][::-1]
    str3 = word[split_index[i][1]+1:][::-1]

    split_words.append(str1+str2+str3)

print(sorted(split_words)[0])

# 다른 풀이
word = input()
split_words = []

for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        str1 = word[:i][::-1]
        str2 = word[i:j][::-1]
        str3 = word[j:][::-1]

        split_words.append(str1+str2+str3)

print(sorted(split_words)[0])