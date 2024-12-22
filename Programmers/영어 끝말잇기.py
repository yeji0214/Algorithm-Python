def solution(n, words):
    appeared = [words[0]]
    
    endChar = words[0][-1]
    for i in range(1, len(words)):
        if words[i][0] != endChar or words[i] in appeared:
            return [i % n + 1, i // n + 1]
        appeared.append(words[i])
        endChar = words[i][-1]

    return [0, 0]