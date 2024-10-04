a = int(input())

for i in range(0, a):
    b = input()
    n = []
    k = 0
    for j in b:
        if j == "O":
            k += 1
            n.append(k)
        else:
            k = 0
    
    print(sum(n))