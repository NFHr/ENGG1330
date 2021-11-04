primes = []
num = int(input())
count = 0

#generate primes from (2,input)
for i in range(2,num):
    check = 0
    for j in range(2,i):
        if i % j == 0:
            check = 1
            break
    if check == 0 and i not in primes:
        primes.append(i)

#count nprime
for n in primes:
    if num % n != 0:
        count += 1

print(count)