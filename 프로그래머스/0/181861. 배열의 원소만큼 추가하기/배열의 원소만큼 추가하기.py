def solution(arr):
    answer = []
    for i in arr:
        j = 1
        while j <= int(i):
            answer.append(i)
            j += 1
            
    return answer