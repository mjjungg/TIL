import sys

#sys.stdin = open("input.txt", "rt")
N = int(input())
cnt = 0

# solve 1) 문제점 : 9와 같은 경우 9 -> 4 -> 1 => -1 출력함
# while 0 < N:
#     if 5 <= N:
#         N -= 5
#         cnt += 1
#     elif 3 <= N:
#         N -= 3
#         cnt += 1
#     elif N < 3:
#         cnt = -1
#         break

while 0 < N:
    if 5 <= N:
        if (N-5) % 5 != 0:
            N -= 3
            cnt += 1
        else:
            N -= 5
            cnt += 1

    elif 3 <= N:
        N -= 3
        cnt += 1

    elif N < 3:
        cnt = -1
        break
    #print(N)

print(cnt)
