a = int(input())
l = input()
l = list(map(int, l.split()))
w = []
n = 1

for i in l:
    if i == n:
        n += 1
    else:
        w.append(i)

    while w and (w[-1] == n):
        w.pop()
        n += 1
if w:
    while w and (w[-1] == n):
        w.pop()
        n += 1
else:
    pass

if (len(w) == 0) and ((n-1) == (a)):
    print("Nice")
else:
    print("Sad")