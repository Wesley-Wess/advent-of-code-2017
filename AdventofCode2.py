number = raw_input("number?")
i = 0
res = 0
a = 0
gap = len(number) / 2
while i <= len(number):
    number1 = int(number[a])
    if (i + gap) >= number:
        number2 = int(number[i + gap])
    else:
        number2 = (i + gap) - len(number)
    if number1 == number2:
        res = res + number1
        print res
    i += 1
    a += 1
print res
