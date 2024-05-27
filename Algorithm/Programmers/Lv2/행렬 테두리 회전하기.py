import copy

def solution(rows, columns, queries):
    answer = []
    board = []
    num = 1
    
    for i in range(1, rows+1):
        lst = []
        for j in range(1, columns+1):
            lst.append(num)
            num += 1
        board.append(lst)
        
    new_board = [i.copy() for i in board]
    
    for q in queries:
        a, b, c, d = q
        a -= 1
        b -= 1
        c -= 1
        d -= 1
        tmp = num
        
        # ->
        for x in range(b+1, d+1):
            new_board[a][x] = board[a][x-1]
            tmp = min(tmp, board[a][x-1])
        
        # ↓
        for y in range(a+1, c+1):
            new_board[y][d] = board[y-1][d]
            tmp = min(tmp, board[y-1][d])
        
        # <-
        for x in range(d-1, b-1, -1):
            new_board[c][x] = board[c][x+1]
            tmp = min(tmp,board[c][x+1])
        
        # ↑
        for y in range(c-1, a-1, -1):
            new_board[y][b] = board[y+1][b]
            tmp = min(tmp, board[y+1][b])
        
        board = [i.copy() for i in new_board]

        answer.append(tmp) 
    
    return answer
