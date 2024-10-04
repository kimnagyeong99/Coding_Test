a, b = input().split()

a = list(map(int, a))
b = list(b)

c = 0

a = sum(a)

for i in b:
    c += int(i) * a

print(c)