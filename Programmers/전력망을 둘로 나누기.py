from collections import deque

def bfs(s, visited, connection):
    q = deque()
    q.append(s)
    visited[s] = True
    res = 1
    
    while q:
        c = q.popleft()
        
        for k in connection[c]:
            if not visited[k]:
                visited[k] = True
                res += 1
                q.append(k)
                
    return res

def solution(n, wires):
    connection = [[] for _ in range(n + 1)]
    answer = n
    
    for w in wires:
        w1, w2 = w[0], w[1]
        connection[w1].append(w2)
        connection[w2].append(w1)
        
    for w in wires:
        w1, w2 = w[0], w[1]
        visited = [False] * (n + 1)
        connection[w1].remove(w2)
        connection[w2].remove(w1)
        
        result = []
        for i in range(1, n + 1):
            if not visited[i]:
                result.append(bfs(i, visited, connection))
                
        answer = min(answer, abs(result[0] - result[1]))
        
        connection[w1].append(w2)
        connection[w2].append(w1)
    
    return answer

print(solution(4, [[1,2],[2,3],[3,4]]))