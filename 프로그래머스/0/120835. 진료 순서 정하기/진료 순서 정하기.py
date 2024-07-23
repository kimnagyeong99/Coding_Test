def solution(emergency):
    a = emergency.copy()
    answer = []
    a.sort(reverse = True)
    for i in emergency:
        j = a.index(i) + 1
        answer.append(j)
        
    return answer