def cut(n, current_paper):
    global white, blue
    current_white = current_blue = 0

    if n == 1:
        if current_paper[0][0] == 0:
            current_white += 1
        else:
            current_blue += 1
    else:
        for i in range(n):
            current_white += current_paper[i].count(0)
            current_blue += current_paper[i].count(1)

            if current_white > 0 and current_blue > 0:
                mid = n // 2
                cut(mid, [p[0:mid] for p in current_paper[0:mid]])
                cut(mid, [p[mid:n] for p in current_paper[0:mid]])
                cut(mid, [p[0:mid] for p in current_paper[mid:n]])
                cut(mid, [p[mid:n] for p in current_paper[mid:n]])
                return

    if current_white == 0:
        blue += 1
    else:
        white += 1


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

white = blue = 0

cut(N, paper)

print(white)
print(blue)