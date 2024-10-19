vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    p = input()

    if p == 'end':
        exit(0)

    count_v = 0 # 모음 개수
    continuous_v = 0
    continuous_c = 0
    no = 0
    prev = p[0]

    if prev in vowel:
        count_v += 1
        continuous_v += 1
    else:
        continuous_c += 1

    for i in range(1, len(p)):
        if p[i] in vowel:
            count_v += 1
            if p[i - 1] in vowel:
                continuous_v += 1
            else:
                continuous_v = 1
        else:
            if p[i - 1] not in vowel:
                continuous_c += 1
            else:
                continuous_c = 1

        if p[i - 1] ==  p[i] and p[i] != 'e' and p[i] != 'o':
            no = 1

        if continuous_c >= 3 or continuous_v >= 3:
            no = 1

    if count_v == 0:
        no = 1

    if no == 1:
        print('<' + p + '> is not acceptable.')
    else:
        print('<' + p + '> is acceptable.')