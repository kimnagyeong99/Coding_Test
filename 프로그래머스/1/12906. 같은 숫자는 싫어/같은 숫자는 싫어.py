def solution(arr):
    answer = []
    j = ''
    for i in arr:
        if j == i:
            pass
        else:
            answer.append(i)
        
        j = i
    return answer