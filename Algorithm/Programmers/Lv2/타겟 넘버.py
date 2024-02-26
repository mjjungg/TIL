answer = 0
def solution(numbers, target):
    def dfs(n, lev):
        global answer
        
        if lev == len(numbers):
            if n == target:
                answer += 1 
            return

        
        dfs(n + numbers[lev], lev + 1)
        dfs(n - numbers[lev], lev + 1)
    
    dfs(0, 0)
        
    return answer
