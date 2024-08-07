def solution(num_list, n):
    a = []
    b = []
    for i in range(0, n):
        a.append(num_list[i])
    for j in range(n, len(num_list)):
        b.append(num_list[j])
    return b + a