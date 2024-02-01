a = 600851475143
mn = []
i = 2
while a > 1:
    if a % i == 0:
        mn.append(i)
        a = a / mn[-1]
    else:
        i += 1
print(mn[-1])
print(mn)
print(i)
            
