x = 0
for i in range(100, 1000):
    for j in range(100,1000):
        a1 = str(i*j)
        a2 = a1[::-1]
        if a2 == a1 and int(a1) > x:
            x = int(a1)
print(x)
        
