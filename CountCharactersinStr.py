def count(s):
    contarletra = {}
    if s == '':
        return contarletra
    for letra in s:
        if letra in contarletra:
            contarletra[letra] += 1
        else:
            contarletra[letra] = 1
    return contarletra



