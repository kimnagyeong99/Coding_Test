def solution(n_str):
    a = 0
    for i in n_str:
        if i == "0":
            pass
        else:
            a += n_str.find(i)
            break
            
    return n_str[a:]