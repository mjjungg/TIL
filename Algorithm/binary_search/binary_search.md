## **이분 탐색이란?**

오름차순 또는 내림차순으로 정렬된 수열에서 **특정 값의 위치를 찾는 알고리즘**이다. 탐색 대상을 반으로 줄여나가므로 선형 탐색보다 빠르게 검색할 수 있다.  시간복잡도는 O(logn)이다.

*예) 숫자 M이 정렬된 상태에서 몇 번째에 위치하는 지를 묻는 문제*

수열의 중간 위치에서부터 탐색을 시작한다.

```python
lower = 0
upper = N-1

while lower <= upper:
    mid = (lower + upper) // 2
    if lst[mid] == M:
        print(mid + 1)
        break
    elif lst[mid] < M:
        lower = mid + 1
    else:
        upper = mid - 1
```

> 💡 **답이 어떤 범위 내에 존재할 때 이분 탐색을 사용한다**.
