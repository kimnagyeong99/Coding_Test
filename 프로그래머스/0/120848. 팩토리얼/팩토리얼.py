def solution(n):
    a = 0 
    j = 1
    while True:
        for i in range(1, n+1):
            j *= i
            a += 1
            if j == n:
                return a
                break
            elif j > n:
                return a - 1
                break