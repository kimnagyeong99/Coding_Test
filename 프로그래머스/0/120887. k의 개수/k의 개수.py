def solution(i, j, k):
    a = 0
    for l in range(i, j+1):
        l = str(l)
        a += l.count(str(k))
        
    return a