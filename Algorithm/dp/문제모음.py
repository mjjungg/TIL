import sys


'''
    9251 LCS

'''

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    s1 = input()
    s2 = input()

    n = len(s1)
    m = len(s2)

    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:  # 맨 끝 글자가 같을 때
                dp[i][j] = dp[i-1][j-1] + 1     # s1, s2에서 각 문자를 추가하기전 값 + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # s1에 문자를 추가하기전 값, s2에 문자를 추가하기 전 값 중 큰 값

    print(dp[-1][-1])


'''
    11054 가장 긴 바이토닉 부분 수열
    
    증가하는 수열 길이 + 리스트 반대로 감소하는 수열 길이의 합이 가장 큰 지점 
    = 바이토닉 수열이면서 가장 긴 수열의 길이
    
    바이토닉 수열 : S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN 
    한 번에 바이토닉 수열 찾을 생각X -> 증가 수열 + 감소 수열 로 쪼개서 생각하기!
'''

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n = int(input())

    lst = list(map(int, input().split()))

    increase = [1 for _ in range(n)]   # 증가하는 수열의 길이가 담긴 리스트
    decrease = [1 for _ in range(n)]   # 반대로 감소하는 수열의 길이가 담긴 리스트
    res = [0 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if lst[j] < lst[i]:
                increase[i] = max(increase[i], increase[j] + 1)


    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            if lst[j] < lst[i]:
                decrease[i] = max(decrease[i], decrease[j] + 1)



    for i in range(n):
        res[i] = increase[i] + decrease[i] - 1  # 중복 숫자빼줘야 해서 -1함

    print(max(res))
    
    
    '''
    11048 
    
    생각의 전환! 다음 위치로 갈 수 있는 경로가 (r+1, c), (r, c+1), (r+1, c+1) 이면,
    현재 위치로 올 수 있는 전 위치는 (r-1, c), (r, c-1), (r-1, c-1) 이다!!!


'''

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n, m = map(int, input().split())

    board = []
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n):
        board.append(list(map(int, input().split())))


    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = board[i-1][j-1] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
            # 현재 위치에 있는 사탕의 개수 + 이전 위치에 있던 사탕의 수 중 max값

    print(dp[n][m])
    
    
'''
    1309 동물원
    
    
    점화식 : 
    N = 2인 곳에 아무것도 배치 x 경우 : dp[i-1] (전과 동일)
    N = 1인 곳에 아무것도 배치 x 경우 : dp[i-2] * 2
    N = 1, 2에 모두 배치 : dp[i-1] - dp[i-2]
    
'''



if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n = int(input())

    dp = [0 for _ in range(n+1)]

    dp[0] = 1
    dp[1] = 3

    for i in range(2, n+1):
        dp[i] = (dp[i-2] + dp[i-1] * 2) % 9901


    print(dp[n])


    
'''
    2631 줄세우기
    
    생각의 전환!!
    순서대로 배치하기 위해 옮겨지는 아이의 최소 수 = n - 최장 수열의 길이  
'''

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n = int(input())
    lst = []
    dp = [1 for _ in range(n)]
    dp[0] = 1
    for _ in range(n):
        lst.append(int(input()))

    for i in range(n):
        for j in range(i):
            if lst[j] < lst[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(dp)
    print(n - max(dp))
    

'''
    16194 카드 구매하기2
    
    dp[n] : 카드를 n개 샀을 때 최소 금액
'''

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n = int(input())
    cards = list(map(int, input().split()))
    cards.insert(0, 0)
    dp = [cards[i] for i in range(n+1)] # dp를 카드 n개가 들어있는 카드팩의 금액으로 초기화 시킴 

    for i in range(1, n+1):
        for j in range(1, i):
            dp[i] = min(dp[i], dp[j] + dp[i-j]) # n개보다 작은 개수의 카드의 최소 금액을 이용해서 카드 n개의 최소 금액 구함

    print(dp[n])
    


'''
    2225 합분해 
    
    n, k를 작은 단위로 나눠서 규칙 찾아본다
    n = 1부터, k = 1부터 테이블을 만들어서 현재 위치에 오는 값을 계산할 수 있는 식(규칙)을 찾는다. 
       
'''

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n, k = map(int, input().split())

    board = [[0 for _ in range(n+1)] for _ in range(k+1)]

    for i in range(1, n+1):
        board[1][i] = 1

    for i in range(2, k+1):
        board[i][1] = i

    for i in range(2, k+1):
        for j in range(2, n+1):
            board[i][j] = board[i-1][j] + board[i][j-1]

    print(board[k][n] % 1000000000)


'''
    4811 알약
    
    이중 테이블 만들어 각각의 경우의 수 생각 -> 규칙 찾아내기 
    dp[i][j] 행 : h의 개수, 열 : w의 개수 
    h는 앞에 w의 개수보다 같거나 적어야 한다. ex) hw, hhw (x) 
   
'''

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    while True:
        n = int(input())
        if n == 0:
            break

        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

        for i in range(1, n+1):
            dp[0][i] = 1

        for i in range(1, n+1):
            for j in range(i, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]


        print(dp[n][n])

        
'''
    2302 극장 좌석
    
    n = 1, 2, 3 ... 작은 문제로 쪼개서 점화식을 찾아본다.
    n = 1 => 경우의 수 : 1
    n = 2 => 12, 21 : 2
    n = 3 => 123, 132, 213 : 3
    n = 4 => 1234, 1324, 2134, 1243, 12143 : 5
    n = 4일 때를 보면, dp[3] + dp[2] 라는 것을 알 수 있다!!! 
    
    vip는 자리가 고정된다 -> 리셋된다고 보면 됨(처음부터 다시 시작)
     -> 동시에 일어나므로 곱함
    
    동시에 일어나면 곱을 해주고, 동시에 일어나지 않으면 덧셈을 해준다.
   
'''

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n = int(input())
    m = int(input())
    res = 1
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    tmp = 0
    for i in range(m):
        vip = int(input())
        res *= dp[vip-tmp-1]
        tmp = vip

    res *= dp[n-tmp]
    print(res)
    
    
'''
        11660 구간 합 구하기5
        
        규칙 찾는 문제!

'''


if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n, m = map(int, input().split())
    board = []
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for _ in range(n):
        board.append(list(map(int, input().split())))

    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + board[i-1][j-1]

    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])

        
