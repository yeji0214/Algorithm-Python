w1 = input()
w2 = input()
remove = 0

for w in w1:
    if w in w2:
        idx = w2.find(w)
        if idx == 0:
            w2 = w2[1:]
        elif idx == len(w2) - 1:
            w2 = w2[0:len(w2) - 1]
        else:
            w2 = w2[0:idx] + w2[idx + 1:]
    else:
        remove += 1

print(remove + len(w2))