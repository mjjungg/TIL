'''
        4673 셀프 넘버  
'''

def split_num(x):
    lst = []
    while x // 10 > 0:
        lst.append(x % 10)
        x = x // 10
    lst.append(x)

    return lst

if __name__ == "__main__":
    n = 10000
    self_num_lst = []

    for i in range(1, n+1):
        self_num = i
        r = split_num(i)

        for j in range(len(r)):
            self_num += r[j]

        self_num_lst.append(self_num)

    for i in range(1, n+1):
        if i not in self_num_lst:
            print(i)

        
'''
        1316 그룹단어 체커
'''
        
if __name__ == "__main__":
    n = int(input())
    res = n

    for _ in range(n):
        s = input()
        check = []

        for i in s:
            if i not in check:
                check.append(i)
            else:
                if check[-1] != i:
                    res -= 1
                    break
    print(res)

'''
        2941 크로아티아 알파벳
        
        문자열에서 for문 돌려고만 생각함 -> 크로아티아에서 for문 돎
        
'''


if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    s = input()
    c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

    for i in c:
        s = s.replace(i, '*')

    print(len(s))

import sys
from collections import deque
'''
        1021 회전하는 큐
        
        1. 큐에서 원소 삭제할 때마다 큐의 길이 갱신해야 하는 부분 빼먹음
        2. 문제 제대로 읽지 않아서 잘못 이해함 
        
        => 구현 문제는 문제 꼼꼼히 읽고 주어진 조건, 변할 때 마다 체크 사항 빠뜨리지 않기!!!!
        
'''

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n, m = map(int, input().split())
    targets = list(map(int, input().split()))
    res = 0
    q = deque([i for i in range(1, n+1)])

    for i in range(m):
        target = targets[i]
        getIdx = q.index(target)
        m = len(q)  # 큐의 길이가 계속 줄어드니 갱신해야 함

        if getIdx < m-getIdx:   # 왼쪽으로 이동
            while True:
                if q[0] == target:
                    q.popleft()
                    break
                else:
                    q.append(q.popleft())
                    res += 1

        else:   # 오른쪽으로 이동
            while True:
                if q[0] == target:
                    q.popleft()
                    break
                else:
                    q.appendleft(q.pop())
                    res += 1

    print(res)
