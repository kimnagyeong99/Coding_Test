def solution(my_string):
    a = []
    for i in my_string:
        if i.isdigit():
            a.append(int(i)) 
    a.sort()
    return a