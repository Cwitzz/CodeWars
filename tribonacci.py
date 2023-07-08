def tribonacci(signature, n):
    if n == 0:
        return []
    elif n <= 3:
        return signature[:n]

    sequence = signature[:]

    while len(sequence) < n:
        next_number = sum(sequence[-3:])
        sequence.append(next_number)

    return sequence[:n]


