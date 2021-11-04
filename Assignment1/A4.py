num, index, count = input('Numbers: '), 0, 0
numlist, prime = [], []
check = 0

#converting into list
for i in range(len(num)):
    if num[i] == ' ':
        numlist.append(int(num[index:i]))
        index = i+1
numlist.append(int(num[index:i+1]))

if 1 in numlist:
    numlist.remove(1)

#find prime
for m in range(1, min(numlist) + 1):
    for n in numlist:
        if n % m == 0:
            prime.append(m)
prime_set = set(prime)

#judge
for k in prime_set:
    count = 0
    for l in prime:
        if k == l and k != 1:
            count += 1

    if count > 1:
        if count == len(numlist): 
            check = 2 # means not mrp or prp
            break
        else:
            check = 1 #1 means mrp

if check == 0:
    print('prp')
elif check == 1:
    print('mrp')
else:
    print('~')