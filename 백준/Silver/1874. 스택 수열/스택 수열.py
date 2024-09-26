a = int(input())
end = []
num = []
p_m = []

for i in range(0, a):
    b = int(input())
    end.append(b)

for j in range(1, a+1):
    num.append(j)
    p_m.append("+")
    while (len(num) != 0) and (num[-1] == end[0]):
        num.pop()
        end.remove(end[0])
        p_m.append("-")
        if len(end) == 0:
            break

if len(num) == 0:
    for k in p_m:
        print(k)
else:
    print("NO")