def no_boring_zeros(n):
    n = str(n)
    if n == '0':
        return 0
    while n[-1] == '0':
        n = n[:-1]
    return int(n)


no_boring_zeros(12330)