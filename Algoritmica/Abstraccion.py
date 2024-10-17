def f(x):

    a = 0

    for i in range(1000):
        a += 1

    for i in range (x):
        a += x

    for i in range (x):
        for j in range (x):
            a += 1
            a += 1

    return a

print(f(5))  
