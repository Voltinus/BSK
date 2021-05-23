from sympy.ntheory.factor_ import totient


def caesar_encode(M, k0, k1, n=26):
    ret = ""
    for i in M:
        ret += chr(((ord(i) - ord("A")) * k1 + k0) % n + ord("A"))
    return ret


def caesar_decode(M, k0, k1, n=26):
    ret = ""
    for i in M:
        ret += chr((((ord(i) - ord("A")) + (n - k0)) * (k1 ** (totient(n)-1))) % n + ord("A"))
    return ret