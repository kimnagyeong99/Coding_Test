def solution(rsp):
    i = 0
    rsp = list(rsp)
    while i < len(rsp):
        if rsp[i] == '0':
            rsp[i] = '5'
            i += 1
            
        elif rsp[i] == '2':
            rsp[i] = '0'
            i += 1
        else:
            rsp[i] = '2'
            i += 1
            
    return ''.join(rsp)