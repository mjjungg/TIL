import sys

sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
m = int(input())

lower = 1
upper = m

# 모든 요청이 배정될 수 있는 경우-요청한 총 금액의 합 <= 총 예산  
if sum(a) <= m:     
    print(max(a))
# 모든 요청이 배정될 수 없는 경우 
else:
    while lower <= upper:
        re = 0  # 제공 가능한 예산의 합 
        mid = (lower + upper) // 2  # 최대 배정 예산이 될 수 있는 수 
        for i in a:
            if i - mid <= 0:    
                re += i
            else:
                re += mid
                
        if m < re:
            upper = mid - 1
        else:
            lower = mid + 1

    print(upper)
