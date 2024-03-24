# 자료구조, 문자열, 스택
string = input()
explosion = input()
ans = []
last_char = explosion[-1]

for i in string:
    ans.append(i)
    if i == last_char and ''.join(ans[-len(explosion):]) == explosion:
        del ans[-len(explosion):]

if len(ans) == 0:
    print("FRULA")
else:
    print(''.join(ans))