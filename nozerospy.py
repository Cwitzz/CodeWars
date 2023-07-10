def no_boring_zeros(n):
    n = str(n)
    n = list(n)
    while len(n) > 0 and n[-1] == '0':
        n.pop()
    n = ''.join(n)
    return int(n)
