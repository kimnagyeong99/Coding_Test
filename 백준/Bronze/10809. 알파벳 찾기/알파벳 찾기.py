ap = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

a = input()
b = []

for i in ap:
    if i in a:
        b.append(a.index(i))
    else:
        b.append(-1)

print(" ".join(map(str, b)))