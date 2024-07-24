def solution(s):
    a = set(list(s))
    b = []
    for i in a:
        if s.count(i) == 1:
            b.append(i)
    b.sort()
    return ''.join(b)