'''
        9465
        스티커
        
        규칙 찾기 - 현재 올 수 있는 값 중 최선의 값(최대값) 찾기
        ※ 리스트 마이너스 인덱스를 조심하자! 
        리스트에서 마이너스 인덱스는 에러가 나지 않고 뒤로 돌기 때문에 예외처리 해주어야 한다.

'''


if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    t = int(input())
    for _ in range(t):
        n = int(input())
        board = []
        dp = [[0 for _ in range(n)] for _ in range(2)]

        for _ in range(2):
            board.append(list(map(int, input().split())))

        dp[0][0] = board[0][0]
        dp[1][0] = board[1][0]

        for j in range(1, n):
            if j-2 < 0:
                dp[0][j] = board[0][j] + dp[1][j-1]
                dp[1][j] = board[1][j] + dp[0][j - 1]
            else:
                dp[0][j] = max(board[0][j] + dp[1][j - 1], board[0][j] + dp[1][j - 2])
                dp[1][j] = max(board[1][j] + dp[0][j - 1], board[1][j] + dp[0][j - 2])

        res = 0

        for i in dp:
            if res < max(i):
                res = max(i)
        print(res)

        
'''
        11049 행렬 곱셈 순서
        
        1. n이 4정도 됐을 때의 예를 생각해보자. 
        dp의 점화식을 찾기 위해서 n=1일때부터 규칙을 찾아나갈 수도 있지만, 
        n이 웬만큼 커야(3이나 4정도) 규칙을 찾기 쉬울 때도 있다.
        
        2. 다이아몬드 행렬 구조 파악
        for i in range(1, n):
            for j in range(n-i):
                dp[j][j + i]         
'''


if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n = int(input())
    mat_lst = []
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(n):
        mat = list(map(int, input().split()))
        mat_lst.append(mat)

    for i in range(1, n):
        for j in range(n-i):
            if i == 1:
                dp[j][j + i] = mat_lst[j][0] * mat_lst[j][1] * mat_lst[j + i][1]
                continue

            dp[j][j + i] = 2 ** 32
            for k in range(j, j + i):
                dp[j][j + i] = min(dp[j][j + i],
                                   dp[j][k] + dp[k + 1][j + i] + mat_lst[j][0] * mat_lst[k][1] * mat_lst[j + i][1])

    print(dp[0][n-1])
    
    
'''
    12863 평범한 배낭 
    
    첫 번째 풀이: 시간 초과

'''


if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n, k = map(int, input().split())
    dp = [0 for _ in range(k + 1)]
    for _ in range(n):
        w, v = map(int, input().split())
        dp[w] = v

    for i in range(2, k + 1):
        for j in range(i):
            dp[i] = max(dp[j] + dp[i - j], dp[i])

    print(max(dp))
    
    
'''
    12863 평범한 배낭 
    
    두 번째 풀이: 냅색 알고리즘 
    주어진 물건의 용량과 가치를 고려해서 담을지 말지 결정하는 문제 
    
    배낭의 용량 7 이라고 했을 때, 
    1. (무게: 6, 가치: 13)인 첫 번째 물건을 담았다
    2. (무게: 4, 가치 8)인 두 번째 물건을 담을 수 없다. 
    -> 첫 번째 담았던 물건을 버리던가, 두 번째 물건을 담지 않던가 선택해야 함! 
    
    dp[n][k]: n 번째 물건까지 살펴보았을 때 무게가 k인 배낭의 최대 가치 
    (y축: [무게, 가치]에 해당 하는 물건, x축: 가방의 무게(0~K))
    
'''


if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n, k = map(int, input().split())
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    lst = [[0, 0]]

    for i in range(n):
        w, v = map(int, input().split())
        lst.append([w, v])

    for i in range(n+1):
        for j in range(k+1):
            w = lst[i][0]
            v = lst[i][1]
            # 현재 배낭의 허용 무게보다 넣을 물건의 무게가 크다면 넣지 않는다.
            if j < w:
                dp[i][j] = dp[i-1][j]

            # 현재 물건을 넣는다. vs 현재 물건을 넣지 않는다.
            else:
                dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])

    print(dp[n][k])

    
'''
    1699 제곱수의 합 
    (pypy 제출)
    시간초과 해결 도움: min -> if문 
    
'''


if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n = int(input())
    dp = [i for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, i):
            if i < j ** 2:
                break

            if dp[i - j ** 2] + 1 < dp[i]:
                dp[i] = dp[i - j ** 2] + 1

    print(dp[n])
