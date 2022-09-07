import collections
import sys
from collections import deque

'''
    11559 Puyo Puyo
    
    정말 하루 꼬박 걸려 푼 문제이다.. 구글링을 해봐도 도저히 이해가 안되서 끝까지 붙잡고 풀었다..
    이 문제로 배운 점은 
    1. 알고리즘을 생각할 때, 뭉터기로 생각하지 말고 차근차근 한 개씩 풀어서 생각해보자. 
        블록을 한 칸 씩 미루는 알고리즘을 정말 이해하기 힘들었고, 구현하는데 오래걸렸다. 
        그 이유는, 2칸 이상을 미루려고 할 때 계속 2칸을 뭉쳐서 생각했기 때문이다. 
        다시 생각해봤을 때, 2칸 이상을 미루는 행위는  1칸을 미루고 그 이후에 1칸을 미루는 행위와 같다. 
        따라서 for문을 돌려서 계속 한 칸씩 미루는 로직으로 생각하면 쉬운 문제! 
    
    2. 여러 블록이 동시에 터져야 하는 알고리즘을 작성할 때는 while문을 돌리고, 
       최종 답을 카운트하는 행위를 하나의 블록이 터지는 로직 밖에 빼야 한다는 점 
        이렇게 동시 처리 하는 문제를 꽤 많이 봤지만, 최종 답을 카운트하는 위치는 맨날 헷갈렸다..
        이 문제를 풀면서, 대략적으로 어디에 최종 값 카운트 하는 행위를 위치시켜야하는지 감이 왔다. 


'''


# 블록을 한 개씩 뒤로 미루는 것을 생각해보자. -> 미루려는 블록의 값은 이전 행의 블록의 값으로 바꾸면 된다. 그리고, 제일 위에 .을 삽입하면 끝!
# 단, 이 과정이 뒤에서 부터 진행되어야 함 -> why? 0부터 시작하면, 이전 행의 값이 그 이전 값으로 덮어씌워지기 때문!
# 현재 행에 이전 행의 값을 넣어야 하는데, 이전 행의 값 = 전전 행의 값이 되어버리므로, 뒤에서부터 값을 이전 행의 값으로 바꾼다.
# 여러 개의 블록을 뒤로 미룰 때, 미루려는 블록 중 제일 위 블록부터 한 칸씩 밑으로 미루면 된다.
def down(bomb_lst):
    bomb_lst.sort(key=lambda x: x[1])
    for y, x in bomb_lst:
        for i in range(y, -1, -1):
            board[i][x] = board[i - 1][x]

        # 제일 위에 . 삽입
        board[0][x] = '.'


if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n = 12
    m = 6

    board = []
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    for _ in range(n):
        board.append(list(input()))
    res = 0

    while True:     # 여러 그룹이 동시에 터져야 하기 때문에 while문 사용
        bp = 0    # 모든 탐색을 했을 때, 뭉쳐있는 블록이 4개 미만이면 break
        visited = [[0 for _ in range(m)] for _ in range(n)]
        bomb_lst = []
        for i in range(n):  # 블록이 4개 이상인 경우 탐색
            for j in range(m):
                if board[i][j] != '.' and visited[i][j] == 0:
                    visited[i][j] = 1
                    s = board[i][j]
                    block = 1
                    q = deque()
                    q.append([i, j])
                    tmp = []
                    tmp.append([i, j])

                    while q:
                        y, x = q.popleft()

                        for k in range(4):
                            ny = y + dy[k]
                            nx = x + dx[k]

                            if (0 <= ny < n) and (0 <= nx < m):
                                if board[ny][nx] == s and visited[ny][nx] == 0:
                                    q.append([ny, nx])
                                    visited[ny][nx] = 1
                                    block += 1
                                    tmp.append([ny, nx])

                    if 4 <= block:  # 블록이 4개 이상인 경우, 아래로 떨어저야 하기 때문에 bomb_lst에 해당 블록의 좌표 추가 
                        bp += 1     
                        bomb_lst += tmp   # 여러 그룹이 동시에 터져야 하기 때문에 터지는 좌표 계속해서 추가해야 함! 
                                          # bomb_lst = tmp 는 한 그룹에서 터지는 블록의 좌표이기 때문에 X!!!!  

        if bp < 1:  
            print(res)
            break

        else:
            res += 1
            down(bomb_lst)
