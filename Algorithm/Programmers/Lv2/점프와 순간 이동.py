# 시간초과 풀이 --> dp 사용 
# 결과적으로 dp도 틀린 풀이임 
'''
짝수인 경우, 무조건 dp[i] = dp[i//2]
홀수인 경우, 무조건 dp[i] = dp[i-1] + 1

=> 입력값의 최댓값 && dp 조건 잘 확인하기!!
'''
def solution(n):
    dp = [i for i in range(n+1)]
    if n < 2:
        return dp[n]
    
    dp[2] = 1
    
    for i in range(3, n+1):
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2], dp[i-1] + 1)
        else:
            dp[i] = min(dp[i], dp[i-1] + 1)
    
    return dp[n]

# 정답
def solution(n):
    answer = 0
    
    while 0 < n:
        if n % 2 == 1:
            answer += 1
            n -= 1
            
        else:
            n //= 2
    
    return answer
