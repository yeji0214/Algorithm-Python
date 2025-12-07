def solution(participant, completion):
    runner = {}
    
    for p in participant:
        if p in runner.keys():
            runner[p] += 1
        else:
            runner[p] = 1
            
    for c in completion:
        if runner[c] > 1:
            runner[c] -= 1
        else:
            del runner[c]
            
    return list(runner.keys())[0]

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))