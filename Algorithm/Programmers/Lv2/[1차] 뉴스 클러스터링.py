def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    
    lst1 = []
    lst2 = []
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            lst1.append(str1[i:i+2])
    
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            lst2.append(str2[i:i+2])
        
    union = []
    inter = []
    cpy_lst1 = lst1[:]
    
    for i in lst2:
        union.append(i)
        
        if i in cpy_lst1:
            cpy_lst1.remove(i)
    
    union += cpy_lst1
    
    cpy_lst1 = lst1[:]
    
    for i in lst2:        
        if i in cpy_lst1:
            inter.append(i)
            cpy_lst1.remove(i)
    
    if len(union) == 0 and len(inter) == 0:
        return 65536
    
    answer = int(len(inter) / len(union) * 65536)
          
    return answer
