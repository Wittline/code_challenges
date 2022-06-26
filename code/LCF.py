def LCF(n1, n2):

    greater = max(n1, n2)

    while True:
        if (greater % n1 == 0) and (greater % n2 == 0):
            break
        greater += 1

    return greater