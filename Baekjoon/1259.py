while True:
    num = input()
    if num == '0':
        exit(0)
    if num == num[::-1]:
        print('yes')
    else:
        print('no')