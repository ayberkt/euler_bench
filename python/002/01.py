fib = [1,2]
stop = 4000000
total = 0
while True:
        nex = fib[-1] + fib[-2]
        if nex <= stop:
                fib.append(nex)
        else: break
for i in fib:
        if i%2 != 0: total += i
print total
