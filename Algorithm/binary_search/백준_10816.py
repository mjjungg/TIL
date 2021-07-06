import sys
from collections import Counter
''' 단일 타겟을 검색하는 것이 아니라 복수의 타겟을 검색해야 하는 문제이다 
    => 이진 탐색 사용 시 시간 초과 발생 
'''

sys.stdin = open("input.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

c = Counter(a)
for i in b:
    if i in c:
        print(c[i], end=' ')
    else:
        print(0, end=' ')
