def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    x = len(arr2[0])
    answer = [[0 for _ in range(x)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            for k in range(x):
                answer[i][k] += arr1[i][j] * arr2[j][k]  
                
    return answer
