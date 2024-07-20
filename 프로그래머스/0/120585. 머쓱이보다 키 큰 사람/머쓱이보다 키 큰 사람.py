def solution(array, height):
    array.sort()
    j = 0
    for i in array:
        if int(height) < i:
            j += 1
        
    return j