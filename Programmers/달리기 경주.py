def solution(players, callings):
    rank = {name: i for i, name in enumerate(players)}
    
    for name in callings:
        idx = rank[name]
        front = players[idx - 1]
        
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
        
        rank[name] -= 1
        rank[front] += 1
        
    return players