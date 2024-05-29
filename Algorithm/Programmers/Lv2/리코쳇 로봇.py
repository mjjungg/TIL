from collections import deque

def solution(board):
    answer = 0
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    q = deque()
    n = len(board)
    m = len(board[0])
    visited = [[float('inf') for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                q.append([i, j])
                visited[i][j] = 0
                break
        
        if q:
            break
    
    while q:
        y, x = q.popleft()

        if board[y][x] == 'G':
            return visited[y][x]
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            while (0 <= ny < n) and (0 <= nx < m) and (board[ny][nx] != 'D'):
                ny += dy[i]
                nx += dx[i]
            
            end_y = ny - dy[i]
            end_x = nx - dx[i]
            
            if visited[y][x] + 1 < visited[end_y][end_x]:
                    visited[end_y][end_x] = visited[y][x] + 1
                    q.append([end_y, end_x])
                    
    return -1
