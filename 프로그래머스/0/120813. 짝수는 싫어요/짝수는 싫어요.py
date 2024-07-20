def solution(n):
    i = 1
    answer = []
    while i <= int(n):
        if i % 2 != 0:
            answer.append(i)
        i += 1
    return answer