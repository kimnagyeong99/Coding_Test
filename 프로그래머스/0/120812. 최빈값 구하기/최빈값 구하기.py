def solution(array):
    if len(array) == 1:
        return array[0]
    else:
        a = set(array)
        b = {}
        for i in a:
            b[i] = array.count(i)
        
        answer = list(sorted(b.items(), key = lambda x : x[1], reverse = True))
        if len(answer) == 1:
            return answer[0][0]
        
        if answer[0][1] == answer[1][1]:
            return -1
        else:
            return answer[0][0]