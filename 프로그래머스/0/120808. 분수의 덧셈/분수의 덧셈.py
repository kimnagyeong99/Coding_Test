def solution(numer1, denom1, numer2, denom2):
    a = ((numer1 * denom2) + (numer2 * denom1))
    b = (denom2 * denom1)
    i = 1
    a1 = []
    b1 = []
    c1 = []
    final = []
    while i <= int(a):
        if int(a) % i == 0:
            a1.append(i)
        i += 1
            
    i = 1
    while i <= int(b):
        if int(b) % i == 0:
            b1.append(i)
        i += 1
        
    for j in a1:
        for k in b1:
            if int(j) == int(k):
                c1.append(j)
            
    final.append(int(a) / c1[-1])
    final.append(int(b) / c1[-1])
    
    return final