def solution(array):
    a = ''
    for i in array:
        a += str(i)
        
    a = list(a)
    return a.count('7')