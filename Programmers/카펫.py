# def solution(brown, yellow):
#     if yellow == 1:
#         return [3, 3]
    
#     for i in range(1, yellow // 2 + 1):
#         if yellow % i == 0:
#             cw, ch = yellow // i ,i
#             cb = cw * 2 + ch * 2 + 4
#             if cb == brown:
#                 return [cw + 2, ch + 2]


def solution(brown, yellow):
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            j = yellow // i

            if (i + 2) * (j + 2) - yellow == brown:
                return [j + 2, i + 2]

print(solution(24, 24))