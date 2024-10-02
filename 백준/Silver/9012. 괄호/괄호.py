a = int(input())

for i in range(0, a):
    s = []
    b = list(input())
    while b:
        if b[0] == '(':
            s.append(b.pop(0))
        elif b[0] == ')' and s:
            b.pop(0)
            s.pop()
        else:
            break 
        
    if len(s) == 0 and len(b) == 0:
        print('YES')
    else:
        print("NO")