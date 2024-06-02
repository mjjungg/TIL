def solution(s):
    answer = len(s)
    
    for i in range(1, len(s)//2+1):
        prev = ''
        compression = ''
        n = 1
        
        for j in range(0, len(s), i):
            if len(prev) == 0:
                prev = s[j:j+i]
                continue
            
            now = s[j:j+i]
            if prev == now:
                n += 1
            else:
                if n != 1:
                    compression += str(n)
                
                compression += prev
                prev = now
                n = 1
    
        if n != 1:
            compression += str(n)
        compression += prev
     
        answer = min(answer, len(compression))
        
    return answer
