from collections import deque

def solution(maps):
    
    def bfs(start, end):
        q = deque()
        visited = [[float('inf') for _ in range(len(maps[0]))] for _ in range(len(maps))]
        
        dy = [0, 0, 1, -1]
        dx = [1, -1, 0, 0]

        for i in range(len(maps)):
            for j in range(len(maps[0])):
                if maps[i][j] == start:
                    q.append([i, j, 0])
                    visited[i][j] = 0
                    break

            if q:
                break
        
        while q:
            y, x, dis = q.popleft()

            if maps[y][x] == end:
                return dis

            for i in range(len(dy)):
                ny = y + dy[i]
                nx = x + dx[i]

                if (0 <= ny < len(maps)) and (0 <= nx < len(maps[0])):
                    if maps[ny][nx] in ('O', 'L', 'S', 'E') and dis + 1 < visited[ny][nx]:
                        visited[ny][nx] = dis + 1
                        q.append([ny, nx, dis + 1])
        
        return 0
    
    res1 = bfs('S', 'L')
    res2 = bfs('L', 'E') 
    
    if res1 == 0 or res2 == 0:
        return -1
    else:
        return res1 + res2
