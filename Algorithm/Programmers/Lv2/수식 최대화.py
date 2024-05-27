from itertools import permutations

def solution(expression):
    answer = 0
    ex = set()
    lst = []
    tmp = ''
    
    for i in expression:
        if i in ['-', '*', '+']:
            ex.add(i)
            lst.append(tmp)
            lst.append(i)
            tmp = ''
        else:
            tmp += i 
            
    lst.append(tmp)
    p = permutations(ex, len(ex))
    
    for case in p:
        tmp = 0
        cpy_lst = lst[:]
        stack = []
        case = list(case)
        
        while case:
            if 0 < len(cpy_lst):
                now = cpy_lst.pop(0)
                
                if now == case[0]:
                    stack.append(str(eval(stack.pop() + case[0] + cpy_lst.pop(0))))
                
                else:
                    stack.append(now)
            else:
                case.pop(0)
                cpy_lst = stack[:]
                stack = []

        answer = max(answer, abs(int(cpy_lst[0])))
    
    return answer
