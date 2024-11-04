T = int(input())

for _ in range(T):
    n = int(input())

    candidates = [0]

    for _ in range(n):
        candidates.append(int(input()))

    number_of_votes = max(candidates)

    winner_count = candidates.count(number_of_votes)

    if winner_count > 1:
        print("no winner")

    else:
        winner_num = candidates.index(number_of_votes)

        if sum(candidates) // 2 < number_of_votes:
            print("majority winner " + str(winner_num))
        else:
            print("minority winner " + str(winner_num))