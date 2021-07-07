import sys

#sys.stdin = open("input.txt", "rt")
n = int(input())
lst1 = list(map(int, input().split()))
m = int(input())
lst2 = list(map(int, input().split()))

lst1.sort()

for i in range(m):
    lower = 0
    upper = n-1

    while lower <= upper:
        mid = (lower + upper) // 2

        if lst1[mid] == lst2[i]:
            print(1)
            break
        elif lst1[mid] > lst2[i]:
            upper = mid - 1
        else:
            lower = mid + 1
    else:
        print(0)
