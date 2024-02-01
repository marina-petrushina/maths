fib = [1, 2]
while fib[-1] < 4000000:
    i = fib[-1] + fib[-2]
    if i < 4000000:
        fib.append(i)
    else:
        break
print(fib)
summa = 0
for i in fib:
    if i % 2 == 0:
        summa += i
print(summa)
    
