import sys

sys.stdin = open("input.txt", "rt")

n = int(input())
a, b, c = 0, 0, 0
flg = 0

''' 
뺄셈으로 풀었지만, //, % 로 푸는 것이 더 효율적!! 
항상 뺄셈으로 푸는 문제 나눗셈으로 대체될 수 있는 지 체크하자
'''
while n > 0:
    if n < 10:
        print(-1)
        flg = 1
        break

    if n - 300 >= 0:
        n -= 300
        a += 1
    elif n - 60 >= 0:
        n -= 60
        b += 1
    elif n - 10 >= 0:
        n -= 10
        c += 1

if flg == 0:
    print(a, b, c)

