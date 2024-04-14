def solution(files):
    answer = []
    lst = []
    
    for k in range(len(files)):
        head = ""
        number = ""
        flg = 0
        number_cnt = 0
        
        for i in files[k]:
            if (i.isalpha() or i in (" ", ".", "-")) and flg == 0:
                head += i
                
            elif i.isdigit() and number_cnt < 5:
                number += i
                flg = 1
                number_cnt += 1
            else:
                break

        lst.append([files[k], head.lower(), int(number), k])
        
    lst.sort(key = lambda x:(x[1], x[2], x[3]))
        
    return [i[0] for i in lst]
