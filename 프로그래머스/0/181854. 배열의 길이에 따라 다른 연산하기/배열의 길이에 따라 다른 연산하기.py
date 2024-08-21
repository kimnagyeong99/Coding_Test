def solution(arr, n):
    answer = []
    if len(arr) % 2 == 0:
        for i in range(0, len(arr)):
            if i % 2 == 0:
                answer.append(arr[i])
            else:
                answer.append(int(arr[i])+n)
    else:
        for i in range(0, len(arr)):
            if i % 2 != 0:
                answer.append(arr[i])
            else:
                answer.append(int(arr[i])+n)
    return answer