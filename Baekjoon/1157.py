sentence = input().upper()
deduplicated_sentence = list(set(sentence))
a = {}

for s in deduplicated_sentence:
    a[s] = sentence.count(s)
    res = [key for key, value in a.items() if value == max(a.values())]

if len(res) > 1:
    print('?')
else:
    print(*res)