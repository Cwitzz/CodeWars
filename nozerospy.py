def semzero(n):
    n = str(n)
    n = list(n)
    while n[-1] == '0':
        n.pop()
    n = ''.join(n)
    return print(int(n))




semzero(12300320)