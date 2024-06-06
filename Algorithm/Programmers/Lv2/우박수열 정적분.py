def solution(k, ranges):
    answer = []
    lst = []
    area = []
    y = 0
    
    lst.append([y, k])
    
    while 1 < k:
        y += 1
        
        if k % 2 == 0:
            k //= 2
        
        else:
            k = k * 3 + 1
        
        lst.append([y, k])
    
    n = len(lst) - 1
    pre_a = lst[0][1]    
    
    for i in range(1, len(lst)):
        a = lst[i][1]
                
        area.append((pre_a + a) / 2)
        
        pre_a = a
    
    for x, y in ranges:
        y = n + y
        res = 0
        if (x < y):
            for i in range(x, y):
                if 0 <= i:
                    res += area[i]
        elif x == y:
            res = 0
            
        else:
            res = -1
        
        answer.append(res)
 
    return answer
