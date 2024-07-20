def solution(n):
    i = 1
    j = 0
    while i <= n:
        if n % i == 0:
            j += 1
        i += 1
    return j