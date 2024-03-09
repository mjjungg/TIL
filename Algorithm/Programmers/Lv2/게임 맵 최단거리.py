from collections import deque 

def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])
    
    q = deque()
    visited = [[0 for _ in range(m)] for _ in range(n)]
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    
    q.append([0, 0, 1])
    visited[0][0] = 1
    
    while q:
        y, x, cost = q.popleft()
        
        if y == n - 1 and x == m - 1:
            answer = cost
            break
            
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if (0 <= ny < n) and (0 <= nx < m):
                if maps[ny][nx] == 1 and visited[ny][nx] == 0:
                    q.append([ny, nx, cost+1])
                    visited[ny][nx] = 1
    return answer
