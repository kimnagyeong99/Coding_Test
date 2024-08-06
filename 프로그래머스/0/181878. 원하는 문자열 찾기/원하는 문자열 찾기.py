def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()
    if myString.find(pat) >= 0:
        return 1
    else:
        return 0