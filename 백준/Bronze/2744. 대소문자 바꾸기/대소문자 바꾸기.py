my_string = input()

b = ''

for i in my_string:
    if i.isupper() == True:
        b += i.lower()
    else:
         b += i.upper()

print(b)