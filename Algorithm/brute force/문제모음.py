import sys

'''
        2798 블랙잭   
'''

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))
    res = 0
    cards.sort()

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                tmp = 0

                if m < tmp + cards[k]:
                    break
                tmp += cards[k]

                if m < tmp + cards[j]:
                    break
                tmp += cards[j]

                if m < tmp + cards[i]:
                    break
                tmp += cards[i]

                if res < tmp:
                    res = tmp
    print(res)

'''
        7568 덩치
        
        키 포인트 : 자신보다 더 덩치가 큰 사람의 수 + 1
'''

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n = int(input())
    report = []
    res = []

    for _ in range(n):
        x, y = map(int, input().split())
        report.append([x, y])

    for i in range(n):
        cnt = 0
        for j in range(n):
            if (report[i][0] < report[j][0]) and (report[i][1] < report[j][1]):
                cnt += 1

        res.append(cnt+1)

    for i in res:
        print(i, end=' ')


'''
        2231 분해합
'''
def split_num(x):
    lst = []

    while x // 10 > 0:
        lst.append(x % 10)
        x = x // 10
    lst.append(x)
    return lst
if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n = int(input())
    res = []
    ans = float('inf')

    for i in range(1, n):
        m = i
        k = split_num(m)
        for j in range(len(k)):
            m += k[j]

        if m == n:
            tmp = [str(i) for i in k]
            tmp.reverse()
            case = int("".join(tmp))

            if case < ans:
                ans = case

    if ans == float('inf'):
        print(0)
    else:
        print(ans)
        

'''
        1018 체스판 다시 칠하기 
        
        W와 B의 위치의 규칙 찾는 게 포인트! 
        (행+열) % 2 == 0 인 경우 다 같은 색이여야 함
        
'''


if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n, m = map(int, input().split())
    board = []
    res = []
    c = 7
    for _ in range(n):
        board.append(input())

    for i in range(n-c):
        for j in range(m-c):
           caseW = 0  # 'W'로 시작하는 체스 판으로 만들기 위해 바꿔야 하는 정사각형 갯수
           caseB = 0  # 'B'로 시작하는 체스 판으로 만들기 위해 바꿔야 하는 정사각형 갯수
           for k in range(i, i+8):
               for l in range(j, j+8):
                   if (k+l) % 2 == 0:  # 시작점의 색과 같아야 함
                       if board[k][l] != 'W':
                           caseW += 1
                       if board[k][l] != 'B':
                           caseB += 1
                   else:    # 시작점의 색과 달라야 함
                       if board[k][l] != 'B':
                           caseW += 1
                       if board[k][l] != 'W':
                           caseB += 1


           res.append(min(caseW, caseB))

    print(min(res))
