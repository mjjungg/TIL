import copy

def solution(skill, skill_trees):
    answer = 0
    
    for st in skill_trees:
        cpy_skill = list(copy.deepcopy(skill))
        
        for i in st:
            if cpy_skill[0] == i:
                cpy_skill.pop(0)
            
            if len(cpy_skill) == 0:
                answer += 1
                break
        
        flg = 0

        for i in cpy_skill:
            if i in st:
                flg = 1
                break

        if len(cpy_skill) > 0 and flg == 0:
            answer += 1
                      
    return answer
