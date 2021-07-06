import sys

'''
모든 로프를 사용하지 않아도 된다는 것 이해해야 함!!
예를 들어 2, 20 두 개의 로프가 있다고 가정했을 때 
2를 쓰지 않는 것이 더 무거운 물체를 들 수 있다  
'''
sys.stdin = open("input.txt", "rt")

n = int(input())
l = [int(input()) for _ in range(n)]

l.sort(reverse=True)
for i in range(n):
    l[i] = l[i] * (i+1)

print(max(l))
