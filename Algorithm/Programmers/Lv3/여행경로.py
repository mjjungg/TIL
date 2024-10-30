import copy

def solution(tickets):
    answer = []
    visited = [0 for _ in range(len(tickets))]
    start = "ICN"
    
    
    def dfs(lev, start, tmp):
        if lev == len(tickets):
            answer.append(tmp)
            return
        
        for i in range(len(tickets)):
            if (tickets[i][0] == start) and (visited[i] == 0):
                t = copy.deepcopy(tmp)
                t.append(tickets[i][1])
                visited[i] = 1
                dfs(lev+1, tickets[i][1], t)
                visited[i] = 0
    
    dfs(0, start, [start])
    answer.sort()
    
    return answer[0]
