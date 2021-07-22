import sys

sys.stdin = open("input.txt", "rt")

'''
    문제를 제대로 읽자..! 
    등수를 성적으로 보고 해매는 일 없도록 하자 
'''
t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    cnt = 1     # 서류 1위는 무조건 합격
    lst = []
    for j in range(n):
        a, b = map(int, input().split())
        lst.append([a, b])

    lst.sort(key=lambda x: x[0])
    compare = lst[0][1]   # 면접 제일 처음 비교는 서류 1위 합격자의 면접 등수
    for j in range(1, n):
        if lst[j][1] < compare:     # 합격자와 비교했을 때 이미 서류 등수가 낮으므로 무조건 면접 등수가 낮아야 함!
            cnt += 1    # 면접 등수가 낮으면 합격자!
            compare = lst[j][1]     # 비교할 합격자의 면접 등수를 갱신

    print(cnt)
