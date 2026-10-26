# def solution(participant, completion):
#     runner = {}
    
#     for p in participant:
#         if p in runner.keys():
#             runner[p] += 1
#         else:
#             runner[p] = 1
            
#     for c in completion:
#         if runner[c] > 1:
#             runner[c] -= 1
#         else:
#             del runner[c]
            
#     return list(runner.keys())[0]

# print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))


def solution(participant, completion):
    player = {}

    for p in participant:
        player[p] = player.get(p, 0) + 1

    for c in completion:
        player[c] -= 1

    for p in player:
        if player[p] == 1:
            return p