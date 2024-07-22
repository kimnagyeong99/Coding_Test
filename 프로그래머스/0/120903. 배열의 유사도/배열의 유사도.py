def solution(s1, s2):
    j = 0
    for i in s1:
        if i in s2:
            j += 1
    return j