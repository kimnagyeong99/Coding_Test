def solution(a, b):
    f = str(a) + str(b)
    s = 2 * a * b
    if int(f) > s:
        return int(f)
    elif int(f) < s:
        return s
    else:
        return int(f)