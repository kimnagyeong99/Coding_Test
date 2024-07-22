def solution(array):
    answer = []
    array_s = array.copy()
    array_s.sort()
    answer.append(array_s[-1])
    answer.append(array.index(array_s[-1]))
    return answer
    
    