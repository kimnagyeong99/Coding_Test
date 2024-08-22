def solution(arr, intervals):
    answer = []
    for a, b in intervals:
        a = arr[int(a):int(b)+1]
        for j in a:
            answer.append(j)
    return answer