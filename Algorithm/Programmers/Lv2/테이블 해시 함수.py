def solution(data, col, row_begin, row_end):
    answer = 0
    
    # 1. col 기준 정렬
    data.sort(key=lambda x:(x[col-1], -x[0]))
    
    
    # 2. S_i 값 계산
    for i in range(row_begin-1, row_end):
        s = 0
        for j in range(len(data[0])):
            s += data[i][j] % (i+1)
        
        # XOR 연산 
        answer = answer ^ s
        
    return answer
