def solution(s):
    ans = []
    if 'a' <= s[0] <= 'z':
        ans.append(s[0].upper())
    else:
        ans.append(s[0])

    for i in range(1, len(s)):
        if s[i - 1] == ' ' and 'a' <= s[i].lower() <= 'z':
            ans.append(s[i].upper())
        elif 'A' <= s[i] <= 'Z':
            ans.append(s[i].lower())
        else:
            ans.append(s[i])

    return ''.join(ans)

print(solution("3people unFollowed me"))