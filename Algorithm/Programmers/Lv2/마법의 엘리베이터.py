def solution(storey):
    answer = 0
    
    while 0 < storey: 
        if 5 < storey % 10:
            answer += 10 - storey % 10
            n = len(str(storey))
            storey = (storey + (10 - storey % 10)) // 10

        elif 5 > storey % 10:
            answer += storey % 10
            n = len(str(storey))
            storey = (storey - storey % 10) // 10
            
        else:
            if len(str(storey)) == 1:
                answer += 10 - storey % 10
                n = len(str(storey))
                storey = (storey + (10 - storey % 10)) // 10
                break
                
            for i in range(len(str(storey))-2, -1, -1):
                if int(str(storey)[i]) < 5:
                    answer += storey % 10
                    n = len(str(storey))
                    storey = (storey - storey % 10) // 10
                    break
                
                else:
                    answer += 10 - storey % 10
                    n = len(str(storey))
                    storey = (storey + (10 - storey % 10)) // 10  
                    break
             
    return answer
