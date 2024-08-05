def solution(id_pw, db):
    a = id_pw
    for i in db:
        if i[0] == a[0]:
            if i[1] == a[1]:
                return 'login'
                break
            else:
                return'wrong pw'
        
    return 'fail'     