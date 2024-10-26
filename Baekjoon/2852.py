N = int(input())

t1 = 0
t2 = 0

t_t1 = 0
t_t2 = 0
f_t1 = 0
f_t2 = 0

max_time = 2880

for _ in range(N):
    num, time = input().split()
    m, s = map(int, time.split(':'))

    if num == '1':
        t1 += 1
    else:
        t2 += 1

    if t1 > t2:
        if f_t1 == 0:
            t_t1 += max_time - (m * 60 + s)
            f_t1 = 1
    elif t2 > t1:
        if f_t2 == 0:
            t_t2 += max_time - (m * 60 + s)
            f_t2 = 1
    else:
        if f_t1 == 1:
            t_t1 -= max_time - (m * 60 + s)
        else:
            t_t2 -= max_time - (m * 60 + s)
        f_t1 = 0
        f_t2 = 0

print('{:02d}:{:02d}'.format(t_t1 // 60, t_t1 % 60))
print('{:02d}:{:02d}'.format(t_t2 // 60, t_t2 % 60))