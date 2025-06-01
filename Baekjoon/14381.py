T = int(input())

for t in range(T):
    N = input()
    new_N = N
    numbers = []
    mul = 1

    while True:
        arr = list(map(int, new_N))
        
        for a in arr:
            if a not in numbers:
                numbers.append(a)

        if len(numbers) == 10:
            print(f"Case #{t + 1}: {new_N}")
            break

        mul += 1
        prev_N = new_N
        new_N = str(int(N) * mul)
        if new_N == prev_N:
            print(f"Case #{t + 1}: INSOMNIA")
            break