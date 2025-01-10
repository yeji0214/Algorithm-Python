x, y, w, h = map(int, input().split())
ans = [x, abs(x - w), y, abs(y - h)]

print(min(ans))