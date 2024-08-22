def solution(arr, divisor):
    answer = []
    for i in arr:
        if int(i) % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
        return answer
    else:
        answer.sort()
        return answer