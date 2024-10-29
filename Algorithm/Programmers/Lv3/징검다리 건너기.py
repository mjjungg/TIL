def solution(stones, k):
    left = 1
    right = 200000000
    
    while left <= right:
        mid = (left + right) // 2
        tmp = stones[:]
        cnt = 0
        
        for i in tmp:
            if i - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            
            if k <= cnt:
                break
                
        if k <= cnt:
            right = mid - 1
        else:
            left = mid + 1
            
    return left
