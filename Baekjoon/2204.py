while True:
    n = int(input())
    if n == 0:
        exit(0)
    words = []

    for _ in range(n):
        s = input()
        if len(words) > 0 and words[0].lower() > s.lower():
            words.insert(0, s)
        else:
            words.append(s)

    print(words[0])