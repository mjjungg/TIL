import sys
import math


''' 1072 게임
    처음 아이디어 : 
    lt = 1, rt = x로 초기화하고 
    승률을 계산한 값이 처음 승률과 다르다면 mid 값을 줄임 (간격을 줄임)
    ?? 승률은 계속 증가한다(계속 이기만 하기 때문) 그러면 간격은 대체 언제 넓힘 ??
    ?? rt 값을 어떻게 초기화할지도 모르겠음 ??
'''
# def calculate(x, y):
#     return math.trunc((y / x) * 100)
#
#
# if __name__ == '__main__':
#     sys.stdin = open("input.txt", "rt")
#     x, y = map(int, input().split())
#     res = -1
#     now = calculate(x, y)
#
#     lt = 1
#     rt = x
#
#     while lt <= rt:
#         mid = (lt + rt) // 2
#
#         if calculate != now:
#             rt = mid - 1
#             res = mid
#
#     print(res)


########### 정답 #################

sys.stdin = open("input.txt", "rt")
x, y = map(int, input().split())
res = float('inf')
fir_rate = math.trunc((y / x) * 100)

lt = 1
rt = x

if 99 <= fir_rate or x == y:
    print(-1)
    exit()

while lt <= rt:
    mid = (lt + rt) // 2
    rate = math.trunc(((y+mid) / (x+mid)) * 100)

    # 승률이 오르지 않으면 게임 판 수를 늘린다
    if rate == fir_rate:
        lt = mid + 1
    # 승률이 오르면, 게임 판 수를 줄여보자 -> 최소 판 수를 구해야 하기 때문!
    else:
        res = mid
        rt = mid - 1

print(res)

