N = int(input())
s = []
teacher = 0
ans = 0

for _ in range(N + 1):
    t, w = input().split()
    if w == 'student':
        s.append(t)
    else:
        th, tm = map(int, t.split(":"))
        teacher = th * 60 + tm

sh, sm = map(int, input().split(":"))
start_time = sh * 60 + sm

for i in range(N):
    ch, cm = map(int, s[i].split(":"))
    student = ch * 60 + cm

    if start_time <= student and teacher <= student:
        ans += 1

print(ans)