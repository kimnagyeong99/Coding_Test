def solution(balls, share):
    a = 1
    for i in range(1, share+1):
        a *= i
    
    b = 1
    for i in range(balls, (balls - share), -1):
        b *= i
        
    return b / a