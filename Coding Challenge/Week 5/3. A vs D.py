nums = []
A, D = 0, 0

while True:
    n = input('Number: ')
    if n == 'x':
        break
    else:
        n = int(n)
        for i in nums:
            if i < n:
                D = 1
            elif i > n:
                A = 1
        nums.append(n)

if A == 0:
    print('A')
if D == 0:
    print('D')