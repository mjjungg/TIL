def solution(n, words):
    answer = [0, 0]
    d = [words[0]]
    
    for i in range(1, len(words)):
        # 이전에 등장했던 단어가 나온 경우 or 끝말잇기 틀린 경우 
        if words[i] in d or words[i-1][-1] != words[i][0]:
            answer[0] = i % n + 1
            answer[1] = i // n + 1
            break
            
        d.append(words[i])
        
    return answer
