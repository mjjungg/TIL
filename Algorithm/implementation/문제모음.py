'''
        4673 셀프 넘버  
'''

def split_num(x):
    lst = []
    while x // 10 > 0:
        lst.append(x % 10)
        x = x // 10
    lst.append(x)

    return lst

if __name__ == "__main__":
    n = 10000
    self_num_lst = []

    for i in range(1, n+1):
        self_num = i
        r = split_num(i)

        for j in range(len(r)):
            self_num += r[j]

        self_num_lst.append(self_num)

    for i in range(1, n+1):
        if i not in self_num_lst:
            print(i)

        
'''
        1316 그룹단어 체커
'''
        
if __name__ == "__main__":
    n = int(input())
    res = n

    for _ in range(n):
        s = input()
        check = []

        for i in s:
            if i not in check:
                check.append(i)
            else:
                if check[-1] != i:
                    res -= 1
                    break
    print(res)

'''
        2941 크로아티아 알파벳
        
        문자열에서 for문 돌려고만 생각함 -> 크로아티아에서 for문 돎
        
'''


if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    s = input()
    c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

    for i in c:
        s = s.replace(i, '*')

    print(len(s))
