import re
number = raw_input("number?")
i = 0
res = 0
a = 0
b = 1
while i < len(number):
    number1 = int(number[a])
    number2 = int(number[b])
    if number1 == number2:
        print 'match found'
        res = res + number1
        print res
    if b == len(number):
        b = 0
    a += 1
    b += 1
    i += 1
if number.startswith == number.endswith:
    res = res + number.startswith
print res
