import sys


#sys.stdin = open("input.txt", "rt")

n = int(input())
res = float('inf')
lst = list(map(int, input().split()))
lst.sort()

lower = 0
upper = n-1
ans1, ans2 = 0, 0

while lower < upper:
    mid = lst[lower] + lst[upper]

    if abs(mid) < abs(res):
        ans1, ans2 = lst[lower], lst[upper]
        res = mid

    if mid == 0:
        break

    if mid < 0:
        lower += 1

    elif 0 < mid:
        upper -= 1


print(ans1, ans2)


