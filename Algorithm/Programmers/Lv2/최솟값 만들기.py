def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    
    while A:
        answer += A.pop(0) * B.pop(0)
        
    return answer
