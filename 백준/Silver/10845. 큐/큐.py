a = int(input())
q = []
for i in range(0, a):
    b = input()
    if b == 'size':
        print(len(q))
    elif 'push' in b:
        c, d = b.split()
        q.append(d)
    else:
        if len(q) == 0:
            if b == 'pop' or (b == 'front') or (b == 'back'):
                print(-1)
            else:
                print(1)
        else:
            if b == 'pop':
                print(q.pop(0))
            elif b == 'front':
                print(q[0])
            elif b == 'back':
                print(q[-1])
            else:
                print(0)