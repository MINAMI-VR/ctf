import math

i = 0
pi = math.pi
while 1:
    a = pi
    b = 0.1 * pi
    j = i
    while j > 0:
        b = b * 10
        j = j - 1
    c = int(b)
    b = c
    j = i - 1
    while j > 0:
        b = b * 0.1
        j = j - 1
    a = a - b
    j = i + 9
    while j > 0:
        a = a * 10
        j = j - 1
    c = int(a)
    d = math.sqrt(c)
    j = 2
    isPrime = 1
    while j <= d:
        if c % j == 0:
            isPrime = 0
            break
        j = j + 1
    if isPrime == 1:
        print(c)
        break
    i = i + 1
