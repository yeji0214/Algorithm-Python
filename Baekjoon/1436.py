N = int(input())

num = 666
cnt = 0

while True:
    if '666' in str(num):
        cnt += 1
    if cnt == N:
        print(num)
        exit(0)
    num += 1