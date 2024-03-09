def solution(n, t, m, p):
    answer = ''
    numbers = ['0']
    
    for i in range(t*m+1):
        tmp = []
    
        while 0 < i:
            if 10 <= i % n: 
                tmp.append(chr(i % n + 55))
            else:
                tmp.append(str(i % n))
            i //= n
            
        tmp = tmp[::-1]
        numbers.append(''.join(tmp))
    
    total = ''
    for num in numbers:
        total += num
        
    for i in range(t):
        answer += total[i * m + (p-1)]
        
    return answer
