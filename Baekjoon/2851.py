def mushroom(scores):
    total = 0
    result = []

    for s in scores:
        total += s
        if total >= 100:
            break
    else:
        result.append(total)
        return result

    if total - s <= 100:
        result.append(total - s)
    result.append(total)
    return result

scores = [int(input()) for _ in range(10)]

m = mushroom(scores)

if len(m) == 2:
    if abs(100 - m[0]) < abs(100 - m[1]):
        print(m[0])
    else:
        print(m[1])
else:
    print(m[0])
