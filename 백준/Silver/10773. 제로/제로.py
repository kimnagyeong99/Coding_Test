a = int(input())
num = []
s = 0
for i in range(0, a):
    b = int(input())
    if b != 0:
        num.append(b)
    else:
        num.pop()

for i in num:
    s += int(i)

print(s)