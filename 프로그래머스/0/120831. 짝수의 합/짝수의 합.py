def solution(n):
    i = 1
    j = 0
    while i <= n:
        if i % 2 == 0:
            j += i
            
        i += 1
    return j