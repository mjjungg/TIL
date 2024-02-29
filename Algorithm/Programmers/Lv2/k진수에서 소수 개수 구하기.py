def solution(n, k):
    answer = 0
    a = ''
    
    while 0 < n:
        a += str(n % k)
        n //= k
        
    a = a[::-1]
    l = a.split('0')
    
    for i in l:
        if i != '':
            flg = 0
            
            for k in range(2, int(int(i) ** 0.5) + 1):
                if int(i) % k == 0:
                    flg = 1
                    break
                    
            if flg == 0 or i == '2':
                if i != '1':
                    answer += 1
    
    return answer
