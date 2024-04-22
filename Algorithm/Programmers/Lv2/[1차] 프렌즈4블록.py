def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])
        
    while True:
        flg = 0
        #1. 지워지는 블록이 있는지 탐색
        visited = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                now = board[i][j]
                if now == 'X':
                    continue

                if i+1 < m and j+1 < n:
                    if board[i][j+1] == now and board[i+1][j] == now and board[i+1][j+1] == now:
                        visited[i][j] = 1
                        visited[i][j+1] = 1
                        visited[i+1][j] = 1
                        visited[i+1][j+1] = 1
                        flg = 1
        if flg == 0:
            break

        #2. 지워지는 블록의 개수 세고, 지움 
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 1:
                    answer += 1
                    board[i][j] = 'X'

        # 3. 블록 떨어지기 
        while True:
            moved = 0
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] != 'X' and board[i+1][j] == 'X':
                        board[i+1][j] = board[i][j]
                        board[i][j] = 'X'
                        moved = 1
            if moved == 0:
                break
                
    return answer
