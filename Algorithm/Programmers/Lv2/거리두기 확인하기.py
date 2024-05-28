def solution(places):
    answer = []
    dy = [0, 0, 1, -1, -1, 1, 1, -1, 0, 0, -2, 2]
    dx = [1, -1, 0, 0, 1, 1, -1, -1, 2, -2, 0, 0]
    
    for p in places:
        flg = 0
        for y in range(5):
            for x in range(5):
                if p[y][x] == 'P':
                    for k in range(12):  
                        ny = y + dy[k]
                        nx = x + dx[k]
                        
                        if (0 <= ny < 5) and (0 <= nx < 5): 
                            if p[ny][nx] == 'P':
                                if k < 4:   # 상하좌우
                                    answer.append(0)
                                    flg = 1
                                    break
                                else:
                                    if k == 4:
                                        if (0 <= y-1 and p[y-1][x] != 'X') or ( x+1 < 5 and p[y][x+1] != 'X'):
                                            answer.append(0)
                                            flg = 1
                                            break
                                    
                                    elif k == 5:
                                        if (x+1 < 5 and p[y][x+1] != 'X') or (y+1 < 5 and p[y+1][x] != 'X'):
                                            answer.append(0)
                                            flg = 1
                                            break
                                    
                                    elif k == 6:
                                        if (0 <= x-1 and p[y][x-1] != 'X') or (y+1 < 5 and p[y+1][x] != 'X'):
                                            answer.append(0)
                                            flg = 1
                                            break
                                            
                                    elif k == 7:
                                        if (0 <= y-1 and p[y-1][x] != 'X') or (0 <= x-1 and p[y][x-1] != 'X'):
                                            answer.append(0)
                                            flg = 1
                                            break  
                                    
                                    elif k == 8:
                                        if (p[y][x+1] != 'X'):
                                            answer.append(0)
                                            flg = 1
                                            break
                                    
                                    elif k == 9:
                                        if (p[y][x-1] != 'X'):
                                            answer.append(0)
                                            flg = 1
                                            break
                                    
                                    elif k == 10:
                                        if (p[y-1][x] != 'X'):
                                            answer.append(0)
                                            flg = 1
                                            break
                                    
                                    elif k == 11:
                                        if (p[y+1][x] != 'X'):
                                            answer.append(0)
                                            flg = 1
                                            break                                                       
                if flg == 1:
                    break
                    
            if flg == 1:
                break
            
        if flg == 0:
            answer.append(1)
            
    return answer
