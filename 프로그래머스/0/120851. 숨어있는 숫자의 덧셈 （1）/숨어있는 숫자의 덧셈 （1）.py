def solution(my_string):
    k = 0
    for i in my_string:
        for j in range(1, 10):
            if i == str(j):
                k += int(i)
    return k