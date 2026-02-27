n = int(input())
switch = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    g, s = map(int, input().split())

    if g == 1:
        i = 1
        while s * i <= n:
            current = switch[s * i - 1]

            if current == 1:
                switch[s * i - 1] = 0
            else:
                switch[s * i - 1] = 1

            i += 1
    else:
        current = switch[s - 1]
        if current == 1:
            switch[s - 1] = 0
        else:
            switch[s - 1] = 1

        start, end = s - 1, s + 1

        while start >= 1 and end <= n:
            if switch[start - 1] == switch[end - 1]:
                s_result = switch[start - 1]
                e_result = switch[end - 1]

                if s_result == 1:
                    switch[start - 1] = 0
                else:
                    switch[start - 1] = 1

                if e_result == 1:
                    switch[end - 1] = 0
                else:
                    switch[end - 1] = 1

                start -= 1
                end += 1

            else:
                break

if len(switch) <= 20:
    print(*switch)
else:
    i = 0
    s, e = 20 * i, 20 * (i + 1)

    while s < len(switch):
        if e <= len(switch):
            print(*switch[s:e])
        elif s < len(switch):
            print(*switch[s:])

        i += 1
        s, e = 20 * i, 20 * (i + 1)