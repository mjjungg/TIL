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
