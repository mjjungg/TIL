import sys

'''
        2798 블랙잭   
'''

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))
    res = 0
    cards.sort()

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                tmp = 0

                if m < tmp + cards[k]:
                    break
                tmp += cards[k]

                if m < tmp + cards[j]:
                    break
                tmp += cards[j]

                if m < tmp + cards[i]:
                    break
                tmp += cards[i]

                if res < tmp:
                    res = tmp
    print(res)


'''
        2231 분해합
'''
def split_num(x):
    lst = []

    while x // 10 > 0:
        lst.append(x % 10)
        x = x // 10
    lst.append(x)
    return lst
if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n = int(input())
    res = []
    ans = float('inf')

    for i in range(1, n):
        m = i
        k = split_num(m)
        for j in range(len(k)):
            m += k[j]

        if m == n:
            tmp = [str(i) for i in k]
            tmp.reverse()
            case = int("".join(tmp))

            if case < ans:
                ans = case

    if ans == float('inf'):
        print(0)
    else:
        print(ans)
