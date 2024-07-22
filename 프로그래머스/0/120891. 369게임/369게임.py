def solution(order):
    k = 0
    for i in str(order):
        if i in ['3', '6', '9']:
            k += 1
    return k