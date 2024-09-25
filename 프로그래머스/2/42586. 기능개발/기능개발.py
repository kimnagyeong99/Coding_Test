def solution(progresses, speeds):
    answer = []
    day = []
    a = 0
    b = 0
    for i, j in zip(progresses, speeds):
        if (100-int(i)) % j == 0:
            answer.append((100-int(i)) // j)
        else:
            answer.append(((100-int(i)) // j) + 1)
    for k in answer:
        if a < k:
            day.append(b)
            b = 0
            a = k
            b += 1
        else:
            b += 1
    day.append(b)     
    return day[1:] 
        