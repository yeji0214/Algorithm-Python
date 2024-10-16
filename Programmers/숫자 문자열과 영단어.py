words = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six':6, 'seven': 7, 'eight': 8, 'nine': 9}
def solution(s):
    answer = s
    for w in words.keys():
        if w in s:
            answer = s.replace(w, str(words[w]))
            s = answer
    return int(answer)

print(solution("123"))