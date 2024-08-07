def solution(arr):
    a = []
    
    for i in arr:
        if (i % 2 == 0) and (i >= 50):
            a.append(i // 2)
        elif (i % 2 != 0) and (i < 50):
            a.append(i * 2)
        else:
            a.append(i)
    return a