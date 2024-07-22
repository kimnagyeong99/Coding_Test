def solution(num_list):
    j = 0
    k = 0
    for i in num_list:
        if i % 2 == 0:
            j += 1
        else:
            k += 1
            
    return [j, k]