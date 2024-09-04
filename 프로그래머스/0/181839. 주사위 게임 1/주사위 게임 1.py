def solution(a, b):
    if ((a + b) % 2 == 0) and ((a * b) % 2 == 0):
        return abs(a-b)
    elif ((a + b) % 2 == 0) and ((a * b) % 2 != 0):
        return (a**2) + (b**2)
    else:
        return 2 * (a + b)