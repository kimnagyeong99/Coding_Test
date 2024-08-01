def solution(spell, dic):
    for i in dic:
        i = list(i)
        if len(i) == len(spell):
            for j in spell:
                if j in i:
                    i.remove(j)
            if len(i) == 0:
                return 1
                break
            
    return 2