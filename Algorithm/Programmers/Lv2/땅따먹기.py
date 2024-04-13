def solution(land):
    answer = 0
    dp = [[0 for _ in range(4)] for _ in range(len(land))]
    
    for i in range(4):
        dp[0][i] = land[0][i]
    
    for i in range(1, len(land)):
        for j in range(4):
            max_val = 0
            for k in range(4):
                if j != k and max_val < dp[i-1][k]:
                    max_val = dp[i-1][k]
            dp[i][j] = land[i][j] + max_val
            
    return max(dp[-1])
