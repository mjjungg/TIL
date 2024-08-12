def solution(n):
    answer = 0
    dp = [0 for _ in range(n+1)]
    dp[2] = 3
    
    for i in range(4, n+1):
        if i % 2 == 0:
            dp[i] = dp[i-2] * dp[2]
            for j in range(i-4, 0, -2):
                dp[i] += dp[j] * 2
                
            dp[i] += 2
            dp[i] %= 1000000007
        
    return dp[n]
