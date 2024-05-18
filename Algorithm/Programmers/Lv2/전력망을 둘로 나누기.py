from collections import deque

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        q = deque()
        visited = [0 for _ in range(n+1)]
        visited[1] = 1
        
        for i in range(len(graph[1])):
            q.append(graph[1][i])
            visited[graph[1][i]] = 1    
        
        while q:
            now = q.popleft()
                
            for k in graph[now]:
                if visited[k] == 0:
                    visited[k] = 1
                    q.append(k)
        
        diff = abs(visited[1:].count(1) - visited[1:].count(0))
        answer = min(answer, diff)
        
        graph[a].append(b)
        graph[b].append(a)
        
    return answer
