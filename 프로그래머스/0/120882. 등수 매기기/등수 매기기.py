def solution(score):
    a = []
    for i in score:
        a.append(sum(i)/2)
    b = sorted(a, reverse = True)
    c = [b.index(j) + 1 for j in a]
    return c