```
  deque는 pop(i) 안 됨!!
```

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    hit = 1
    miss = 5
    cache = deque()
    cities = [i.lower() for i in cities]
    
    if cacheSize == 0:
        return len(cities) * miss
    
    for i in range(len(cities)):
        if cities[i] not in cache:
            answer += miss
            if cacheSize <= len(cache):
                cache.popleft()
            
            cache.append(cities[i])
        else:
            answer += hit
            cache.remove(cities[i])
            cache.append(cities[i])
        
    return answer
