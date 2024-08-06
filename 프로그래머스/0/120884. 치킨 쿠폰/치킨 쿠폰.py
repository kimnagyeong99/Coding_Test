def solution(chicken):
    j = 0
    k = 0
    while chicken // 10 >= 1:
        j += (chicken // 10)
        if chicken % 10 != 0:
            k += (chicken % 10)
            
        chicken = (chicken // 10)
    k += chicken
    j += (k // 10)
    if ((k // 10) + (k % 10)) % 10 == 0:
        j += ((k // 10) + (k % 10)) // 10
    return j

