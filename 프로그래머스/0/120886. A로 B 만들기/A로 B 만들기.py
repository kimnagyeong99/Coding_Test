def solution(before, after):
    a = list(before)
    b = list(after)
    a.sort()
    b.sort()
    if "".join(a) == "".join(b):
        return 1
    else:
        return 0