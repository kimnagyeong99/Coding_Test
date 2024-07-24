def solution(my_string):
    return ''.join(list(dict.fromkeys(list(my_string))))