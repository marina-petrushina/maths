
x = 0
for i in range(100, 1000):
    for j in range(100,1000):
        a1 = str(i*j)
        a2 = []
        n = 1
        
        while n <= len(a1):
            a2.append(a1[-n])
            n += 1
        a3 = ''
        for n in a2:
            a3 = a3 + n
        if a1 == a3 and int(a1) > x:
            x = int(a1)

print(x)
        
