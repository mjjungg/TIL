def solution(dirs):
    answer = 0
    path = []
    y, x = 0, 0
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    dic = {"U": 0, "D": 1, "R": 2, "L": 3}
    
    for d in dirs:
        ny = y + dy[dic[d]]
        nx = x + dx[dic[d]]
        
        if -6 < ny < 6 and -6 < nx < 6:
            now_path = [(y, x), (y + dy[dic[d]], x + dx[dic[d]])]
            now_path.sort()
            
            if now_path not in path:
                path.append(now_path)
                
            y += dy[dic[d]]
            x += dx[dic[d]]
        
    return len(path)
