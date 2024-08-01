def solution(numbers, k):
    a = []
    if len(numbers) % 2 == 0:
        for i in range(0, len(numbers), 2):
            a.append(numbers[i])
    else:
        for i in range(0,len(numbers), 2):
            a.append(numbers[i])
        for i in range(1, len(numbers), 2):
            a.append(numbers[i])
    
    if len(a) >= k:
        return a[k-1]
    else:
        j = k % len(a)
        return a[j-1]
            