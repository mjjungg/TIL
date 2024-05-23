from collections import deque

def solution(maps):
    answer = []  
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    visited = [[-1 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            q = deque()
            
            if maps[i][j] != 'X' and visited[i][j] == -1:
                q.append([i, j])
                visited[i][j] = 0
                tmp = 0
                
                while q:
                    y, x = q.popleft()
                    tmp += int(maps[y][x])
                    
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        
                        if (0 <= ny < len(maps)) and (0 <= nx < len(maps[0])):
                            if maps[ny][nx] != 'X' and visited[ny][nx] == -1:
                                q.append([ny, nx])
                                visited[ny][nx] = 0
                if 0 < tmp:
                    answer.append(tmp)
                    
    if len(answer) == 0:
        return [-1]
    
    answer.sort()
    
    return answer
