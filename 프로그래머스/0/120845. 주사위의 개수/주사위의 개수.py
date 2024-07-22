def solution(box, n):
    j = 1
    for i in box:
        j *= (i // n)
    return j