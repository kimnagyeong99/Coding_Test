a = int(input())
stack = []
for i in range(0, a):
    b = input()
    if b == 'size':
        print(len(stack))
    elif 'push' in b:
        c, d = b.split()
        stack.append(d)
    else:
        if len(stack) == 0:
            if b == 'pop' or (b == 'top'):
                print(-1)
            else:
                print(1)
        else:
            if b == 'pop':
                print(stack.pop())
            elif b == 'top':
                print(stack[-1])
            else:
                print(0)
