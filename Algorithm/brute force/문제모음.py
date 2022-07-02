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
