def solution(my_string, is_prefix):
    if len(my_string) < len(is_prefix):
        return 0
    else:
        if my_string[0:len(is_prefix)] == is_prefix:
            return 1
        else:
            return 0