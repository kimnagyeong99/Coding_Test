def solution(sides):
    sides.sort()
    a = int(sides[0])
    b = int(sides[1])
    
    return (b - (b-a)) + ((a+b) - b - 1)
    