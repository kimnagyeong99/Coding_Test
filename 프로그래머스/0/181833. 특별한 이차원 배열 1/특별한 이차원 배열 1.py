def solution(n):
    answer = []
    i = 0
    while i < n:
        a = []
        j = 0
        while j < n:
            a.append(0)
            j += 1
        a[i] = 1
        answer.append(a)
        i += 1
    return answer