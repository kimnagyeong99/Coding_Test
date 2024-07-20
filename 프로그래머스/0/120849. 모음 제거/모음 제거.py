def solution(my_string):
    a = ['a', 'e', 'i', 'o', 'u']
    b = my_string
    for i in a:
        b = b.replace(i, '')
    return b