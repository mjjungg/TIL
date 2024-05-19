def solution(book_time):
    answer = 0
    book_time.sort(key=lambda x:(x[0], x[1]))
    end_times = []
    
    for s, e in book_time:
        if len(end_times) == 0:
            end_times.append(e)
            answer += 1
            continue
        
        h1 = int(s.split(":")[0])
        m1 = int(s.split(":")[1])
        flg = 1
        
        for k in end_times:
            h2 = int(k.split(":")[0])
            m2 = int(k.split(":")[1])
            
            if 60 <= m2 + 10:
                m2 += 10
                h2 += 1
                m2 = m2 - 60
            else:
                m2 += 10
                
            if (h1 > h2) or (h1 == h2 and m1 >= m2):                
                end_times.remove(k)
                end_times.append(e)
                flg = 0
                break
                
        if flg == 1:
            answer += 1
            end_times.append(e)
            
        end_times.sort()

    return answer
