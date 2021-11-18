def Pascal(n):
    if n == 1:
        return [1]
    else:
        current = [1]
        prievous = Pascal(n-1)
        for i in range(len(prievous)-1):
            current.append(n[i] + n[i+1])
        current.append(1)
    return current