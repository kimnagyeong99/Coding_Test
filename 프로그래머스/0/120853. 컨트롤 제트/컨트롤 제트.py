def solution(s):
    s = s.split(' ')
    a = 0
    for i in range(len(s)):
        if s[i] != 'Z':
            a += int(s[i])
        else:
            a -= int(s[i-1])
    return a