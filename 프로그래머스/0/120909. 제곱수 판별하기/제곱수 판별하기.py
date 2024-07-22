def solution(n):
    i = 1
    while i <= n:
        if (n % i == 0) and (n // i == i):
            return 1
        else:
            if i == n:
                return 2
            else:
                i += 1