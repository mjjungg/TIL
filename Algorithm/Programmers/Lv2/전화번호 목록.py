def solution(phone_book):
    answer = True
    phone_book.sort(key=len)
    
    d = {}
    
    for pn in phone_book:
        tmp = ''
        
        for i in pn:
            tmp += i
            
            if tmp in d:
                return False
            
        d[tmp] = 1
      
    return answer
