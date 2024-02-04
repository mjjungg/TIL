from collections import Counter

def solution(n):
    cnt = Counter(bin(n))['1']
    
    for i in range(n+1, 1000001):
        cnt2 = Counter(bin(i))['1']

        if cnt == cnt2:
            return i

# 더 좋은 풀이
# 1. 라이브러리 가져오지 않음 Counter -> count로 대체 가능 
# 2. 위 풀이에선 100000인 경우 제대로 결과값 도출 못함(테스트케이스 한계 문제 있음)
def solution(n):
    answer = 0
    cnt = bin(n).count('1')
    nxt = n + 1
    
    while True:
        if cnt == bin(nxt).count('1'):
            answer = nxt
            break
        
        nxt += 1
        
    return answer
