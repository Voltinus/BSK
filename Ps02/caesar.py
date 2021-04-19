from sympy.ntheory.factor_ import totient


class Caesar:
    n = 26

    @staticmethod
    def encode(M, k0, k1):
        ret = ""
        for i in M:
            ret += chr(((ord(i) - ord("A")) * k1 + k0) % Caesar.n + ord("A"))
        return ret

    @staticmethod
    def decode(M, k0, k1):
        ret = ""
        for i in M:
            ret += chr((((ord(i) - ord("A")) + (Caesar.n - k0)) * (k1 ** (totient(Caesar.n)-1))) % Caesar.n + ord("A"))
        return ret
        


if __name__ == "__main__":
    text = "CRYPTOGRAPHY"
    k = 5, 7
    encoded = Caesar.encode(text, k[0], k[1])
    decoded = Caesar.decode(encoded, k[0], k[1])

    print(text)
    print(encoded)
    print(decoded)