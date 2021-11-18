def C(n,k):
    if k == 0 or n == k:
        fn = 1
    else:
        print(f'{n}C{k} = {n-1}C{k-1} + {n-1}C{k}')
        fn = C(n-1,k-1) + C(n-1,k)
    print(f'{n}C{k} = {fn}')
    return fn

C(int(input()),int(input()))